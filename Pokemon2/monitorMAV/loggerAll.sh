#!/bin/sh
# cd /root/pokemon/monitorMAV
VALOR=`cat insert.txt|wc -l`
if [ "$VALOR" -ge 3 ]; then
	echo "$1" >> loggerAll.log
	cat data.txt >> loggerAll.log
else
	echo "NO HACE NDA!"
fi

