# Consultas de interes
select idautobus,horaactualizacion,distancia from datosSIV
where
idparada = 55 and idlinea=4
and minutos = 0
order by
horaactualizacion;

select distinct(idautobus) from datosSIV
where
idparada = 54 and idlinea=4
and minutos = 0
order by
horaactualizacion;

select distinct(CONCAT(idlinea,'-',idparada))
from datosSIV
order by idlinea;

select count(distinct(idparada))
from datosSIV 
where
idlinea=4;
