# this script will export all .geojson files in a directory to .shp files in a specified subdirectory 
# ************************************************************************************************************
#!/bin/bash

NEWDIR="geojson/"
mkdir $NEWDIR # creates new subdirectory
for FILE in $(find . -name '*.shp') # cycles through all files in directory (case-sensitive!)
do
	echo "converting file: $FILE..."
	FILENEW=`echo $FILE | sed "s/.shp/.geojson/"` # replaces old filename
	ogr2ogr \
	-f "geojson" \
	$NEWDIR$FILENEW $FILE
done
exit
