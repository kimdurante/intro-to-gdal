---
layout: default
title: Vector Data (OGR)
nav_order: 3
---

## Working with Vector Data

[Formats and Drivers](#ogr-formats-and-drivers)

[Exploring Data](#exploring-data-ogrinfo)

[Converting Data](#converting-data-ogr2ogr)

[Reprojecting Data](#reprojecting-data-ogr2ogr)

## OGR Formats and Drivers

The list of vector drivers currently supported by OGR can be found here

[https://gdal.org/drivers/vector/index.html](https://gdal.org/drivers/vector/index.html)

See a list of available formats

```$ ogr2ogr --formats```


## Exploring Data (ogrinfo)

Use ```ogrinfo``` to list information about vector data

Let's look at a polygon shapefile of Zip Codes in San Francisco

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/zipcodes.png" width="500">

```
$ ogrinfo sfzipcodes.shp
```

```
INFO: Open of `sfzipcodes.shp'
      using driver `ESRI Shapefile' successful.
1: sfzipcodes (Polygon)
```

Use the summary output flag (```-so```) to display projection, schema, feature count and extent information:

```
$ ogrinfo -so zipcodes.shp sfzipcodes
```

```
Layer name: sfzipcodes
Metadata:
  DBF_DATE_LAST_UPDATE=2005-07-08
Geometry: Polygon
Feature Count: 25
Extent: (5979385.499980, 2085840.500090) - (6024664.500080, 2123808.749990)
Layer SRS WKT:
PROJCRS["NAD83 / California zone 3 (ftUS)",
    BASEGEOGCRS["NAD83",
        DATUM["North American Datum 1983",
            ELLIPSOID["GRS 1980",6378137,298.257222101,
                LENGTHUNIT["metre",1]]],
        PRIMEM["Greenwich",0,
            ANGLEUNIT["degree",0.0174532925199433]],
        ID["EPSG",4269]],
    CONVERSION["SPCS83 California zone 3 (US Survey feet)",
        METHOD["Lambert Conic Conformal (2SP)",
            ID["EPSG",9802]],
        PARAMETER["Latitude of false origin",36.5,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8821]],
        PARAMETER["Longitude of false origin",-120.5,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8822]],
        PARAMETER["Latitude of 1st standard parallel",38.4333333333333,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8823]],
        PARAMETER["Latitude of 2nd standard parallel",37.0666666666667,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8824]],
        PARAMETER["Easting at false origin",6561666.667,
            LENGTHUNIT["US survey foot",0.304800609601219],
            ID["EPSG",8826]],
        PARAMETER["Northing at false origin",1640416.667,
            LENGTHUNIT["US survey foot",0.304800609601219],
            ID["EPSG",8827]]],
    CS[Cartesian,2],
        AXIS["easting (X)",east,
            ORDER[1],
            LENGTHUNIT["US survey foot",0.304800609601219]],
        AXIS["northing (Y)",north,
            ORDER[2],
            LENGTHUNIT["US survey foot",0.304800609601219]],
    USAGE[
        SCOPE["Engineering survey, topographic mapping."],
        AREA["United States (USA) - California - counties Alameda; Calaveras; Contra Costa; Madera; Marin; Mariposa; Merced; Mono; San Francisco; San Joaquin; San Mateo; Santa Clara; Santa Cruz; Stanislaus; Tuolumne."],
        BBOX[36.73,-123.02,38.71,-117.83]],
    ID["EPSG",2227]]
Data axis to CRS axis mapping: 1,2
OBJECTID: Integer64 (11.0)
ZIP_CODE: Integer64 (11.0)
ID: Integer64 (11.0)
```

Let's explore a GeoJSON file

```
$ ogrinfo -so geojson/sfbayhighways.geojson sfbayhighways
```

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

Geodatabases

```
$ ogrinfo geodatabases/SanFranciscoESI.gdb -so birds_polygon
```

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
## Converting Data (ogr2ogr)

Convert a shapefile to a csv

```
$ ogr2ogr -f csv SF/CivicArt.csv SF/CivicArt.shp
```

Convert a shapefile to GeoJSON

```
$ ogr2ogr -f geojson SF/ZipCodes.geojson SF/ZipCodes.shp

```

## Reprojecting Data (ogr2ogr)

Use ```ogr2ogr``` with the target SRS flag (```t_srs```) to reproject vector data. 

```ogr2ogr -t_srs (srs, new, old)```

```ogr2ogr -t_srs EPSG:4326 SF/bus_stops_wgs84.shp SF/Bus_Stops.shp```
