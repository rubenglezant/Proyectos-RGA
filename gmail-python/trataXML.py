__author__ = 'ruben'

from os import listdir

s = ""
for cosa in listdir("."):
    if (cosa.find(".xml")>0):
        f=open(cosa,"r")
        for line in f:
            if (line.find("PAR")>=0):
                s = s + cosa + " - PAR - " + "\n"
                print (s)
        f.close()

if (s != ""):
    hayPMR = 1;
else:
    hayPMR = 0;

f=open("datosEnviar.txt","w")
f.write(s)
f.close()

f=open("sendMail.sh","w")
if (hayPMR>0):
    f.write("./enviaMail.sh\n")
    print ("SI PAR " + s)
else:
    f.write("echo Hola\n")
f.close()
