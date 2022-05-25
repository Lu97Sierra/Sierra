<?php
include "conectar.php";

try{
    $query=$con -> prepare("select * from preguntas");
    $query -> execute();

    while ($row = $query -> fetch()) {
        echo    $row ['Pregunta0'].'-'.
                $row ['Pregunta1'].'-'.
                $row ['Pregunta2'].'-'.
                $row ['Pregunta3'].'-'.
                $row ['Pregunta4'].'-'.
                $row ['Pregunta5'].'-'.
                $row ['Pregunta6'].'-'.
                $row ['Pregunta7'].'-'.
                $row ['Pregunta8'].'<br>';
    }
    $query -> closeCursor();
} catch(PDOException $e) {
    echo "Error de consulta de base de datos";
    echo $e -> getMessage();
}
?>