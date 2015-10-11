set FECHA=%DATE:~-4%%DATE:~-10,2%%DATE:~-7,2%
start c:\M\Ejecucion\CTM\run.bat %FECHA%
start c:\M\Ejecucion\CTM\runBackup.bat %FECHA%
start c:\M\Ejecucion\CTM\runBT.bat %FECHA%



