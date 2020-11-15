//Variables
const diasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
const mesesAnno = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Dicimbre'];


//Ready Page
$(document).ready(function(){
    actualizarDia();
    actualizarHora();    
});



//Funciones
function actualizarDia(){
    var elements = document.getElementsByClassName('fecha');

    var date = new Date();
    var diaSemana = diasSemana[date.getDay() - 1];
    var diaMes = date.getDate();
    var mes = mesesAnno[date.getMonth()];
    var anno = date.getFullYear();

    var fecha = diaSemana + ", " + diaMes + " del " + mes + " de " + anno;

    for(var i = 0; i < elements.length; i++){
        elements[i].innerHTML = fecha;
    }

    setTimeout(function(){actualizarDia();},  500);
}

function actualizarHora(){
    var time = new Date();
    var horas = time.getHours();
    var minutos = time.getMinutes();
    var segundos = time.getSeconds();

    var str =  horas.toString().padStart(2, "0") + ":" + minutos.toString().padStart(2, "0") + ":" + segundos.toString().padStart(2, "0");

    var timers = document.getElementsByClassName("hora");
    for(var i = 0; i < timers.length; i++){
        timers[i].innerHTML = str;
    }

    setTimeout(function(){actualizarHora();},  500);

}