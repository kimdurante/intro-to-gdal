#!/bin/bash
# reprojects a directory of .shp files to WGS84

TSRS=$1 # data source's current CRS (may improve accuracy of OGR if specified)
NEWDIR="wgs84/"
mkdir $NEWDIR # creates new subdirectory
for FILE in $(find . -name '*.shp')
do
 echo "Transforming $FILE file..."
  FILENEW=`echo $FILE | sed "s/.shp/_4326.shp/"`
 ogr2ogr \
 -f "ESRI Shapefile" -t_srs "EPSG:4326" \
 $NEWDIR$FILENEW $FILE

done
