$(document).ready(function(){
  

    btnInsertar.disabled=true;
    btnModificar.disabled=true;
    btnBorrar.disabled=true;
    Nombre.disabled=true;
    Pregunta1.disabled=true;
    Pregunta2.disabled=true;
    Pregunta3.disabled=true;
    Pregunta4.disabled=true;
    Pregunta5.disabled=true;
    Pregunta6.disabled=true;
    Pregunta7.disabled=true;
    Pregunta8.disabled=true;
    

    // new Promise(function(resolve,reject) {
    // $('#botonAjax').click(function(){
        

    //         var solicitud = new XMLHttpRequest();          //Crear objeto XMLHttpRequest
            
    //         solicitud.onreadystatechange = function() {   // En esta propiedad declaramos la funcion a ejecutar
    //                                                     // cuando cambie el status del objeto XMLHttpRequest
            
    //             if (solicitud.readyState == 4 && solicitud.status == 200) {                 // La respueta esta lista
    //                 document.getElementById("idHeader").innerHTML = solicitud.responseText;  // La propiedad responseText tiene la respuesta en texto
    //         }};
        
    //         solicitud.open("GET", "NuevoHeader.txt", true);
    //         solicitud.send();
    //     }).then(value => document.getElementById("enca").innerHTML=value);        
            
           
    // });
    // $('#btnJson').click(function() {
    //     $.post('getRegistro.PHP',{},function(data){

    //         console.log(data);
    //         refrescar(objeto);
    //         // $('#idPregunta1').val(data.idPregunta1);
    //         // $('#idPregunta2').val(data.idPregunta2);
    //         // $('#idPregunta3').val(data.idPregunta3);
    //         // $('#idPregunta4').val(data.idPregunta4);
    //         // $('#idPregunta5').val(data.idPregunta5);
    //         // $('#idPregunta6').val(data.idPregunta6);
    //         // $('#idPregunta7').val(data.idPregunta7);
    //         // $('#idPregunta8').val(data.idPregunta8);

    //     },'json')
    // });

   /*  $('#btnConsultaBD').click(function() {
        let varid= prompt ("ID a consultar.")

        $('#modal1').modal();
        $('#modal1').on('hidden.bs.modal',function(e)
        {   

            let varid= $('#idconsulta').val();
            $.post('./PHP/conectar.PHP'),{par1:varid},function (data){
                refrescar(dato);
            },'json');

        })
    }); */

        
    
    $('#btnConsultaBD').click(function() {
        /* let varid= prompt ("ID a consultar.") */

        $('#Modal').modal();
        $('#Modal').on('hidden.bs.modal',function(e){

            let varid= $('#idConsulta').val();
            $.post('./PHP/conectar.PHP',{par1:varid},function (data){
                refrescar(data);
            },'json');
            btnInsertar.disabled=false;
            btnModificar.disabled=false;
            btnBorrar.disabled=false;
            Nombre.disabled=false;
            Pregunta1.disabled=false;
            Pregunta2.disabled=false;
            Pregunta3.disabled=false;
            Pregunta4.disabled=false;
            Pregunta5.disabled=false;
            Pregunta6.disabled=false;
            Pregunta7.disabled=false;
            Pregunta8.disabled=false;

        })


        });

        $('#btnBorrar').click(function() {
            /* let varid= prompt ("ID a consultar.") */
            let varid = $('#IDID').val();
    
            $.post('./PHP/Borrar.PHP',{par1:varid});
            swal("Se ha borrado correctamente.");
            IDID.value="";
            var btnInsertar="";
            var btnModificar="";
            btnBorrar.value="";
            Nombre.value="";
            Pregunta1.value="";
            Pregunta2.value="";
            Pregunta3.value="";
            Pregunta4.value="";
            Pregunta5.value="";
            Pregunta6.value="";
            Pregunta7.value="";
            Pregunta8.value="";
    
    
            });

            $('#btnModificar').click(function() {

                let varid = $('#IDID').val();
                let Nombre = $('#Nombre').val();
                let Preg1 = $('#Pregunta1').val();
                let Preg2 = $('#Pregunta2').val();
                let Preg3 = $('#Pregunta3').val();
                let Preg4 = $('#Pregunta4').val();
                let Preg5 = $('#Pregunta5').val();
                let Preg6 = $('#Pregunta6').val();
                let Preg7 = $('#Pregunta7').val();
                let Preg8 = $('#Pregunta8').val();
                    $.post('./PHP/Modificar.PHP',{par1:varid, Nombre1:Nombre, preg1:Preg1, preg2:Preg2, preg3:Preg3, 
                                                 preg4:Preg4, preg5:Preg5, preg6:Preg6 , preg7:Preg7, preg8:Preg8 });
                                                 swal("Se ha modificado correctamente.");

              
        
        
                });
                

                $('#btnInsertar').click(function() {
                    /* let varid= prompt ("ID a consultar.") */
            
                    $('#ModalInsertar').modal();
                    $('#ModalInsertar').on('hidden.bs.modal',function(e){
            
                        
                        let Nombre = $('#Nombre').val();
                        let Preg1 = $('#Pregunta1').val();
                        let Preg2 = $('#Pregunta2').val();
                        let Preg3 = $('#Pregunta3').val();
                        let Preg4 = $('#Pregunta4').val();
                        let Preg5 = $('#Pregunta5').val();
                        let Preg6 = $('#Pregunta6').val();
                        let Preg7 = $('#Pregunta7').val();
                        let Preg8 = $('#Pregunta8').val();
                        $.post('./PHP/Insertar.PHP',{Nombre1:Nombre, preg1:Preg1, preg2:Preg2, preg3:Preg3, 
                            preg4:Preg4, preg5:Preg5, preg6:Preg6 , preg7:Preg7, preg8:Preg8 });
            
                    })
            
            
                    });

                    $('#idInsertar').click(function() {

                        swal("Se ha agregado correctamente.");
                     

                
                
                        });

                        $('#idBorr').click(function() {

                            swal("Se ha borrado correctamente.");
                         
    
                    
                    
                            });

                            $('#idMod').click(function() {

                                swal("Se ha modificado correctamente.");
                             
        
                        
                        
                                });

                
        






    function refrescar(objeto){

            $('#IDID').val(objeto.ID);
            $('#Nombre').val(objeto.Nombre);
            $('#Pregunta1').val(objeto.Pregunta1);
            $('#Pregunta2').val(objeto.Pregunta2);
            $('#Pregunta3').val(objeto.Pregunta3);
            $('#Pregunta4').val(objeto.Pregunta4);
            $('#Pregunta5').val(objeto.Pregunta5);
            $('#Pregunta6').val(objeto.Pregunta6);
            $('#Pregunta7').val(objeto.Pregunta7);
            $('#Pregunta8').val(objeto.Pregunta8);
    }




    
    // $(document).ready(function(){
    //       $('#Guardar').click(function(){
    //         swal({
    //         title: 'SweetAlert',
    //         text: 'Esto es un sweet alert',
    //         html: '<p>MHola<strong>formato</strong>.</p>',
    //         type: 'success',
    //         timer: 3000,
    //         });
    //       });
    // });

});