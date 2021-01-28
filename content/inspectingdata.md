---
layout: default
title: Inspecting Data
nav_order: 2
---

## Inspecting Data

Exploring raster and vector data properties

## Raster Data 

Use _gdalinfo_ to list information about a raster dataset. This will output properties about the data including file format, coordinates, projection, and raster band information:

```
$ gdalinfo geotiffs/SF1987.tif
```

Output:

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

Use flags _-norat_ and _-nomd_ to supress output of metadata and raster attributes

```
$ gdalinfo -norat -nomd geotiffs/SF1869.tif
```


## Vector Data

Use _ogrinfo_ to list information about vector data.

```$ ogrinfo shapefiles/ZipCodes.shp```

```
INFO: Open of `shapefiles/ZipCodes.shp'
      using driver `ESRI Shapefile' successful.
1: ZipCodes (Polygon)
```

Use the summary output flag to display projection, schema, feature count and extent information:

```
$ ogrinfo -so shapefiles/ZipCodes.shp -so ZipCodes
```

Output:

```
Layer name: ZipCodes
Metadata:
  DBF_DATE_LAST_UPDATE=1920-02-14
Geometry: Polygon
Feature Count: 187
Extent: (-122.804417, 37.252190) - (-121.403842, 38.864245)
Layer SRS WKT:
GEOGCRS["WGS84(DD)",
    DATUM["WGS84",
        ELLIPSOID["WGS84",6378137,298.257223563,
            LENGTHUNIT["metre",1,
                ID["EPSG",9001]]]],
    PRIMEM["Greenwich",0,
        ANGLEUNIT["degree",0.0174532925199433]],
    CS[ellipsoidal,2],
        AXIS["geodetic longitude",east,
            ORDER[1],
            ANGLEUNIT["degree",0.0174532925199433]],
        AXIS["geodetic latitude",north,
            ORDER[2],
            ANGLEUNIT["degree",0.0174532925199433]]]
Data axis to CRS axis mapping: 1,2
area: Real (33.31)
length: Real (33.31)
po_name: String (254.0)
state: String (254.0)
zip: String (254.0)
```
