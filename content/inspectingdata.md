---
layout: default
title: Inspecting Data
nav_order: 2
---

## Inspecting Data

## Raster Data

Use gdalinfo to list information about raster data:

Input
{: .label .label-green }
```
$ gdalinfo geotiffs/SF1987.tif
```

Output
{: .label .label-yellow }
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

## Vector Data

Use ogrinfo to list information about vector data:

```ogrinfo shapefiles/ZipCodes.shp```
