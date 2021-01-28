---
layout: default
title: Converting Data
nav_order: 3
---

## Converting Data

File formats, etc...

### gdal_translate

Use ```gdal_translate``` to convert raster data from one format to another. 

```
gdal_translate -of (of, old, new)
```
Convert a GeoTIFF to a PNG:

```
gdal_translate -of png SF/SF1987.tif SF/SF1987_converted.png
```

See a list of available formats:

```$ gdal_translate --formats```

### ogr2ogr

See a list of available formats:

```$ ogr2ogr --formats``
