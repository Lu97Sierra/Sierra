<?php


$paridCte= $_POST['par1'];

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
    $consultaSql = "delete from preguntas where ID =".$paridCte;
    $consulta = $con -> prepare($consultaSql);
    $consulta -> execute();
    $consulta->closeCursor();
} catch(PDOException $e){
    echo "Error GUSTAVO";
    echo $e->getMessage();
}

?>