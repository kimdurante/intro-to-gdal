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

From multiple rasters

```
gdaltindex -t_srs EPSG:4326 maps.shp SF1987.tif SF1993.tif california.tif
```

## Creating a Mosaic

Merging several raster files

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaic.png" width="500">

Create an input list of DOQQs
```
$ for file in DOQQ/*/*.tif*; do echo "$file" >> DOQQ/doqqs.txt; done
```
VRT (Virtual Dataset)  is a mosaic of the list of input GDAL-supported rasters. With a mosaic you can merge several raster files. 
```
$ gdalbuildvrt -input_file_list DOQQ/doqqs.txt DOQQ/doqqs_merged.vrt 
```

Use `gdalwarp` to reproject, set a nodata value, apply JPEG compression and output a GeoTIFF
```
gdalwarp -t_srs EPSG:4326 -dstnodata 0 -co COMPRESS=JPEG  -of gtiff DOQQ/doqqs_merged.vrt DOQQ/doqqs_merged.tif
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaiced.png" width="500">

## Creating a Raster Tile Index

```
gdaltindex -t_srs EPSG:4326 DOQQ/index.shp DOQQ/*/*.tif 
```
