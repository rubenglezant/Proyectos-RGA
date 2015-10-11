dir="./BT"
for file in $dir/*
do
    php etlPHP.php $file
done
