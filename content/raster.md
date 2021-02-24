---
layout: default
title: Raster Data
nav_order: 2
---

## Using GDAL with Raster Data

GDAL supports a wide-range of raster formats through the use of drivers which contain specifications and capabilities for reading and writing data. 

The list of raster drivers currently supported by GDAL can be found here: [https://gdal.org/drivers/raster/index.html](https://gdal.org/drivers/raster/index.html).

## Inspecting Data

Use ```gdalinfo``` to list information about a raster dataset. This will output properties about the data including file format, projection, extent, metadata, and raster band information.

Run the following command:

```
$ gdalinfo geotiffs/SF1987.tif
```

You should see a large block of output text, beginning with:

```
Driver: GTiff/GeoTIFF
```

This indicates that the file is a GeoTIFF, which is a special type of TIFF that stores the information necessary to place each pixel in the image on the surface of the Earth. The next lines of text display the filename, and the size (in pixels) of the image.

```
Files: geotiffs/SF1987.tif
Size is 6244, 7581
```

Below that, you will see some very important information which contains the projection of the data. This is the information that places this image correctly over the city of San Francisco, and specifies the location of each pixel.

```
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
```
The output also contains some generic metadata for the file:
```
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
  SECONDARY_HORIZONTAL_DATUM=NAD27 secondary horizontal datum*
  SECONDARY_NE_QUAD_XY=555014.390 4184990.576 XY coords. - sec. NE quad cor.*
  SECONDARY_NW_QUAD_XY=549512.904 4184955.623 XY coords. - sec. NW quad cor.*
  SECONDARY_SE_QUAD_XY=555060.733 4178056.378 XY coords. - sec. SE quad cor.*
  SECONDARY_SW_QUAD_XY=549554.612 4178021.444 XY coords. - sec. SW quad cor.*
  SECONDARY_XY_ORIGIN=549211.000 4185301.000 coord upper left pixel sec datum*
  SE_QUAD_CORNER_XY=555059.365 4178261.445 XY coords. of pri. SE quad corner*
  SOURCE_DEM_DATE=1998 1 29 source dem date yyyy mm dd*
  SOURCE_IMAGE_DATE=1987 6 22 source image date as yyyy mm dd*
  SOURCE_IMAGE_ID=NAPP 511 125 source image id*
  SOUTH_LATITUDE=37 45 0.000 signed deg min sec SDDD MM SS.SSS*
  STANDARD_VERSION=1996 12 version of DOQ standard*
  STATE=CA state fip code*
  SW_QUAD_CORNER_XY=549553.381 4178226.512 XY coords. of pri. SW quad corner*
  WEST_LONGITUDE=-122 26 15.000 signed deg min sec SDDD MM SS.SSS*

```

The last block of output shows the corner points of the image in two different units (meters and minutes, degrees, seconds), as well as some information about each band (also called a channel) in the image. Each channel is byte (8-bit) format, there are three bands (red, green, and blue, respectively). The minimum and maximum values in each band are also displayed.

```
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

Use flags ```-norat``` and ```-nomd``` to supress output of metadata and raster attributes:

```
$ gdalinfo -norat -nomd geotiffs/SF1987.tif
```

Let's look at the information for one of the digital elevation models:

```
$ gdalinfo dem/gt30w140n40_dem/gt30w140n40.dem


Driver: EHdr/ESRI .hdr Labelled
Files: gt30w140n40_dem/gt30w140n40.dem
       gt30w140n40_dem/gt30w140n40.dem.aux.xml
       gt30w140n40_dem/gt30w140n40.hdr
       gt30w140n40_dem/gt30w140n40.stx
       gt30w140n40_dem/gt30w140n40.prj
Size is 4800, 6000
Coordinate System is:
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

...

Band 1 Block=4800x1 Type=Int16, ColorInterp=Undefined
  Min=-66.000 Max=4280.000 
  Minimum=-66.000, Maximum=4280.000, Mean=1329.977, StdDev=744.157
  NoData Value=-9999

```









## Vector Data


Use ```ogrinfo``` to list information about vector data:

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