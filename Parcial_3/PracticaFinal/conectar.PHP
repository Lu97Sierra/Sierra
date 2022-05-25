<?php

/* $registro['idPregunta0'] = 'Luis Gustavo';
$registro['idPregunta1'] ='Un medio ambiente limpio es fuente de satisfacción';
$registro['idPregunta2'] ='Cuidar el medio ambiente es cuidarnos a nosotros mismos, uno no está separado del otro';
$registro['idPregunta3'] ='Ahorrar recursos con los que tengas contacto diario';
$registro['idPregunta4'] ='Reciclaje de papel, Reciclaje de vidrio';
$registro['idPregunta5'] ='Reducir los envases o productos de usar y tirar';
$registro['idPregunta6'] ='Compra solo lo que necesitas';
$registro['idPregunta7'] ='Las pérdidas de alimentos conllevan el desperdicio de recursos utilizados en la producción como tierra, agua, energía e insumos';
$registro['idPregunta8'] ='Los voluntarios se encargan de recoger todos los residuos que puedan de las playas y, de ser posible, identificarlos para que estos sean reciclados';

$registroJson = json_encode($registro);
echo $registroJson */

$hostname='localhost';
$database='l18100233';
$username='root';
$password='1234';
$id = '1';
try{
    $con= new PDO("mysql:host=$hostname;dbname=$database",$username,$password);
} catch (PDOException $e){
    echo "Error de conexion de base de datos";
    echo $e -> getMessage();
    exit();
}

$con -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

try {
    $consultaSql = "select Nombre from preguntas where ID =".$id;
    $consulta = $con -> prepare($consultaSql);
    $consulta -> execute();
    $resultado = $consulta->fetch(PDO::FETCH_ASSOC);
    $consulta->closeCursor();
} catch(PDOException $e){
    echo "Error GUSTAVO";
    echo $e->getMessage();
}
echo json_encode($resultado);

?>