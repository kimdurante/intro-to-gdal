## Scripts


Batch reproject files to WGS84
```
for i in `find *.tif`; do gdalwarp -t_srs EPSG:4326 -dstalpha $i optimized/$i; done
```

Batch convert from shapefile to geojson
```
for i in `find *.shp`; do ogr2ogr -of geojson $i optimized/$i; done
```
