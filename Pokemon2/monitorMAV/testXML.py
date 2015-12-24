from datetime import datetime
import xml.etree.ElementTree as ET
import sys
import re

try:
    ip = sys.argv[1]
    # ip = '192.168.1.5'
    fname = 'data.xml'
    indice = 0
    tieneError = 0
    estadoLista = []
    with open(fname) as f:
        content = f.readlines()
        xml = content[0]
        words = re.split('<|>',xml)
        estado = 0
        for word in words:
            if (estado == 1):
                estadoLista.append(word)
                indice = indice + 1
                if (indice%2 == 0):
                    if (word != "Operativo"):
                        tieneError = 1
            if ((word == 'component') or (word == 'state') or (word == 'subcomponent')):
                estado = 1
            else:
                estado = 0

    if (tieneError == 1):
        indice = 0
        for valor in estadoLista:
            indice = indice + 1
            if (indice%2 == 0):
                print ("insert into dataMAV values('%s','%s','%s','%s');" %(ip,valorAnterior, valor,str(datetime.now())))
            else:
                valorAnterior = valor
    else:
        print ("insert into dataMAV2 values('%s','STATUS MAV','OK','%s');" %(ip, str(datetime.now())))

except:
    print ("insert into dataMAV2 values('%s','STATUS MAV','NO MONITOR','%s');" %(ip, str(datetime.now())))




