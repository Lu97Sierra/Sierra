<?php

$registro['idCliente'] ='123';
$registro['nomCliente'] ='Gerardo';
$registro['hora'] ='12:00:00';
$registro['dirCliente'] ='Guerrero 2001';
$registro['telCliente'] ='867 163 123';
$registro['ciudad'] ='Nuevo Laredo';
$registro['estado'] ='Tamaulipas';
$registro['pais'] ='Mexico';

$registroJson = json_encode($registro);
echo $registroJson
?>