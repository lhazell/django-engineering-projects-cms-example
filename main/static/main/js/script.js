/*      CONTENTS:
 *  1. Slider Initialization
 *  3. Google Maps Setup
 *  3. Project Slider
 *  4. Map Animation
 */

$(document).ready(function() {

/**************************************
    1. Slider Initialization
***************************************/

    var sliderControl = (function (){

        //slidesjs initialization
        $(function() {
            $('#slides').slidesjs({
                height: 'auto',
                start: 1,
                navigation: {
                    active: false
                },
                pagination: {
                    active: false
                },
                play: {
                    active: false,
                    effect: "fade",
                    interval: 5000,
                    auto: true,
                    swap: true,
                    pauseOnHover: false,
                    restartDelay: 2500
                }
            });
        });

    }());


/**************************************
    2. Google Maps Setup
***************************************/

  if ($(".map").length) {
    google.maps.visualRefresh = true;

    var EBS_MapObject = (function() {
      var ebsEngineering = new google.maps.LatLng(25.917059, -80.276537),
        miamiDade = new google.maps.LatLng(25.914589, -80.278028),
        //make the map un-draggable on mobile
        drag = (getBootstrapWidth() === 'xs') ? false : true;
        myOptions = {
          'scrollwheel': false,
          zoom: 14,
          'draggable': drag,
          center: miamiDade,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        return {
          loadNorthMiami: function() {
            if ($(".map").length) {
              var image = new google.maps.MarkerImage(DJANGO_STATIC_URL+"main/img/mapStake@2x.png", null, null, null, new google.maps.Size(288,133)); // Create a variable for our marker image.


              var map = new google.maps.Map($(".map")[0], myOptions),
                  marker = new google.maps.Marker({
                    position: ebsEngineering,
                    icon: image,
                    title:'Click to zoom',
                  });

              marker.setMap(map);
              
              google.maps.event.addListener(marker,'click',function() {
                 window.location.href='https://www.google.com/maps/dir//EBS+Engineering+Inc,+4715+NW+157th+St+%23+202,+Hialeah,+FL+33014/@25.916794,-80.276558,17z/data=!4m12!1m3!3m2!1s0x88d9aff7d9282721:0xce16a409b4977518!2sEBS+Engineering+Inc!4m7!1m0!1m5!1m1!1s0x88d9aff7d9282721:0xce16a409b4977518!2m2!1d-80.276558!2d25.916794';
              });

              google.maps.event.trigger(map, 'resize');
              map.panTo(miamiDade);
            }
          }
        };
    }());

    //Draw North Miami
    EBS_MapObject.loadNorthMiami();
  }

/**************************************
    3. Projects Slider
***************************************/

  var ProjectsSlider = (function() {
    //get slider variables
    var slidesContainer = $('.projects-slider .slides'),
      slider = $('#projects-slider'),
      displayCurrent = $(slider).find('.position-display .current'),
      displayTotal = $(slider).find('.position-display .total'),
      next = slider.find('.next'),
      previous = slider.find('.previous'),
      slides = $('.slides-container').find('.slides > li'),
      sliderContainerOffset = 0,
      setDisplayTotal = function() {
        $(displayTotal).html('' + ( slides.length ) + '');
      },
      initSliderContainerOffset = function() {
        //slide offset = (window - slide)/2
        var slideWidth = slides.first().width(),
            windowWidth = $(window).width(),
            offset = (windowWidth - slideWidth)/2;
        
        //setOffset to slidesContainer
        $(slidesContainer).css("marginLeft", offset);
        sliderContainerOffset = offset;
      },
      getActive = function() {
        var activeSlide;
        $(slides).each(function() {
          if ($(this).hasClass('active')) {
            activeSlide = $(this);
            return false;
          }
        });
        return activeSlide;
      },
      slideFrom = function(from) {
        //get offset to slide (current - active)
        var activeSlide = $(getActive()),
            slidesContainerLeftMargin = parseInt($(slidesContainer).css( "marginLeft" ), 10),
            slidingOffset = (($(from).offset().left - $(activeSlide).offset().left)) + slidesContainerLeftMargin;

        //console.log( "From Index: " + $( slides ).index( from ) );
        //console.log( "Active Index: " + $( slides ).index( activeSlide ) + "\nOffset = " + slidingOffset);
        
        //set sliderContainer sliding offset
        $(slidesContainer).css("marginLeft", slidingOffset);

        //update the position display
        $(displayCurrent).html('' + ($( slides ).index( activeSlide ) + 1) + '');
      };


    //button handlers
    next.click(function(e){
      var activeSlide = $(getActive());
          previousSlide = activeSlide; //for clarity

      //add active class to next | first
      if ($(activeSlide).next('li').length) {
        $(activeSlide).removeClass('active').next('li').addClass('active');
      }
      else {
        $(activeSlide).removeClass('active');
        slides.first().addClass('active');
      }
      //move to active slide
      slideFrom(previousSlide);
    });

    previous.click(function(e){
      var activeSlide = $(getActive());
          previousSlide = activeSlide; //for clarity

      //add active class to next | last
      if ($(activeSlide).prev('li').length) {
        //console.log("There is a previous");
        $(activeSlide).removeClass('active').prev('li').addClass('active');
      }
      else {
        //console.log("There is NOT a previous");
        $(activeSlide).removeClass('active');
        slides.last().addClass('active');
      }
      //move to active slide
      slideFrom(previousSlide);

    });

    //register post-resize actions
    $(window).on('resize', function(){
      //var win = $(this); //this = window

      //console.log('Hey! The window was resized!');
      initSliderContainerOffset();
    });

    return {
      init: function() {
        //get and set initial offset
        initSliderContainerOffset();
        //set first element to active
        slides.first().addClass('active');
        //set display count/total
        setDisplayTotal();
      }
    };
  }());

  ProjectsSlider.init();

/**************************************
    4. Map Animation
***************************************/

  var mapAnimation = (function() {
    var leadIn = 490,
      navHeight = $('.navbar').height(),
      headerheight = $('.header').height(),
      $mapContainer = $('#corporate-overview'),
      $message = $($mapContainer).find('.united-states .message');
      //get the beginning of the map/corporate-overview block
      mapStart = $($mapContainer).offset().top - (navHeight + leadIn + headerheight),
      mapEnd = ( ( parseInt($($mapContainer).height(), 10) + parseInt($($mapContainer).offset().top, 10) )),
      viewPortBottom = mapStart + $(window).height(),
      iterateSpeed = 100,
      mapInView = function () {
        var scrollPosition = getScrollPosition();

        return ((scrollPosition > mapStart ) && (scrollPosition < mapEnd));
      },
      iterate = function() {
        if ($('ul.stately > li.projects.not-colored, .caribbean .projects.not-colored').length) {
          setTimeout(function() {
            console.log("I ran");
            $('ul.stately > li.projects.not-colored, .caribbean .projects.not-colored').random().removeClass('not-colored');
            iterate();
          }, iterateSpeed); // .5 second
        }
        else {
          //show message after last state colored
          setTimeout(function(){
            $($message).fadeIn('fast');
            //TODO: set state number with js
          }, iterateSpeed);
        }
      };

      return {
        initializeMapAnimation: function () {
          //hide message for after animation complete
          $($message).hide();
        },
        checkAnimation: function () {
            var leadTime = 500;
              animated = $($mapContainer).hasClass('animated');

            //Check if services list is in view and if the animated class has been added
            if( mapInView() && !animated) {
                console.log("map in view");
                $($mapContainer).addClass('animated');
                iterate();
            }
            else {
                return;
            }
        }
      };
  }());
  
  //initialze map animation
  mapAnimation.initializeMapAnimation();

  $(window).scroll(function(){
      mapAnimation.checkAnimation();
  });
}); //end