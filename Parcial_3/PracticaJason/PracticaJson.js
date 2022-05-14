$(Document).ready(function(){
    $('#botonAjax').click(function(){
        

            var solicitud = new XMLHttpRequest();          //Crear objeto XMLHttpRequest
            
            solicitud.onreadystatechange = function() {   // En esta propiedad declaramos la funcion a ejecutar
                                                        // cuando cambie el status del objeto XMLHttpRequest
            
                if (solicitud.readyState == 4 && solicitud.status == 200) {                 // La respueta esta lista
                    document.getElementById("idHeader").innerHTML = solicitud.responseText;  // La propiedad responseText tiene la respuesta en texto
            }};
            
            solicitud.open("GET", "NuevoHeader.txt", true);
            solicitud.send();
                       
            
           
    });
    $('#btnJson').click(function() {
        $.post('getRegistro.PHP',{},function(data){

            console.log(data);
            $('#idPregunta1').val(data.idPregunta1);
            $('#idPregunta2').val(data.idPregunta2);
            $('#idPregunta3').val(data.idPregunta3);
            $('#idPregunta4').val(data.idPregunta4);
            $('#idPregunta5').val(data.idPregunta5);
            $('#idPregunta6').val(data.idPregunta6);
            $('#idPregunta7').val(data.idPregunta7);
            $('#idPregunta8').val(data.idPregunta8);

        })
    });
});