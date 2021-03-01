---
layout: default
title: Mosaicing
nav_order: 6
---

## Indexing Raster Tiles
<br/>
The `gdaltindex` utility creates a polygon boundary containing features for each input file and a polygon geometry outlining the extent.

To create an index from one raster file

```
$ gdaltindex SF1987_index.geojson SF1987.tif
```

![Index of one raster file](https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/single_index.png)

To index multiple rasters by filename

```
$ gdaltindex -t_srs EPSG:4326 houston.tif los_angeles.tif
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/index_2.png" width="500">

To index multiple rasters in a directory

```
$ gdaltindex -t_srs DOQQ/index.shp DOQQ/*/*.tif 
```

![Index of multiple raster files in a directory](https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/index.png)
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
$ gdalwarp -t_srs EPSG:4326 -dstnodata 0 -co COMPRESS=JPEG  -of gtiff DOQQ/doqqs_merged.vrt DOQQ/doqqs_merged.tif
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaiced.png" width="500">
