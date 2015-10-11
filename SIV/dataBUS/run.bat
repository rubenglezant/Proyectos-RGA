:loop

echo Ooops
set datetimef=%date:~-4%_%date:~3,2%_%date:~0,2%__%time:~0,2%_%time:~3,2%_%time:~6,2%
echo %datetimef%
wget http://datos.gijon.es/doc/transporte/busgijontr.json -O out%datetimef%.json
TIMEOUT 50

goto loop
