#!/bin/sh
cd /root/pokemon/monitorMAV
if [ "$1" == "10.40.1.5" ]; then
	cat data.txt >> logMAV5.txt
else
	echo "NO HACE NDA!"
fi
if [ "$1" == "10.40.1.6" ]; then
        cat data.txt >> logMAV6.txt
else
        echo "NO HACE NDA!"
fi
if [ "$1" == "10.40.1.7" ]; then
        cat data.txt >> logMAV7.txt
else
        echo "NO HACE NDA!"
fi

