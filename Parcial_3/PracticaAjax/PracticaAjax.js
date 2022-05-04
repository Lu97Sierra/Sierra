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
});