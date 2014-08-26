/**************************************
    1. Contact Form Validation
***************************************/

    if ($('#contact form').length) {
        $('#contact form').bootstrapValidator({
          fields: {
              message: {
                  validators: {
                      notEmpty: {
                          message: 'A message is required and cannot be empty'
                      }
                  }
              },
              email: {
                  validators: {
                      notEmpty: {
                          message: 'An e-mail address is required'
                      },
                      emailAddress: {
                          message: 'The input is not a valid email address'
                      }
                  }
              },
          }
        }).on('success.form.bv', function(e) {

          // Get the form instance
          var $form = $(e.target);


          if (($form.hasClass('ajax'))) {
            // Prevent form submission
            e.preventDefault();

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                // ... Process the result ...

                if (result.status == 'success') {
                  $("#contact .ajax-response").addClass(result.status).find('h3').html('' + result.message + '');
                  setTimeout(function() {
                    $('#contact').modal('hide');
                  }, 3000);
                } else {
                  $('#contact .ajax-response').addClass(result.status).find('h3').html('' + result.message + '');
                  $('#contact form').data('bootstrapValidator').resetForm(true);
                  setTimeout(function() {
                    $('#contact .ajax-response').removeClass(result.status).find('h3').html('');
                  }, 3000);
                }

            }, 'json');

          }

        });
    }