<?php include "header.php"; ?>

<header>
    <h1 class='titulo'>Aula 02 - PHP</h1>
    <p>Tabuada de numeros de 1 A 10</p>
    </header>
        <form action="tab.php" method="get">
            <label for="tab">informe o numero que voce quer a tabuada</label>
            <input type="number" name="tab_1" id="tab_1">

            <input type="submit" value="Tabuada">
        </form><br><br>
        <a href="index.php">Voltar...</a>
<?php include "footer.php"; ?>