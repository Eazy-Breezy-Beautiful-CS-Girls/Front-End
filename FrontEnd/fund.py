from base64 import b64encode
import datetime
from flask import Blueprint, flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from FrontEnd.auth import login_required
import os
import json

from FrontEnd.database import get_db

bp = Blueprint("fund", __name__)

@bp.route('/', methods=['GET'])
def index():
    with get_db().cursor() as cursor:
        cursor.execute('SELECT * FROM Funds')
        funds = cursor.fetchall()
        fund_images = []
        fund_data = zip(funds, fund_images)
        for fund in funds:
            cursor.execute('SELECT picture FROM Images WHERE FundName = %s LIMIT 1', (fund[0],))
            image = cursor.fetchone()
            if image:
                fund_images.append(b64encode(image[0]).decode('utf-8'))
            else:
                fund_images.append(None)
        return render_template('index.html', fund_data=fund_data)

@bp.route('/fundraisers/<string:fund_name>', methods=['GET','POST'])
def fundraisers(fund_name):
    if request.method == 'POST':
        title = fund_name
        amount = request.form.get('amount')
        comment = request.form.get('comment')
        get_db().cursor().execute('UPDATE Funds SET FundRaised = FundRaised+%s WHERE FundName = %s',(amount,title))
        get_db().commit()
        if g.user:
            get_db().cursor().execute('INSERT INTO Donations (FundName, UserID, DonoAmount, DonoTime, DonoComment) VALUES (%s,%s,%s,%s,%s)',(title,g.user,amount,datetime.datetime.now(),comment))
            get_db().commit()
        return redirect(url_for('index'))
    with get_db().cursor() as cursor:
        cursor.execute('SELECT * FROM Funds WHERE FundName = %s',(fund_name))
        fund = cursor.fetchone()
        cursor.execute('SELECT picture FROM Images WHERE FundName = %s',(fund_name))
        imagesFetch = cursor.fetchall()
        images=list()
        for image in imagesFetch:
            images.append(b64encode(image[0]).decode('utf-8'))
        cursor.execute('SELECT UserID,DonoAmount,DonoComment FROM Donations WHERE FundName = %s', (fund_name))
        comments = cursor.fetchall()

    return render_template('fundraisers.html', fund=fund, images=images, comments=comments)

@bp.route('/form', methods=['GET', 'POST'])
@login_required
def form():
    if request.method == 'GET':
        min_date = datetime.date.today().isoformat()
        return render_template('form.html', min_date=min_date)
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        goal = int(request.form.get('goal').replace(',',''))
        user_id = g.user[0]
        end_date = request.form.get('date')
        start_date = datetime.datetime.now()
        tags = request.form.get('tags')
        
        # Insert fundraiser information and image into the database
        with get_db().cursor() as cursor:
            cursor.execute('SELECT FundName FROM Funds WHERE FundName=%s',(title))
            try:
                cursor.execute('INSERT INTO Funds (FundName, FundEndDate, FundDesc, FundGoal, FundRaised, FundStart, FundTags) VALUES (%s, %s, %s, %s, 0, %s, %s)', (title, end_date, description, goal, start_date, tags))
                cursor.execute('INSERT INTO UserFundLink (UserId,FundName) VALUES (%s,%s)', (user_id, title))
            except:
                flash('Fundraiser name already exists')
                min_date = datetime.date.today().isoformat()
                return render_template('form.html', min_date=min_date)
            # Save the image
            upload = request.files.getlist('myFile')
            for image in upload:
                image.save(image.filename)
                with open(image.filename, 'rb') as f:
                    binaryData = f.read()
                cursor.execute('INSERT INTO Images (FundName, picture) VALUES (%s, %s)', (title, binaryData))
                get_db().commit()
                # Remove the saved image file
                os.remove(image.filename)
        
        return redirect(url_for('fund.fundraisers', fund_name=title))




