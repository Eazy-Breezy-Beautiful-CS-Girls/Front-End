# Front-End

1. 
```powershell
pip install -r "FrontEnd/requirements.txt"
```

2. Make sure you are in the main folder that was created when you cloned the github repo like:
C:\Users\Jacob\cs projects\CS-451R-wholething\Front-End

3. You can install our app with:
```powershell
pip install -e .
```
while you are in the outer Front-End folder

4. Then 
```powershell
flask --app FrontEnd run --debug
```
Note: please have the required dependencies installed in order to run the program:
```flask
pymysql
pytest
coverage
```

5. this will run a local server that will show a development version and just click the link that looks like an ip that gets generated
