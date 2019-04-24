<?php
    if (isset($_POST["submit"])){
        $target_dir = "numbers.txt";
        $target_file = dirname(__DIR__).'/'.$target_file;
        echo ''.$_POST["number"].' >> '.$target_file
    }
?>
