---
layout: default
title: Clipping Data
nav_order: 6
---

## Clipping Data

Clipping a GeoTIFF to the 94109 zipcode boundary
```
gdalwarp -cutline SF/sf_94109.geojson SF/SF1987_wgs84.tif SF/SF1987_wgs84_clipped.tif
```
Clipping to a boundary, add alpha channel, and crop to extent
```
gdalwarp -cutline SF/sf_94109.geojson -dstalpha -crop_to_cutline SF/SF1987_wgs84.tif SF/SF1987_wgs84_cropped.tif
```

Clipping Data by coordinates
```
gdal_translate -projwin -121.852 39.593 -119.119 37.675 -of USGSDEM DEM/gt30w140n40_dem/gt30w140n40.dem DEM/gt30w140n40_clipped.dem
```

