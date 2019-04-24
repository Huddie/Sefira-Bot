<?php
    if (isset($_POST["submit"])){
        $target = "numbers.txt";
        $target_file = __DIR__.'/'.$target;
        echo $target_file;
        echo $_POST["number"];
        file_put_contents($target_file, "\r\n".$_POST["number"], FILE_APPEND);
        echo "You're all set!";
    }
?>

<!DOCTYPE html>
<html>
<head>
<title>Sefira Bot</title>
<link href=<?php echo __DIR__.'/sefira.css'; ?> rel="stylesheet" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Roboto+Mono:700" rel="stylesheet">
</head>
<body>
<center>
<text class="main_title">Sefira Bot (2019)</text>
<br>
</center>
<center>
<div class="sponsor_div">
<text>Step 1: Whatsapp message "join fifth-sail" (without the quotes) to +14155238886</text><br><br>
<text>Step 2: Enter your Whatsapp number (along with the country code, +1 for USA) below. </text><br>
<text class="sponsor">Example: +12223334444. </text><br><br>

<text>Messages are sent every night @ 8pm</text><br>
</div>
</center>
<center>
<form class="upload-email-wrapper" action=<?php echo $_SERVER['PHP_SELF']; ?> method="post" enctype="multipart/form-data">
<input class="email" type="tel" id="number" name="number" placeholder="Whatsapp Number">
<input class="btn" type="submit" value="Sign Up" name="submit">
</form>
</center>
<center>
<p><text>Made by me with &lt;3 </text></p>
</center>
</body>
</html>
