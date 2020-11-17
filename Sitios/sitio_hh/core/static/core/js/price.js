//variables
var dolar = 700;
var euro = 1;
var uf = 1;

const idCalcEntrada = 'txt_entrada';
const idCalcSalida = 'txt_salida';

$(document).ready(function(){
    ActualizarMonedas();
});

//Precio Dolar
function ActualizarMonedas(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', 'https://mindicador.cl/api', true);
    xmlhttp.send();


    xmlhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
                var data = JSON.parse(this.responseText);

                uf = data.uf.valor;
                dolar = data.dolar.valor;
                euro = data.euro.valor;
        }

        //Actualizar Indicadores de precio
        var elements;
        var i;

        //Dolar
        elements = document.getElementsByClassName('valorDolar');
        for (i = 0; i < elements.length; i++){
            elements[i].innerHTML = new Intl.NumberFormat('es-CL', {style:'currency', currency:'CLP', maximumFractionDigits:2}).format(dolar) + " CLP";    
        }

        //Euro
        elements = document.getElementsByClassName('valorEuro');
        for (i = 0; i < elements.length; i++){
            elements[i].innerHTML = new Intl.NumberFormat('es-CL', {style:'currency', currency:'CLP', maximumFractionDigits:2}).format(euro) + " CLP";    
        }

        //UF
        elements = document.getElementsByClassName('valorUF');
        for (i = 0; i < elements.length; i++){
            elements[i].innerHTML = new Intl.NumberFormat('es-CL', {style:'currency', currency:'CLP', maximumFractionDigits:2}).format(uf) + " CLP";    
        }
    }
}

//Funciones

function GetCLP(pesos){
    var formato_numero = Intl.NumberFormat();
    var str = formato_numero.format(pesos);
    document.write("$ " + str + " CLP");
}

function GetDolars(pesos){
    var formato_numero = Intl.NumberFormat();
    var str = formato_numero.format(parseInt(pesos/dolar)+0.99);
    document.write("$ " + str + " Dolares");
}

//Funciones Calculado de divisas
function GetFloatEntrada(){
    var input = document.getElementById(idCalcEntrada).value;
    return input;
}

function ActualizarSalida(valor){
    var input = document.getElementById(idCalcSalida);
    input.value = parseFloat(valor);
}

function ActulizarTipoMoneda(entrada, salida){
    var elem_entrada = document.getElementById("tipoMoneda_Entrada");
    var elem_salida = document.getElementById("tipoMoneda_Salida");

    elem_entrada.innerHTML = entrada;
    elem_salida.innerHTML = salida;
}


//clp dolar
function calc_clp_a_dolar(){
    var valor = GetFloatEntrada();
    var dolares = valor / dolar;
    ActualizarSalida(dolares);
    ActulizarTipoMoneda('CLP', 'Dolares')
}

function calc_dolar_a_clp(){
    var valor = GetFloatEntrada();
    var pesos = valor * dolar;
    ActualizarSalida(pesos);
    ActulizarTipoMoneda('Dolares', 'CLP')
}

//clp euro
function calc_clp_a_euro(){
    var valor = GetFloatEntrada();
    var euros = valor / euro;
    ActualizarSalida(euros);
    ActulizarTipoMoneda('CLP', 'Euros')
}

function calc_euro_a_clp(){
    var valor = GetFloatEntrada();
    var pesos = valor * euro;
    ActualizarSalida(pesos);
    ActulizarTipoMoneda('Euros', 'CLP')
}

//clp uf
function calc_clp_a_uf(){
    var valor = GetFloatEntrada();
    var ufs = valor / uf;
    ActualizarSalida(ufs);
    ActulizarTipoMoneda('CLP', 'UF')
}

function calc_uf_a_clp(){
    var valor = GetFloatEntrada();
    var pesos = valor * uf;
    ActualizarSalida(pesos);
    ActulizarTipoMoneda('UF', 'CLP')
}