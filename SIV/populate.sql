create database siv;

use database siv;

Create table datosSIV 
(
      idlinea integer(5),
      idtrayecto integer(5),
      idautobus integer(5),
      utmx integer(10),
      utmy integer(10),
      horaactualizacion datetime,
      fechaactualizacion datetime,
      idparada integer(5),
      minutos integer(5),
      distancia integer(15),
      matricula varchar(255),
      modelo varchar(255),
      ordenparada integer(5),
      idsiguienteparada integer(5)
);

select * from datosSIV;

delete from datosSIV;

LOAD DATA INFILE 'data.txt' INTO TABLE datosSIV
  FIELDS TERMINATED BY ',';

# cp /home/ruben/Proyectos/SIV/SIV/data.txt /var/lib/mysql/siv/data.txt  

grant file on *.* to root@localhost identified by 'root';
grant file on *.* to root@rubenpc identified by 'root';
GRANT FILE ON *.* to root@localhost;
  
  
# Consultas de interes
select * from dataSIV
where
idparada = 54 and idlinea=4;


# Creacion de una tabla temporal
CREATE TABLE t (linea DECIMAL, parada DECIMAL, segundos FLOAT);

insert into t values (1,16,692.01);

select * from t;

delete from t;

drop table t;

select linea,sum(segundos)/count(segundos) as media from t group by linea;


