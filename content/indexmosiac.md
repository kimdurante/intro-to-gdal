---
layout: default
title: Mosaicing
nav_order: 6
---

## Indexing Raster Tiles
<br/>
Create a polygon boundary containing attributes for each input file and a polygon geometry outlining the extent

From one raster

```
gdaltindex SF1987_index.geojson SF1987.tif
```

![Index](https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/index_1.png)

From multiple rasters in a directory

```
$ gdaltindex -t_srs EPSG:4326 DOQQ/index.shp DOQQ/*/*.tif 
```

## Creating a Mosaic

Mosaicing raster tiles of all the files and then an overview image

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaic.png" width="500">

Create an input list of DOQQs
```
$ for file in DOQQ/*/*.tif*; do echo "$file" >> DOQQ/doqqs.txt; done
```
VRT (Virtual Dataset) is an XML file, similar to a tile index, that references all the files holding the extent, projection, etc without any processing or translation of the files.
```
$ gdalbuildvrt -input_file_list DOQQ/doqqs.txt DOQQ/doqqs_merged.vrt 
```

Use `gdalwarp` to reproject, set a nodata value, apply JPEG compression and output a GeoTIFF
```
gdalwarp -t_srs EPSG:4326 -dstnodata 0 -co COMPRESS=JPEG  -of gtiff DOQQ/doqqs_merged.vrt DOQQ/doqqs_merged.tif
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaiced.png" width="500">

## Creating a Raster Tile Index

