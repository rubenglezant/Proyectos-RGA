# SIV
Information Passenger

Proceso:
1. Carga.py
Obtiene los valores en JSON y los introduce en una tabla MySQL
NOTA: Obtiene un fichero txt que hay que importar al MySQL según se dice en populate.sql

2. Consultas.py
Recorre todas las lineas y paradas y obtiene el momento de llegada del autobus. Tomando el valor minimo.
Inserta en una tabla los valores obtenidos por parada y linea

3. Consultas2.py
Agrupando por linea realiza la media para todas las paradas. Valor que se puede comparar directamente con la tabla de horarios de
planificacion fija de los autobuses.
El resultado es que la planificacion real y la teorica son similares por tanto el servicio es bueno.


