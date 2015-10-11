import json
from pprint import pprint

def obtenerDatosJSON(fichero):
	# Lectura del JSON
	with open(fichero) as data_file:    
	    data = json.load(data_file)

	# Obtencion de los datos para una parada
	for i in data['llegadas']['llegada']:
		valor = ''
		valor =  valor + str(i['idlinea']) + ','
		valor =  valor + str(i['idtrayecto']) + ','
		valor =  valor + i['idautobus'] + ','
		valor =  valor + '0' + ','
		valor =  valor + '0' + ','
		valor =  valor + i['fechaactualizacion'][:11] + i['horaactualizacion'] + ','
		valor =  valor + i['fechaactualizacion'] + ','
		valor =  valor + str(i['idparada']) + ','
		valor =  valor + str(i['minutos']) + ','
		valor =  valor + str(i['distancia']) + ','
		valor =  valor + i['matricula'] + ','
		valor =  valor + i['modelo'] + ','
		valor =  valor + '0' + ','
		valor =  valor + '0'
		print valor

# Obtenemos los valores de cada fichero
import glob
lista = glob.glob("dataBUS/*.json")
for i in lista:
	obtenerDatosJSON(i)



