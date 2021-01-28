---
layout: default
title: Inspecting Data
nav_order: 2
---

## Inspecting Data

Exploring raster and vector data properties

## Inspecting Raster Data 

Use ```gdalinfo``` to list information about a raster dataset. This will output properties about the data including file format, projection, extent, metadata, and raster band information:

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
        PRIMEM["Greenwich",0,
            ANGLEUNIT["degree",0.0174532925199433]],
        ID["EPSG",4269]],
    CONVERSION["UTM zone 10N",
        METHOD["Transverse Mercator",
            ID["EPSG",9807]],
        PARAMETER["Latitude of natural origin",0,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8801]],
        PARAMETER["Longitude of natural origin",-123,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8802]],
        PARAMETER["Scale factor at natural origin",0.9996,
            SCALEUNIT["unity",1],
            ID["EPSG",8805]],
        PARAMETER["False easting",500000,
            LENGTHUNIT["metre",1],
            ID["EPSG",8806]],
        PARAMETER["False northing",0,
            LENGTHUNIT["metre",1],
            ID["EPSG",8807]]],
                
...

Metadata:
  AGENCY=WESTERN MAPPING CENTER (WMC) oversight agency*
  AREA_OR_POINT=Area
  DATA_FILE_SIZE=142026024 data set size in bytes*
  EAST_LONGITUDE=-122 22 30.000 signed deg min sec SDDD MM SS.SSS*
  IMAGE_SOURCE=COLOR INFRA-RED FILM b&w, cir, natural color, other*
  METADATA_DATE=1998 4 7 date created or changed, yyyy mm dd*
  NATION=US nation code*
  NE_QUAD_CORNER_XY=555013.021 4185195.796 XY coords. of pri. NE quad corner*
  NORTH_LATITUDE=37 48 45.000 signed deg min sec SDDD MM SS.SSS*
  NW_QUAD_CORNER_XY=549511.672 4185160.843 XY coords. of pri. NW quad corner*
  PRODUCER=WESTERN MAPPING CENTER (WMC)
  PRODUCTION_DATE=1998 1 29 yyyy mm dd*
  PRODUCTION_SYSTEM=DV2.6.3 10/9OV2.4 5/95 production system*
  QUADRANGLE_NAME=SAN FRANCISCO NORTH 3.45 or 7.5-min. name*
  QUADRANT=SE quadrant indicator if cell size = 3.75-minutes*
  RASTER_ORDER=LEFT_RIGHT/TOP_BOTTOM video display order*
  RMSE_XY=3.40 doq horiz. accuracy*

...

Image Structure Metadata:
  INTERLEAVE=BAND
Corner Coordinates:
Upper Left  (  549115.000, 4185497.000) (122d26'31.14"W, 37d48'55.98"N)
Lower Left  (  549115.000, 4177916.000) (122d26'32.99"W, 37d44'50.01"N)
Upper Right (  555359.000, 4185497.000) (122d22'15.77"W, 37d48'54.70"N)
Lower Right (  555359.000, 4177916.000) (122d22'17.85"W, 37d44'48.73"N)
Center      (  552237.000, 4181706.500) (122d24'24.44"W, 37d46'52.37"N)
Band 1 Block=6244x1 Type=Byte, ColorInterp=Red
Band 2 Block=6244x1 Type=Byte, ColorInterp=Green
Band 3 Block=6244x1 Type=Byte, ColorInterp=Blue
```

Some datasets may contain a lot of metadata strings. Use flags ```-norat``` and ```-nomd``` to supress output of metadata and raster attributes:

```
$ gdalinfo -norat -nomd geotiffs/SF1869.tif
```

Use the ```-stats``` flag to compute image statistics:

```
$ gdalinfo -stats geotiffs/SF1987.tif
```

## Vector Data


Use ```ogrinfo``` to list information about vector data:

```
$ ogrinfo shapefiles/ZipCodes.shp
```
Output:

```
INFO: Open of `shapefiles/ZipCodes.shp'
      using driver `ESRI Shapefile' successful.
1: ZipCodes (Polygon)
```

Use the summary output flag (```-so```) to display projection, schema, feature count and extent information:

```
$ ogrinfo -so shapefiles/ZipCodes.shp ZipCodes
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

geoJSON

```
ogrinfo -so geojson/sfbayhighways.geojson sfbayhighways
```

Output:

```
INFO: Open of `geojson/sfbayhighways.geojson'
      using driver `GeoJSON' successful.

Layer name: sfbayhighways
Geometry: Multi Line String
Feature Count: 657
Extent: (-123.518512, 36.917289) - (-121.214302, 38.852543)
Layer SRS WKT:
GEOGCRS["WGS 84",
    DATUM["World Geodetic System 1984",
        ELLIPSOID["WGS 84",6378137,298.257223563,
            LENGTHUNIT["metre",1]]],
    PRIMEM["Greenwich",0,
        ANGLEUNIT["degree",0.0174532925199433]],
    CS[ellipsoidal,2],
        AXIS["geodetic latitude (Lat)",north,
            ORDER[1],
            ANGLEUNIT["degree",0.0174532925199433]],
        AXIS["geodetic longitude (Lon)",east,
            ORDER[2],
            ANGLEUNIT["degree",0.0174532925199433]],
    ID["EPSG",4326]]
Data axis to CRS axis mapping: 2,1
id: String (0.0)
fnode_: Integer (0.0)
tnode_: Integer (0.0)
lpoly_: Integer (0.0)
rpoly_: Integer (0.0)
length: Real (0.0)
st_hwy_dis: Integer (0.0)
st_hwy_d_1: Real (0.0)
rte: Integer (0.0)
status: Integer (0.0)
funccl: Integer (0.0)
numlane: String (0.0)
accont: Integer (0.0)
rsys: Integer (0.0)
label: String (0.0)
bbox: RealList (0.0)
```

