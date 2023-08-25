<?php
    include "header.php";
    //receber os dados do formulario via GET
    //declarar uma variavel e recuperar via GET a informacao 

    $numero_um = $_GET['num1'];
    $numero_dois = $_GET['num2'];

    $operacao = $_GET['operacao'];

    if($operacao == "soma"){
        $resultado = $numero_um + $numero_dois;
        echo "O resultado da soma e: ". $resultado . "</h2>";
    }

    elseif($operacao == "subtrair"){
        $resultado = $numero_um - $numero_dois;
        echo "O resultado da subtracao e: ". $resultado;
    }
    elseif($operacao == "multiplicar"){
        $resultado = $numero_um * $numero_dois;
        echo "O resultado da multiplicacao e: ". $resultado;
    }
    elseif($operacao == "dividir"){
        $resultado = $numero_um / $numero_dois;
        echo "O resultado da divisao e: ". $resultado;
    }
include "footer.php";