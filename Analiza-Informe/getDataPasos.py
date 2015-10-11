# Obtenemos los valores de las validaciones y los pasos para cada barrera
import sys
s = ""
#entrada = "/home/ruben/Proyectos/gmail/Informe-CTM_01-09-2015_02:00.txt"
entrada = sys.argv[1]
with open(entrada) as input_file:
    for i, line in enumerate(input_file):
        if (i==1):
            corte = line.split()
            fecha   = corte[11]
            hora    = corte[12]
            s += fecha+"|"+hora
        if ((i>=291) and (i<=399)):
            corte = line.split()
            ip   = corte[0]
            valida   = corte[1]
            puerta   = corte[2]
            print (s + "|"+ip+ "|"+valida+"|"+puerta)
