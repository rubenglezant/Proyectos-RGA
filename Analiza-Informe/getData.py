import sys
s = ""
with open(sys.argv[1]) as input_file:
    for i, line in enumerate(input_file):
        if (i==1):
            corte = line.split()
            fecha   = corte[11]
            hora    = corte[12]
            s += fecha+"|"+hora
        if ((i>=6) and (i<=13)):
            corte = line.split()
            puertasOK   = corte[2]
            puertasTotal   = corte[4]
            s += "|"+puertasOK+"|"+puertasTotal
        if ((i>=42) and (i<=47)):
            corte = line.split()
            puertasOK   = corte[2]
            puertasTotal   = corte[4]
            s += "|"+puertasOK+"|"+puertasTotal

print s
