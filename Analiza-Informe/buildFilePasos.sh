#!/bin/bash
FILES=./*.txt
for f in $FILES
do
	python getDataPasos.py $f
done
