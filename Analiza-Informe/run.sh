#!/bin/bash
# Recoge todos los ficheros del directorio indicado que tienen *root*
# Para cada fichero: toma las ultimas lineas y decodifica. 
# La decodificacion da como resultado un nuevo fichero
FILES=/home/ruben/Proyectos/gmail/gmail-backup-20110307/mails/2015/07/*root*
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  tail -260 $f | uudecode
  tail -262 $f | uudecode
  tail -264 $f | uudecode
done

