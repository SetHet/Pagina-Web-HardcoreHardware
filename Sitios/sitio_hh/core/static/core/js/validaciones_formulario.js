//rut validation function
function checkRut(rut) {
    rut = String(rut);
    var valor = rut.replace(".", "").replace(".", "");
    valor = valor.replace("-", "");
    cuerpo = valor.slice(0, -1);
    dv = valor.slice(-1).toUpperCase();
    rut = cuerpo + "-" + dv;
    if (cuerpo.length < 7) {
      return false;
    }
    suma = 0;
    multiplo = 2;
    for (i = 1; i <= cuerpo.length; i++) {
      index = multiplo * valor.charAt(cuerpo.length - i);
      suma = suma + index;
      if (multiplo < 7) {
        multiplo = multiplo + 1;
      } else {
        multiplo = 2;
      }
    }
    dvEsperado = 11 - suma % 11;
    dv = dv == "K" ? 10 : dv;
    dv = dv == 0 ? 11 : dv;
    if (dvEsperado != dv) {
      return false;
    }
    return true;
  }
  
  $.validator.addMethod("validRut", function(value, element) {
        return checkRut(value);
      }, "Debes ingresar un rut válido");

//Letters only funcion
jQuery.validator.addMethod("lettersonly", function(value, element) {
    return this.optional(element) || /^[a-z]+$/i.test(value);
  }, "Solo estan permitidas las letras");      
$(function() {
    $("#mi_formulario").validate( {
        errorClass: "my-error-class",
        validClass: "my-valid-class",
        rules:
        {
            direccion:
            {
                required:true
            },
            
            acepto_termino:
            {
                required: true
            },
            username:
            {
                required: true,
                minlength:6
            },
            rut: {
                required: true,
                validRut: true
            },
            nombre:
            {
                required:true,
                minlength:2,
                maxlength:30,
                lettersonly: true
            },
            email:
            {
                required:true,
                email:true,
                minlength:6,
                maxlength:100
            },
            password:
            {
                required:true,
                minlength:6,
                maxlength:15
            },
            password_confirm:
            {
                required:true,
                equalTo:"#password"
            },
            comentarios:
            {
                required:true,
                maxlength:100
            },
            acepto_terminos:
            {
                required:true
            },
            fecha_nac:
            {
                required:true
            },       
        },
        messages:
        {
            direccion:
            {
                required:"Debe ingresar una dirección"
            },
            acepto_termino:
            {
                required:"Debe aceptar los términos y condiciones"
            },
            username:
            {
                required:"Debes ingresar un nombre de usuario",
                minlength:"Debe ingresar al menos 6 caracteres para su nombre de usuario"
            },
            rut:
            {
                required:"Debes ingresar tu RUT",
                validRut:"Debe ingresar un RUT valido"
            },

            nombre:
            {
                required:"Debes ingresar tu nombre y apellido.",
                minlength:"Debes ingresar al menos 2 caracteres.",
                maxlength:"Puedes ingresar un máximo de 30 caracteres.",
                lettersonly:"Ingrese un nombre valido"
            },
            email:
            {
                required:"Debes ingresar tu correo electrónico",
                email:"El formato ingresado no corresponde a una dirección de correo.",
                minlength:"Deber ingresar un correo válido",
                maxlength:"Tu correo excede el largo máximo permitido"
            },
            password:
            {
                required:"Debes ingresar una contraseña.",
                minlength:"Tu contraseña debe contener entre 6 y 15 caracteres.",
                maxlength:"Tu contraseña debe contener entre 6 y 15 caracteres."
            },
            password_confirm:
            {
                required:"Debes ingresar nuevamente tu contraseña",
                equalTo:"La contraseña ingresada no es igual a la anterior."
            },
            comentarios:
            {
                required:"Debes ingresar un comentario.",
                maxlength:"Puedes ingresar un máximo de 100 caracteres."
            },
            acepto_terminos:
            {
                required:"Debes aceptar los términos del contrato"
            },
            fecha_nac:
            {
                required:"Debes ingresar una fecha"
            }
        }
    });
});

function limitarCaracteresComentarios (e,contenido, maximoCarateres) {
    // obtenemos la tecla pulsada
    var unicode=e.keyCode? e.keyCode : e.charCode;

    // Permitimos las siguientes teclas:
    // 8 backspace
    // 46 suprimir
    // 13 enter
    // 9 tabulador
    // 37 izquierda
    // 39 derecha
    // 38 subir
    // 40 bajar
    if(unicode==8 || unicode==46 || unicode==13 || unicode==9 || unicode==37 || unicode==39 || unicode==38 || unicode==40)
    {
        return true;
    }    

    // Si ha superado el limite de caracteres devolvemos false
    if(contenido.length >= maximoCarateres)
    {
        return false;
    }
    else
    {
        return true;
    }
}


function actualizarCantidadCaracteres(maximoCarateres) {
    var elemento = document.getElementById("comentarios");
    var informacion = document.getElementById("info");

    if(elemento.value.length >= maximoCarateres)
    {
        informacion.innerHTML = "Máximo " + maximoCarateres + " caracteres";
    }
    else
    {
        informacion.innerHTML = "Puedes escribir " + (maximoCarateres - elemento.value.length) + " caracteres adicionales.";
    }
}