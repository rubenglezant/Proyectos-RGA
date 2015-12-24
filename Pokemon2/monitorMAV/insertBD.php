<?php
$enlace =  mysql_connect('localhost', 'root', 'root');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado satisfactoriamente';

mysql_select_db("monitor", $enlace); 

$handle = @fopen("insert.txt", "r");
$q = "";
if ($handle) {
    while (($buffer = fgets($handle, 4096)) !== false) {
        echo $buffer;
	$result = mysql_query($buffer, $enlace); 
    }
    if (!feof($handle)) {
        echo "Error: unexpected fgets() fail\n";
    }
    fclose($handle);
}

mysql_close($enlace);
?>

