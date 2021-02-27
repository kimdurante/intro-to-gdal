---
layout: default
title: Clipping Data
nav_order: 6
---

## Clipping Data

Clipping a GeoTIFF to the 94109 zipcode boundary
```
$ gdalwarp -cutline sf_94109.geojson SF1987_wgs84.tif SF1987_wgs84_clipped.tif
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/94109_crop.png" width="500">

IMAGE

Clipping file to a boundary, adding alpha channel, and cropping to extent
```
$ gdalwarp -cutline sf_94109.geojson -dstalpha -crop_to_cutline SF1987_wgs84.tif SF1987_wgs84_a.tif
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/94109_crop_alpha.png" width="500">
IMAGE

Clipping Data by coordinates
```
gdal_translate -projwin -121.852 39.593 -119.119 37.675 -of USGSDEM DEM/gt30w140n40_dem/gt30w140n40.dem DEM/gt30w140n40_clipped.dem
```

