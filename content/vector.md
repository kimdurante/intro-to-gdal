---
layout: default
title: Vector Data (OGR)
nav_order: 3
---

## Working with Vector Data


* [Formats and Drivers](#ogr-formats-and-drivers)
* [Exploring Data](#exploring-data-ogrinfo)
* [Converting Data](#converting-data-ogr2ogr)
* [Reprojecting Data](#reprojecting-data-ogr2ogr)
* [Batch Processing](#batch-processing)

## OGR Formats and Drivers
<br/>
The list of vector drivers currently supported by OGR can be found here

[https://gdal.org/drivers/vector/index.html](https://gdal.org/drivers/vector/index.html)

See a list of available formats

```$ ogr2ogr --formats```


## Exploring Data (ogrinfo)
<br/>

Use `ogrinfo` to list information about vector data

### Shapefiles
<br/>
Let's explore this polygon shapefile of Zip Codes in San Francisco

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/zipcodes.png" width="500">

```
$ ogrinfo sfzipcodes.shp
```

```
INFO: Open of `sfzipcodes.shp'
      using driver `ESRI Shapefile' successful.
1: sfzipcodes (Polygon)
```

This produces a brief output showing the filename, driver, layer name and geometry type. Use the summary output `-so` flag along with the layer name to view a summary of the data

```
$ ogrinfo -so sfzipcodes.shp sfzipcodes
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
### GeoJSON
<br/>

Let's explore this GeoJSON file of highways in the San Francisco Bay Area

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/highways.png" width="500">

```
$ ogrinfo -so sfbayhighways.geojson sfbayhighways
```

```
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
<br/>

Running `ogrinfo` on a geodatabase outputs a list of feature layers

```
$ ogrinfo SanFranciscoESI.gdb
```

```
INFO: Open of `SanFranciscoESI.gdb'
      using driver `OpenFileGDB' successful.
1: breed_dt (None)
2: soc_dat (None)
3: sources (None)
4: biofile (None)
5: birds_polygon (Multi Polygon)
6: fish_polygon (Multi Polygon)
7: fishl_arc (Multi Line String)
8: habitats_polygon (Multi Polygon)
9: hydro_annotation_geog (Multi Line String)
10: hydro_annotation_hydro (Multi Line String)
11: hydro_annotation_soc (Multi Line String)
12: index_polygon (Multi Polygon)
13: invert_polygon (Multi Polygon)
14: m_mammal_polygon (Multi Polygon)
15: mgt_polygon (Multi Polygon)
16: nests (Point)
17: reptiles_polygon (Multi Polygon)
18: socecon_arc (Multi Line String)
19: socecon_point (Point)
20: t_mammal_polygon (Multi Polygon)
21: ESIP (Multi Polygon)
22: esil (Multi Line String)
23: hydro_polygon (Multi Polygon)
24: hydrol_arc (Multi Line String)

```

To view information about a specific layer

```
$ ogrinfo -so SanFranciscoESI.gdb birds_polygon
```

## Converting Data (ogr2ogr)
<br/>

The `ogr2ogr` utility can be used to convert data between file formats. Use the `-f` flag to specify the output format. If no format is specified, OGR will guess from the file extension provided

### Creating GeoJSON from one layer of a Geodatabase
<br/>

```
$ ogr2ogr -f geojson birds.geojson SanFranciscoESI.gdb birds_polygon
```

### Creating a CSV from a Shapefile
<br/>

```
$ ogr2ogr -f csv CivicArt.csv CivicArt.shp
```

### Creating GeoJSON from a Shapefile
<br/>

```
$ ogr2ogr -f geojson sfzipcodes.geojson sfzipcodes.shp
```
## Reprojecting Data (ogr2ogr)
<br/>

Use ```ogr2ogr``` reproject data. Use the `t_srs` flag to specify the target spatial reference system (projection)

### Reprojecting data from EPSG:26910 to EPSG:4326
<br/>

```
$ ogr2ogr -t_srs EPSG:4326 bus_stops_wgs84.shp Bus_Stops.shp
```

### Reprojecting data and converting to GeoJSON
<br/>

```
$ ogr2ogr -t_srs EPSG:4326 -f geojson bus_stops_wgs84.geojson Bus_Stops.shp
```

## Batch Processing

Performing the same operation on multiple vector files

Convert shapefiles to GeoJSON

```
$ shp2geojson.py
```

```
import os
import fnmatch

INPUT_FOLDER="."
OUTPUT_FOLDER= "geojson"
if not os.path.exists('geojson'):
    os.makedirs('geojson')


def findRasters (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield file
        break

for shapefile in findRasters(INPUT_FOLDER, '*.shp'):
    newFile = shapefile[:-4]
    inShape = INPUT_FOLDER + '/' + shapefile	
    outShape = OUTPUT_FOLDER +'/' + newFile + '.geojson'
    cmd = 'ogr2ogr -f geojson %s %s' % (outShape, inShape)
    os.system(cmd)
```

Convert all shapefiles in a directory to EPSG:4326

```
$ python projectShapes.py
```


```
import os
import fnmatch

INPUT_FOLDER="."
OUTPUT_FOLDER= "wgs84"
if not os.path.exists('wgs84'):
    os.makedirs('wgs84')

def findRasters (path, filter):
    for root, dirs, files in os.walk('.'):
        for file in fnmatch.filter(files, filter):
            yield file
        break


for shapefile in findRasters(INPUT_FOLDER, '*.shp'):
    newFile = shapefile[:-4]
    inShape = INPUT_FOLDER + '/' + shapefile	
    outShape = OUTPUT_FOLDER +'/' + newFile + '_wgs84.shp'
    cmd = 'ogr2ogr -t_srs EPSG:4326 %s %s' % (outShape, inShape)
    os.system(cmd)
```
