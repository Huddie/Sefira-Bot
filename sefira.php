<?php
    if (isset($_POST["submit"])){
        $target = "numbers.txt";
        $target_file = __DIR__.'/'.$target;
        file_put_contents($target_file, $_POST["number"], FILE_APPEND);
    }
?>
