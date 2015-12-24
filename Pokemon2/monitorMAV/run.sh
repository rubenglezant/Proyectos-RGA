python test.py $1 reqComp.xml > data.txt
/root/pokemon/monitorMAV/logger.sh $1
tail -1 data.txt > data.xml
python testXML.py $1 > insert.txt
php insertBD.php
# cat insert.txt >> insertAll.txt
