<?php


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
    $consultaSql = "insert into preguntas (Nombre, pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8)
    values ('$Nombre','$pregu1','$pregu2','$pregu3','$pregu4','$pregu5','$pregu6','$pregu7','$pregu8')";
    $consulta = $con -> prepare($consultaSql);
    $consulta -> execute();
    $consulta->closeCursor();
} catch(PDOException $e){
    echo "Error GUSTAVO";
    echo $e->getMessage();
}

?>