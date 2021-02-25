---
layout: default
title: Vector Data (OGR)
nav_order: 3
---

## Working with Vector Data

[Drivers](#ogr-drivers)

[Exploring Data](#exploring-data-ogrinfo)

[Converting Data](#converting-data-ogr2ogr)

[Reprojecting Data](#reprojecting-data-ogr2ogr)

## OGR Drivers

See a list of available formats

```$ ogr2ogr --formats```


## Exploring Data (ogrinfo)

Use ```ogrinfo``` to list information about vector data:

## Converting Data (ogr2ogr)


### Shapefiles
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

### GeoJSON

```
$ ogrinfo -so geojson/sfbayhighways.geojson sfbayhighways
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

### Geodatabases

```
$ ogrinfo geodatabases/SanFranciscoESI.gdb -so birds_polygon
```

Output:

```
INFO: Open of `geodatabases/SanFranciscoESI.gdb'
      using driver `OpenFileGDB' successful.

Layer name: birds_polygon
Geometry: Multi Polygon
Feature Count: 987
Extent: (-122.591975, 37.381318) - (-121.780042, 38.246878)
Layer SRS WKT:
GEOGCRS["NAD83",
    DATUM["North American Datum 1983",
        ELLIPSOID["GRS 1980",6378137,298.257222101,
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
    USAGE[
        SCOPE["Geodesy."],
        AREA["North America - onshore and offshore: Canada - Alberta; British Columbia; Manitoba; New Brunswick; Newfoundland and Labrador; Northwest Territories; Nova Scotia; Nunavut; Ontario; Prince Edward Island; Quebec; Saskatchewan; Yukon. Puerto Rico. United States (USA) - Alabama; Alaska; Arizona; Arkansas; California; Colorado; Connecticut; Delaware; Florida; Georgia; Hawaii; Idaho; Illinois; Indiana; Iowa; Kansas; Kentucky; Louisiana; Maine; Maryland; Massachusetts; Michigan; Minnesota; Mississippi; Missouri; Montana; Nebraska; Nevada; New Hampshire; New Jersey; New Mexico; New York; North Carolina; North Dakota; Ohio; Oklahoma; Oregon; Pennsylvania; Rhode Island; South Carolina; South Dakota; Tennessee; Texas; Utah; Vermont; Virginia; Washington; West Virginia; Wisconsin; Wyoming. US Virgin Islands.  British Virgin Islands."],
        BBOX[14.92,167.65,86.46,-47.74]],
    ID["EPSG",4269]]
Data axis to CRS axis mapping: 2,1
FID Column = OBJECTID
Geometry Column = Shape
ID: Real (0.0)
RARNUM: Integer (0.0)
Shape_Length: Real (0.0)
Shape_Area: Real (0.0)

```
