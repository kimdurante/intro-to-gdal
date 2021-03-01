---
layout: default
title: Clipping Data
nav_order: 6
---

## Clipping Data
<br/>
Clipping is a method of subsetting data. The clipping parameters can be specified as either a bounding box or another data layer.

### Clipping by Bounding Box

Use `gdal_translate` with the `-projwin` flag to specify the coordinates of a clipping extent (ulx uly lrx lry). 

Let's clip _gt30w140n40.dem_ to bounding box (-121.852 39.593 -119.119 37.675)
```
$ gdal_translate -projwin -121.852 39.593 -119.119 37.675 gt30w140n40_dem/gt30w140n40.dem gt30w140n40_clipped.dem
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/dem_clip.png" width="500">


### Clipping by Polygon Boundary

Use `gdalwarp` with the `-cutline` flag to specify the clipping area 

Clip the San Francisco quadrangle to the boundary of zip code 94109. Use the `-crop_to_cutline` flag to crop the extent of the new dataset to the extent of the cutline

```
$ gdalwarp -cutline sf_94109.geojson `-crop_to_cutline SF1987_wgs84.tif SF1987_wgs84_clipped.tif
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/clip_1987.png" width="500">

## Batch Processing

Clip multiple GeoTIFFs to a polygon boundary

```
$ python clipTiffs.py
```

```
import os
import fnmatch

CLIP= "sf_94109.geojson"
INPUT_FOLDER="."
OUTPUT_FOLDER= "clipped"
if not os.path.exists('clipped'):
    os.makedirs('clipped')

def findRasters (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file
        break
for raster in findRasters(INPUT_FOLDER, '*.tif'):
    newFile = raster[:-4]
    inRaster = INPUT_FOLDER + '/' + raster
    outRaster = OUTPUT_FOLDER +'/' + newFile + '_clipped.tif'
    cmd = 'gdalwarp -q -cutline %s -crop_to_cutline -dstalpha -overwrite %s %s' % (CLIP, inRaster, outRaster)
    os.system(cmd)
   ```
<p float="left">
  <img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/clip_1915.png" width="300" />
  <img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/clip_1938.png" width="300" />
</p>

