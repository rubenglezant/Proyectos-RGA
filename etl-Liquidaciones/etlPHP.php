<?php
$enlace =  mysql_connect('localhost', 'root', 'root');
if (!$enlace) {
    die('No pudo conectarse: ' . mysql_error());
}
echo 'Conectado satisfactoriamente';

mysql_select_db("ctm", $enlace); 
$result = mysql_query("SELECT * FROM datos", $enlace); 
echo "Nombre: ".mysql_result($result, 0, "host")."<br>"; 

echo "---------------------------> MAQUINA: ".$argv[1]."<br>"."<-------------------------------------\n"; 

$mov = simplexml_load_file($argv[1]);
$idMAQ = $mov['maq'];
foreach($mov->serv as $serv)
{
	foreach($serv->pa as $pa)
	{
		foreach($pa->ctt as $ctt)
		{
			$q = 'insert into LIQ values('. 
				$idMAQ.',"'.
				$ctt['fhmov'].'",'.
				$ctt['tit'].','.
				$ctt['operacio'].','.
				$ctt['ns'].','.
				$ctt['nop'].','.
				$ctt['ntd'].',"'.
				$ctt['tim'].'",'.
				$ctt['nviat'].','.
				$ctt['saltst'].','.
				$ctt['saltsc'].','.
				$ctt['saldo'].','.
				$ctt['trbs'].
				");";
			echo $q."\n";
			mysql_query($q, $enlace);
		}
		foreach($pa->di as $di)
		{
			// TODO:
			// echo $di['fhmov'].':'.$di['tim'].':'.$di['nop']."\n";
		}
	}
}

mysql_close($enlace);
?>

