
<?php include "header.php"; ?>
    <header>
    <h1 class='titulo'>Aula 02 - PHP</h1>
    <p>Criando uma calculadora com o formulario</p>
    </header>
        <form action="calcular.php" method="get">
            <label for="num1">informe o primeiro numero</label>
            <input type="number" name="num1" id="num1">

            <label for="num2">Informe o segundo numero</label>
            <input type="number" name="num2" id="num2">

            <label for="operacao">Informe a operacao matematica</label>
            
            
            <select name="operacao" id="operacao">
                <option value="soma">somar</option>
                <option value="subtrair">subtrair</option>
                <option value="multiplicar">multiplicar</option>
                <option value="dividir">dividir</option>
            </select>
            <input type="submit" value="calcular">
        </form><br><br>
        <a href="index.php">Voltar...</a>
<?php include "footer.php"; ?>