jQuery.validator.addMethod("lettersonly", function(value, element) {
    return this.optional(element) || /^[a-z]+$/i.test(value);
  }, "Solo estan permitidas las letras");      
$(function() {
    $("#formulario_login").validate( {
        errorClass: "my-error-class",
        validClass: "my-valid-class",
        rules:
        {
            username:
            {
                required: true,
                // minlength:6
            },
            // chkbox:{
            //     required: true,
            // },

            password:
            {
                required:true,
                // minlength:6,
                // maxlength:15
            }  
        },
        messages:
        {
            // chkbox:{
            //     required:"cualquier cosa", 
            // },
            username:{
                required:"Debes ingresar un nombre de usuario",
                // minlength:"Debe ingresar al menos 6 caracteres para su nombre de usuario"
            },
            password:
            {
                required:"Debes ingresar una contraseña.",
                // minlength:"Tu contraseña debe contener entre 6 y 15 caracteres.",
                // maxlength:"Tu contraseña debe contener entre 6 y 15 caracteres."
            }
        }
    });
});

function mensajeError() {
  alert("Usuario y/o Contraseña invalida, intente nuevamente");
}
