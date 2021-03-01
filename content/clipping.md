---
layout: default
title: Clipping Data
nav_order: 6
---

## Clipping Data
<br/>
Clipping is a method of subsetting data. The clipping parameters can be specified as a bounding box or another data layer.

### Clipping by Bounding Box

In the gdal_translate utility, the `-projwin` flag is used to specify the clipping extent (ulx uly lrx lry). 

Clip _gt30w140n40.dem_ to bounding box (-121.852 39.593 -119.119 37.675)
```
$ gdal_translate -projwin -121.852 39.593 -119.119 37.675 gt30w140n40_dem/gt30w140n40.dem gt30w140n40_clipped.dem
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/dem_clip.png" width="500">


### Clipping by Vector

Clip _SF1987_wgs84.tif_ to the 94109 boundary by using `-cutline`

```
$ gdalwarp -cutline sf_94109.geojson SF1987_wgs84.tif SF1987_wgs84_clipped.tif
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/94109_alpha_c.png" width="500">

### Batch Processing

```
import os
import fnmatch

CLIP= "sf_94109.geojson"
INPUT_FOLDER="SFMAPS"
OUTPUT_FOLDER= "wgs84"

def findRasters (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file

for raster in findRasters(INPUT_FOLDER, '*.tif'):
    inRaster = INPUT_FOLDER + '/' + raster
    outRaster = OUTPUT_FOLDER + '/clip_' + raster
    cmd = 'gdalwarp -q -cutline %s -crop_to_cutline -dstalpha %s %s' % (CLIP, inRaster, outRaster)
    os.system(cmd)
   ```
