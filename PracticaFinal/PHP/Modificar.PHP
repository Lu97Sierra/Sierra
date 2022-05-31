<?php

$id= $_POST['par1'];
$Nombre= $_POST['Nombre1'];
$pregu1= $_POST['preg1'];
$pregu2= $_POST['preg2'];
$pregu3= $_POST['preg3'];
$pregu4= $_POST['preg4'];
$pregu5= $_POST['preg5'];
$pregu6= $_POST['preg6'];
$pregu7= $_POST['preg7'];
$pregu8= $_POST['preg8'];


$hostname='localhost';
$database='l18100233';
$username='root';
$password='1234';

try{    
    $con= new PDO("mysql:host=$hostname;dbname=$database",$username,$password);
} catch (PDOException $e){
    echo "Error de conexion de base de datos";
    echo $e -> getMessage();
    exit();
}


try {
    $consultaSql = "update preguntas set Nombre='$Nombre', pregunta1='$pregu1', pregunta2='$pregu2',
                                                           pregunta3='$pregu3', pregunta4='$pregu4',
                                                           pregunta5='$pregu5', pregunta6='$pregu6',
                                                           pregunta7='$pregu7', pregunta8='$pregu8' where ID ='$id'";
    $consulta = $con -> prepare($consultaSql);
    $consulta -> execute();
    $consulta->closeCursor();
} catch(PDOException $e){
    echo "Error GUSTAVO";
    echo $e->getMessage();
}

?>