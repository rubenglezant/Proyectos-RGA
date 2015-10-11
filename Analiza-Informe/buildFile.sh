#!/bin/bash
FILES=./*.txt
for f in $FILES
do
	python getData.py $f
done
