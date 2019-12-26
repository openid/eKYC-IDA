#!/bin/bash

FILENAME=`echo $1 | cut -f1 -d'.'`

mmark -2 $FILENAME.md | sed 's/<?rfc sortrefs="yes"?>/<?rfc sortrefs="yes"?><?rfc private="Draft"?>/' > $FILENAME-1_0.xml

`which xml2rfc` --legacy  --html $FILENAME-1_0.xml 

`which xml2rfc` --legacy --text $FILENAME-1_0.xml
