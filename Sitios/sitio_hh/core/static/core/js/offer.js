//Parametros
const classOfferTitle = 'offer-title';
const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

//Evento
$(document).ready(function(){
    ActualizarOfertaTime();
    ActualizarTitulo();
});


//Funciones
function ActualizarOfertaTime(){
    var time = new Date();
    var horas = (24 - time.getHours()) - 1;
    var minutos = (60 - time.getMinutes()) - 1;
    var segundos = (60 - time.getSeconds()) - 1;

    var str =  horas.toString().padStart(2, "0") + "H : " + minutos.toString().padStart(2, "0") + "M : " + segundos.toString().padStart(2, "0") + "S";

    var timers = document.getElementsByClassName("tiempo_limite");
    for(var i = 0; i < timers.length; i++){
        timers[i].innerHTML = str;
    }

    setTimeout(function(){ActualizarOfertaTime();},  500);
}

function ActualizarTitulo(){
    var time = new Date();
    
    var str =  'Black ' + daysOfWeek[time.getDay()] + '!';

    var titles = document.getElementsByClassName(classOfferTitle);
    for(var i = 0; i < titles.length; i++){
        titles[i].innerHTML = str;
    }

    setTimeout(function(){ActualizarTitulo();},  500);
}