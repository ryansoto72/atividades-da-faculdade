<?php  include "header.php";  ?>

<h1>Diferenças entreos metodos POST e GET</h1>

<form action="teste.php" method="post">
    <label for="nome_aluno">Nome: </label>
    <input type="text" name="nome_aluno" id="nome_aluno">

    <label for="email_aluno">E-mail: </label>
    <input type="email" name="email_aluno" id="email_aluno">

    <label for="senha_aluno">Senha: </label>
    <input type="password" name="senha_aluno" id="senha_aluno">

    <input type="submit" value="Cadastrar Aluno">
</form>

<?php  include "footer.php"; ?>
