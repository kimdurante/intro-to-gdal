---
layout: default
title: Inspecting Data
nav_order: 2
---

## Inspecting Data

Exploring raster and vector datasets

## Raster Data

Use _gdalinfo_ to list information about a raster dataset:

```
$ gdalinfo geotiffs/SF1987.tif
```

_gdalinfo_ will output various properties about the data including file format. projection, and band information

```
Driver: GTiff/GeoTIFF
Files: geotiffs/SF1987.tif
Size is 6244, 7581
Coordinate System is:
PROJCRS["NAD83 / UTM zone 10N",
    BASEGEOGCRS["NAD83",
        DATUM["North American Datum 1983",
            ELLIPSOID["GRS 1980",6378137,298.257222101,
                LENGTHUNIT["metre",1]]],
...

Band 1 Block=6244x1 Type=Byte, ColorInterp=Red
Band 2 Block=6244x1 Type=Byte, ColorInterp=Green
Band 3 Block=6244x1 Type=Byte, ColorInterp=Blue
```

Use flags _-norat_ and _-nomd_ to supress output of metadata andraster attributes

```
$ gdalinfo -norat -nomd geotiffs/SF1869.tif
```


## Vector Data

Use _ogrinfo_ to list information about vector data:

```ogrinfo shapefiles/ZipCodes.shp```
