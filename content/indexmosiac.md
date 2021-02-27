---
layout: default
title: Mosaicing
nav_order: 6
---

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

