jQuery.validator.addMethod("lettersonly", function(value, element) {
    return this.optional(element) || /^[a-z]+$/i.test(value);
  }, "Solo estan permitidas las letras");      
$(function() {
    $("#validarCorreo").validate( {
        errorClass: "my-error-class",
        validClass: "my-valid-class",
        onclick: false,
        rules:
        {
            email:
            {
                required:true,
                email:true,
                minlength:6,
                maxlength:100
            }
        },
        messages:
        {
            email:
            {
                required:"Debes ingresar tu correo electrónico",
                email:"El formato ingresado no corresponde a una dirección de correo.",
                minlength:"Deber ingresar un correo válido",
                maxlength:"Tu correo excede el largo máximo permitido"
            }
        }
        

    });
});
$.validator.setDefaults({
    submitHandler: function() { alert("Enlace de verificación enviado!"); }
});

$().ready(function() {
    // validate the comment form when it is submitted
    $("#validarCorreo").validate();
})