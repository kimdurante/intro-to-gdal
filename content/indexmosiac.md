---
layout: default
title: Indexing and Mosaicing
nav_order: 6
---

## Indexing Raster Tiles
<br/>
The `gdaltindex` utility creates a polygon boundary containing features for each input file and a polygon geometry outlining the extent.

Creating an index from one raster file

```
$ gdaltindex SF1938_index.geojson SF1938.tif
```

![Index of one raster file](https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/single_index.png)

From two files

```
$ gdaltindex -t_srs EPSG:4326 maps_index.shp houston.tif los_angeles.tif
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/index_2.png" width="500">

From all rasters in a directory

```
$ gdaltindex doqq/doqq_index.shp doqq/*.tif 
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/index.png" width="500">

## Creating a Mosaic

Mosaicing raster tiles (DOQQs) and creating an overview image using a VRT (Virtual Dataset) file. VRTs are XML documents containing properties such as pixel dimensions and geometries which allow you to merge (mosaic) several raster files without processing overhead

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaic.png" width="500">

Create an input list of files from the _doqq_ directory
```
$ for file in doqq/*.tif*; do echo "$file" >> doqq/doqq.txt; done
```
Use the `gdalbuildvrt` utility with `-input_file_list` 
```
$ gdalbuildvrt -input_file_list doqq/doqq.txt doqq/doqq_merged.vrt 
```

Use `gdalwarp` to reproject to WGS84, set a nodata value, apply JPEG compression, tiling, and YCBCR photometric and output a GeoTIFF
```
$ gdalwarp -t_srs EPSG:4326 -dstnodata 0 -co COMPRESS=JPEG  -co TILED=YES -co PHOTOMETRIC=YCBCR -of gtiff doqq/doqq_merged.vrt doqq/doqq_merged.tif
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaiced.png" width="500">

### Overwriting files

Run the command above again. You will get an error message saying that the file already exists. Use the `-overwrite` flag to overwrite the existing file

```
$ gdalwarp -t_srs EPSG:4326 -dstnodata 0 -co COMPRESS=JPEG  -co TILED=YES -co PHOTOMETRIC=YCBCR -of gtiff -overwrite doqq/doqq_merged.vrt doqq/doqq_merged.tif
```
