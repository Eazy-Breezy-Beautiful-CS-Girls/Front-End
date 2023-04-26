 AOS.init({
 	duration: 800,
 	easing: 'slide',
 	once: false
 });

jQuery(document).ready(function($) {

	"use strict";

	// $(".loader").delay(1000).fadeOut("slow");
 //  $("#overlayer").delay(1000).fadeOut("slow");	

	var siteMenuClone = function() {

		$('.js-clone-nav').each(function() {
			var $this = $(this);
			$this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
		});


		setTimeout(function() {
			
			var counter = 0;
      $('.site-mobile-menu .has-children').each(function(){
        var $this = $(this);
        
        $this.prepend('<span class="arrow-collapse collapsed">');

        $this.find('.arrow-collapse').attr({
          'data-toggle' : 'collapse',
          'data-target' : '#collapseItem' + counter,
        });

        $this.find('> ul').attr({
          'class' : 'collapse',
          'id' : 'collapseItem' + counter,
        });

        counter++;

      });

    }, 1000);

		$('body').on('click', '.arrow-collapse', function(e) {
      var $this = $(this);
      if ( $this.closest('li').find('.collapse').hasClass('show') ) {
        $this.removeClass('active');
      } else {
        $this.addClass('active');
      }
      e.preventDefault();  
      
    });

		$(window).resize(function() {
			var $this = $(this),
				w = $this.width();

			if ( w > 768 ) {
				if ( $('body').hasClass('offcanvas-menu') ) {
					$('body').removeClass('offcanvas-menu');
				}
			}
		})

		$('body').on('click', '.js-menu-toggle', function(e) {
			var $this = $(this);
			e.preventDefault();

			if ( $('body').hasClass('offcanvas-menu') ) {
				$('body').removeClass('offcanvas-menu');
				$this.removeClass('active');
			} else {
				$('body').addClass('offcanvas-menu');
				$this.addClass('active');
			}
		}) 

		// click outisde offcanvas
		$(document).mouseup(function(e) {
	    var container = $(".site-mobile-menu");
	    if (!container.is(e.target) && container.has(e.target).length === 0) {
	      if ( $('body').hasClass('offcanvas-menu') ) {
					$('body').removeClass('offcanvas-menu');
				}
	    }
		});
	}; 
	siteMenuClone();


	var sitePlusMinus = function() {
		$('.js-btn-minus').on('click', function(e){
			e.preventDefault();
			if ( $(this).closest('.input-group').find('.form-control').val() != 0  ) {
				$(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) - 1);
			} else {
				$(this).closest('.input-group').find('.form-control').val(parseInt(0));
			}
		});
		$('.js-btn-plus').on('click', function(e){
			e.preventDefault();
			$(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) + 1);
		});
	};
	// sitePlusMinus();


	var siteSliderRange = function() {
    $( "#slider-range" ).slider({
      range: true,
      min: 0,
      max: 500,
      values: [ 75, 300 ],
      slide: function( event, ui ) {
        $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
      }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );
	};
	// siteSliderRange();


	

	var siteCarousel = function () {
		if ( $('.nonloop-block-13').length > 0 ) {
			$('.nonloop-block-13').owlCarousel({
		    center: false,
		    items: 1,
		    loop: true,
				stagePadding: 0,
		    margin: 0,
		    smartSpeed: 1000,
		    autoplay: true,
		    nav: true,
				navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
		    responsive:{
	        600:{
	        	margin: 0,
	        	nav: true,
	          items: 2
	        },
	        1000:{
	        	margin: 0,
	        	stagePadding: 0,
	        	nav: true,
	          items: 2
	        },
	        1200:{
	        	margin: 0,
	        	stagePadding: 0,
	        	nav: true,
	          items: 3
	        }
		    }
			});
		}

		let owl2 = $('.slide-one-item-alt-text').owlCarousel({
	    center: false,
	    items: 1,
	    loop: true,
			stagePadding: 0,
	    margin: 0,
	    smartSpeed: 1000,
	    autoplay: true,
	    pauseOnHover: true,
	    onDragged: function(event) {
	    	console.log('event : ',event.relatedTarget['_drag']['direction'])
	    	if ( event.relatedTarget['_drag']['direction'] == 'left') {
	    		$('.owl-1').trigger('next.owl.carousel');
	    	} else {
	    		$('.owl-1').trigger('prev.owl.carousel');
	    	}
	    }
	  });

		let owl = $('.owl-1').owlCarousel({
			// animateOut: 'fadeOut',
			center: true,
			items: 1,
			loop: true,
			margin: 0,
			smartSpeed: 1500,
			dots: true,
	    autoplay: true,
	    pauseOnHover: false,
	    onDragged: function(event) {
	    	console.log('event : ',event.relatedTarget['_drag']['direction'])
	    	if ( event.relatedTarget['_drag']['direction'] == 'left') {
	    		$('.slide-one-item-alt-text').trigger('next.owl.carousel');
	    	} else {
	    		$('.slide-one-item-alt-text').trigger('prev.owl.carousel');
	    	}
	    }
		})

		$( '.owl-dot' ).on( 'click', function() {
		  console.log(owl2.trigger('to.owl.carousel', $(this).index()));
		})




		$('.owl-2').owlCarousel({
			animateOut: 'fadeOut',
			center: true,
			items: 1,
			loop: true,
			margin: 0,
			smartSpeed: 1500,
	    autoplay: true,
	    pauseOnHover: false
		});
		$('.owl-3').owlCarousel({
			animateOut: 'fadeOut',
			center: true,
			items: 1,
			loop: true,
			margin: 0,
			smartSpeed: 1500,
	    autoplay: true,
	    pauseOnHover: false
		})

		$('.slide-one-item').owlCarousel({
	    center: false,
	    items: 1,
	    loop: true,
			stagePadding: 0,
	    margin: 0,
	    smartSpeed: 1500,
	    autoplay: true,
	    pauseOnHover: false,
	    dots: true,
	    nav: false,
	    navText: ['<span class="icon-keyboard_arrow_left">', '<span class="icon-keyboard_arrow_right">']
	  });


	  

	  $('.slide-one-item-alt').owlCarousel({
	    center: false,
	    items: 1,
	    loop: true,
			stagePadding: 0,
	    margin: 0,
	    smartSpeed: 1000,
	    autoplay: true,
	    pauseOnHover: true,
	    onDragged: function(event) {
	    	console.log('event : ',event.relatedTarget['_drag']['direction'])
	    	if ( event.relatedTarget['_drag']['direction'] == 'left') {
	    		$('.slide-one-item-alt-text').trigger('next.owl.carousel');
	    	} else {
	    		$('.slide-one-item-alt-text').trigger('prev.owl.carousel');
	    	}
	    }
	  });

	  if ( $('.owl-all').length > 0 ) {
			$('.owl-all').owlCarousel({
		    center: false,
		    items: 1,
		    loop: false,
				stagePadding: 0,
		    margin: 0,
		    autoplay: false,
		    nav: false,
		    dots: true,
		    touchDrag: true,
  			mouseDrag: true,
  			smartSpeed: 1000,
				navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
		    responsive:{
	        768:{
	        	margin: 30,
	        	nav: false,
	        	responsiveRefreshRate: 10,
	          items: 1
	        },
	        992:{
	        	margin: 30,
	        	stagePadding: 0,
	        	nav: false,
	        	responsiveRefreshRate: 10,
	        	touchDrag: false,
  					mouseDrag: false,
	          items: 3
	        },
	        1200:{
	        	margin: 30,
	        	stagePadding: 0,
	        	nav: false,
	        	responsiveRefreshRate: 10,
	        	touchDrag: false,
  					mouseDrag: false,
	          items: 3
	        }
		    }
			});
		}
		
	};
	siteCarousel();

	

	var siteCountDown = function() {

		$('#date-countdown').countdown('2020/10/10', function(event) {
		  var $this = $(this).html(event.strftime(''
		    + '<span class="countdown-block"><span class="label">%w</span> weeks </span>'
		    + '<span class="countdown-block"><span class="label">%d</span> days </span>'
		    + '<span class="countdown-block"><span class="label">%H</span> hr </span>'
		    + '<span class="countdown-block"><span class="label">%M</span> min </span>'
		    + '<span class="countdown-block"><span class="label">%S</span> sec</span>'));
		});
				
	};
	// siteCountDown();

	var siteDatePicker = function() {

		if ( $('.datepicker').length > 0 ) {
			$('.datepicker').datepicker();
		}

	};
	// siteDatePicker();

	var siteSticky = function() {
		$(".js-sticky-header").sticky({topSpacing:0});
	};
	siteSticky();

	// navigation
  var OnePageNavigation = function() {
    var navToggler = $('.site-menu-toggle');

   	$("body").on("click", ".main-menu li a[href^='#'], .smoothscroll[href^='#'], .site-mobile-menu .site-nav-wrap li a[href^='#']", function(e) {
      e.preventDefault();

      var hash = this.hash;

      $('html, body').animate({
        'scrollTop': $(hash).offset().top - 50
      }, 600, 'easeInOutExpo', function() {
        // window.location.hash = hash;

      });

    });
  };
  OnePageNavigation();

  var siteScroll = function() {

  	

  	$(window).scroll(function() {

  		var st = $(this).scrollTop();

  		if (st > 100) {
  			$('.js-sticky-header').addClass('shrink');
  		} else {
  			$('.js-sticky-header').removeClass('shrink');
  		}

  	}) 

  };
  siteScroll();


  var counter = function() {
		
		$('#about-section').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {

				var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')
				$('.number > span').each(function(){
					var $this = $(this),
						num = $this.data('number');
					$this.animateNumber(
					  {
					    number: num,
					    numberStep: comma_separator_number_step
					  }, 7000
					);
				});
				
			}

		} , { offset: '95%' } );

	}
	counter();



});



const tagInput = document.getElementById('tagInput');
const tagsContainer = document.querySelector('.tags-container');
const hiddenTagsInput = document.getElementById('tags');

tagInput.addEventListener('input', () => {
  const filter = tagInput.value.toUpperCase();
  const dropdownMenu = document.querySelector('.dropdown-menu');
  const tags = dropdownMenu.getElementsByTagName('li');
  let hasVisibleTags = false;
  for (let i = 0; i < tags.length; i++) {
    const tagText = tags[i].textContent || tags[i].innerText;
    if (tagText.toUpperCase().indexOf(filter) > -1 && !isTagSelected(tagText)) {
      tags[i].style.display = '';
      hasVisibleTags = true;
    } else {
      tags[i].style.display = 'none';
    }
  }
  dropdownMenu.style.display = hasVisibleTags ? 'block' : 'none';
});

document.addEventListener('click', (event) => {
  const dropdownMenu = document.querySelector('.dropdown-menu');
  if (!event.target.matches('.dropdown-toggle')) {
    dropdownMenu.style.display = 'none';
  }
});

document.addEventListener('click', (event) => {
  const dropdownMenu = document.querySelector('.dropdown-menu');
  if (event.target.matches('.dropdown-menu li')) {
    const tagText = event.target.textContent || event.target.innerText;
    createTag(tagText);
    tagInput.value = '';
    dropdownMenu.style.display = 'none';
  }
});

tagsContainer.addEventListener('click', (event) => {
  if (event.target.matches('.tag')) {
    const tag = event.target;
    const tagText = tag.textContent || tag.innerText;
    tag.remove();
    removeTagFromInput(tagText);
  }
});

function createTag(text) {
  const tags = document.querySelectorAll('.tag');
  for (let i = 0; i < tags.length; i++) {
    if (tags[i].textContent5 === text) {
      return;
    }
  }

  const tag = document.createElement('div');
  tag.classList.add('tag');
  tag.textContent = text;
  tagsContainer.appendChild(tag);
  addTagToInput(text);
}

function isTagSelected(text) {
  const hiddenTags = hiddenTagsInput.value.split(',');
  return hiddenTags.includes(text);
}

function addTagToInput(text) {
  const hiddenTags = hiddenTagsInput.value.split(',');
  if (!hiddenTags.includes(text)) {
    hiddenTags.push(text);
  }
  hiddenTagsInput.value = hiddenTags.join(',');
}

function removeTagFromInput(text) {
  const hiddenTags = hiddenTagsInput.value.split(',');
  const index = hiddenTags.indexOf(text);
  if (index > -1) {
    hiddenTags.splice(index, 1);
  }
  hiddenTagsInput.value = hiddenTags.join(',');
}




  


// Add this function to handle the file upload
async function uploadImage(file) {
	const formData = new FormData();
	formData.append("image", file);
  
	try {
	  const response = await fetch("/upload", {
		method: "POST",
		body: formData
	  });
  
	  if (response.ok) {
		const jsonResponse = await response.json();
		console.log("Image uploaded successfully:", jsonResponse);
	  } else {
		console.error("Error uploading image:", response.statusText);
	  }
	} catch (error) {
	  console.error("Error uploading image:", error);
	}
  }
  
  // Modify the drop event listener to call the uploadImage function
  dragDropArea.addEventListener("drop", (event) => {
	event.preventDefault();
	const files = event.dataTransfer.files;
	if (files.length === 1) {
	  const file = files[0];
	  if (file.type.startsWith("image/")) {
		uploadImage(file);
	  } else {
		alert("Please drop an image file.");
	  }
	} else {
	  alert("Please drop only one file.");
	}
  });
  

  const imageInput = document.getElementById("imageInput");

// Trigger the click event for the hidden input when the drag-and-drop area is clicked
dragDropArea.addEventListener("click", () => {
  imageInput.click();
});

// Handle the selected file when the hidden input changes
imageInput.addEventListener("change", () => {
  const file = imageInput.files[0];
  if (file && file.type.startsWith("image/")) {
    uploadImage(file);
  }
});

function validateImage(input) {
	if (input.files && input.files[0]) {
	  const file = input.files[0];
	  const fileType = file["type"];
	  const validImageTypes = ["image/gif", "image/jpeg", "image/png", "image/svg+xml", "image/webp"];
	  if (validImageTypes.includes(fileType)) {
		const reader = new FileReader();
		reader.onload = function(e) {
		  const preview = document.getElementById("dragDropArea");
		  preview.style.backgroundImage = `url(${e.target.result})`;
		  preview.style.backgroundSize = "cover";
		  preview.style.backgroundPosition = "center";
		  preview.innerHTML = "";
		};
		reader.readAsDataURL(file);
	  } else {
		alert("Please choose a valid image file (jpg, png, gif, svg, or webp).");
		input.value = "";
	  }
	}
  }

  

  
  
  
  
  document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
	const dropZoneElement = inputElement.closest(".drop-zone");

	dropZoneElement.addEventListener("click", (e) => {
		inputElement.click();
	});

	inputElement.addEventListener("change", (e) => {
		if (inputElement.files.length) {
			updateThumbnail(dropZoneElement, inputElement.files[0]);
		}
	});

	dropZoneElement.addEventListener("dragover", (e) => {
		e.preventDefault();
		dropZoneElement.classList.add("drop-zone--over");
	});

	["dragleave", "dragend"].forEach((type) => {
		dropZoneElement.addEventListener(type, (e) => {
			dropZoneElement.classList.remove("drop-zone--over");
		});
	});

	dropZoneElement.addEventListener("drop", (e) => {
		e.preventDefault();

		if (e.dataTransfer.files.length) {
			inputElement.files = e.dataTransfer.files;
			updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
		}

		dropZoneElement.classList.remove("drop-zone--over");
	});
});

/**
 * Updates the thumbnail on a drop zone element.
 *
 * @param {HTMLElement} dropZoneElement
 * @param {File} file
 */
function updateThumbnail(dropZoneElement, file) {
	let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

	// First time - remove the prompt
	if (dropZoneElement.querySelector(".drop-zone__prompt")) {
		dropZoneElement.querySelector(".drop-zone__prompt").remove();
	}

	// First time - there is no thumbnail element, so lets create it
	if (!thumbnailElement) {
		thumbnailElement = document.createElement("div");
		thumbnailElement.classList.add("drop-zone__thumb");
		dropZoneElement.appendChild(thumbnailElement);
	}

	thumbnailElement.dataset.label = file.name;

	// Show thumbnail for image files
	if (file.type.startsWith("image/")) {
		const reader = new FileReader();

		reader.readAsDataURL(file);
		reader.onload = () => {
			thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
		};
	} else {
		thumbnailElement.style.backgroundImage = null;
	}
}


function showPreview(event){
	if(event.target.files.length > 0){
	  var src = URL.createObjectURL(event.target.files[0]);
	  var preview = document.getElementById("file-ip-1-preview");
	  preview.src = src;
	  preview.style.display = "block";
	}
  }