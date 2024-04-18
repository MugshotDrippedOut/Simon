index.php:
<!DOCTYPE html>
<html class="no-js">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title></title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="">
</head>
<body>
    <?php
        // !!! POZOR PROMENNE JSOU V UVOZOVKACH !!!
        $mystringX = "10";
        $mystringY = "20.30";
     
        echo '$mystringX=' . $mystringX;
        echo '<BR>';
        echo '$mystringY=' . $mystringY;
        echo '<BR>';
        echo '<BR>';
        echo '$mystringX + $mystringY=';
        echo $mystringX + $mystringY;
        echo '<BR>';
        echo '$mystringX . $mystringY=';
        echo $mystringX . $mystringY;
    ?>
</body> 
</html>  