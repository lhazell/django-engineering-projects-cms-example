
/*      CONTENTS:

 *  1. Helper functions
 *  2. Navigation Position Setter
 *  3. Scrolling Navigaion
 */

/**************************************
    1. Helper Functions
***************************************/

var getDeviceHeight = function() {
    if (typeof(window.innerHeight) == 'number') {
        //Non-IE
        return window.innerHeight;
    } else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
        //IE 6+ in 'standards compliant mode'
        return document.documentElement.clientHeight;
    } else if (document.body && (document.body.clientWidth || document.body.clientHeight)) {
        //IE 4 compatible
        return document.body.clientHeight;
    }
    return 0;
};

//Checks device width and returns Bootstrap width class identifier
var getBootstrapWidth = function() {
    var deviceWidth = getDeviceWidth();
    if (deviceWidth >= 1200) {
        return 'lg';
    } else if (deviceWidth >= 992 && deviceWidth < 1200) {
        return 'md';
    } else if (deviceWidth >= 768 && deviceWidth < 992) {
        return 'sm';
    } else if (deviceWidth < 768) {
        return 'xs';
    } else {
        return 'unknown';
    }
};

//Returns window with (Respond.js)
var getDeviceWidth = function() {
    if (typeof(window.innerWidth) == 'number') {
        //Non-IE
        return window.innerWidth;
    } else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
        //IE 6+ in 'standards compliant mode'
        return document.documentElement.clientWidth;
    } else if (document.body && (document.body.clientWidth || document.body.clientHeight)) {
        //IE 4 compatible
        return document.body.clientWidth;
    }
    return 0;
};

var getSubDocument = function(embedding_element) {
    if (embedding_element.contentDocument)
        return embedding_element.contentDocument;
    else {
        var subdoc = null;
        try {
            subdoc = embedding_element.getSVGDocument();
        } catch(e) {}
        return subdoc;
    }
};

var getScrollPosition = function() {
    return $(window).scrollTop();
};

jQuery.fn.random = function() {
    var randomIndex = Math.floor(Math.random() * this.length);
    return jQuery(this[randomIndex]);
};

$(document).ready(function() {

/**************************************
    2. Navigation Position Setter
***************************************/

    var navPositionObject = (function() {
        //get margin-top-fixed height
        //console.log('margin-top-fixed: ' + $('.navbar-fixed-top').css('height'));
        //get margin-top height

        //use the difference to add/subtract from body margin


        var navHeight = parseInt($(".navbar").css("min-height"), 10),
            navTop = $(".header").height();

        $(window).bind('scroll', function() {
            var navbarFixedHeight = 70;
                nextSibling = $(".navbar").next('div');
            
            if (!(getBootstrapWidth() == 'xs') && ($(window).scrollTop() > navTop)) {
                //$(document.body).addClass("navbar-fixed");
                $(".navbar").addClass("navbar-fixed-top");
            }
            else {
                //$(document.body).removeClass("navbar-fixed");
                $(".navbar").removeClass("navbar-fixed-top");
            }
        });
    }());

/**************************************
    3. Scrolling Navigaion
***************************************/

    var scrollingNavigation = (function() {
        var lastId,
            offset = 15,
            heroHeight = $(".hero").height();
            topMenu = $(".nav"),
            topMenuHeight = topMenu.outerHeight() + offset,
            //select only id href
            menuItems = topMenu.find("[href^='#']"),
            scrollItems = menuItems.map(function() {
                var item = $($(this).attr("href"));
                if (item.length) {
                    return item;
                }
            });
        
        // Bind click handler to menu items
        menuItems.click(function(e){
          var href = $(this).attr("href"),
              offsetTop = ($(href).offset().top-topMenuHeight+1) || 0;

          $('html, body').stop().animate({
              scrollTop: offsetTop
          }, 300);
          e.preventDefault();
        });

        // Bind to scroll
        $(window).scroll(function(){
          // Get container scroll position
          var fromTop = $(this).scrollTop() + topMenuHeight;
        
          // Get id of current scroll item
          var current = scrollItems.map(function() {
            var documentBottom = $(document).height(),
              atBottom = ($(this).scrollTop() + $(this).height()) == $(document).height();
               
            if ($(this).offset().top < fromTop) {
              return this;
            }
            //if element bottom == document bottom (i.e. too small, didn't trigger fromTop):
            else if ((($(window).height() + $(window).scrollTop()) >= $(document).height()) && (($(this).height() + $(this).offset().top) == $(document).height())) {
              return this;
            }

          });

          // Get the id of the current element
          current = current[current.length-1];
          var id = current && current.length ? current[0].id : "";
           
          if (lastId !== id) {
            lastId = id;
            // Set/remove active class
            menuItems
              .parent().removeClass("active")
              .end().filter("[href=#"+id+"]").parent().addClass("active");
          }
        });


    }());

}); //end