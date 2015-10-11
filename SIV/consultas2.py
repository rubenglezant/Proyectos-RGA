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

q = "select linea,sum(segundos)/count(segundos) as media from t group by linea;"
result = run_query(q)
for row in result:
		print row[0], str(datetime.timedelta(seconds=row[1]))







