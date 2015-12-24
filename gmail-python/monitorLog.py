__author__ = 'ruben'

import time
import subprocess
import select

def processLine(linea):
    if (linea.find('Kontni') > 0):
        print (linea)

f = subprocess.Popen(['tail','-F','/home/ruben/test.txt'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(1):
        processLine (str(f.stdout.readline()))
    time.sleep(0.001)
