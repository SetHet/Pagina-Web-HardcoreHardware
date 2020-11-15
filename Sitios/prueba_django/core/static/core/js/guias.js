$(document).ready(
    function(){
        EnableSection('guia-section-1');
    }
);

function EnableSection(id_activar){
    
    var list_elements = document.getElementsByClassName('guia-section');

    for (var i = 0; i < list_elements.length; i++){
        list_elements[i].style.display = "none";
    }

    var elementSelect = document.getElementById(id_activar);

    elementSelect.style.display = "block";
}
