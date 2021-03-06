from datetime import timedelta

import MySQLdb
import numpy
import datetime
 
DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'root' 
DB_NAME = 'siv' 
 
def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()
    conn.close()
    
    return data

def linea_parada(linea,parada): 
    # Recuperamos los valores para la parada y la linea
    query = "select idautobus,horaactualizacion,distancia from datosSIV where idparada = "+str(parada)+" and idlinea="+str(linea)+" and minutos = 0 order by horaactualizacion;"
    result = run_query(query)
    distanciaAnterior = 100000
    datos = []
    for row in result:
        distanciaActual = row[2]
        if (distanciaAnterior < distanciaActual):
            datos.append([idBus,hora,dist])
            distanciaAnterior = distanciaActual
        else:
            distanciaAnterior = distanciaActual
        idBus = row[0]
        hora = row[1]
        dist = row[2]

    # Calculamos la distancia temporal entre paradas
    aTiempos = []
    for fila in datos:
        aTiempos.append((fila[1]-hora).total_seconds())
        idBus = fila[0]
        hora = fila[1]
        dist = fila[2]

    # Obtenemos la media
    times = aTiempos[2:]
    average_timedelta = sum(times) / len(times)
    # print linea, parada, str(datetime.timedelta(seconds=average_timedelta))
    # print linea, parada, str(average_timedelta)
    q = "insert into t values ("+str(linea)+","+str(parada)+","+str(average_timedelta)+")"
    result = run_query(q)
    print q


q = "select distinct(CONCAT(idlinea,'-',idparada)) from datosSIV order by idlinea;"
result = run_query(q)
for row in result:
	try:
		valoresLP = row[0].split('-')
		linea_parada(valoresLP[0],valoresLP[1])
	except:
		valoresLP = row[0].split('-')
        # print valoresLP[0],valoresLP[1],'Excepcion'






