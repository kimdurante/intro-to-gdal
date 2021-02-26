---
layout: default
title: Raster Data (GDAL)
nav_order: 2
---

## Working with Raster Data

<br/>

* [Formats and Drivers](#gdal-formats-and-drivers)
* [Exploring Data](#exploring-data-gdalinfo)
* [Converting Data](#converting-data-gdal_translate)
* [Warping Data](#warping-data-gdalwarp)

## GDAL Formats and Drivers

GDAL provides support for a wide-range of raster file formats through the use of drivers which contain specifications and capabilities for handling data

To view a list of available raster formats, run the following command

```
gdal_translate --formats
```
The list of raster drivers currently supported by GDAL can be found here

[https://gdal.org/drivers/raster/index.html](https://gdal.org/drivers/raster/index.html).


## Exploring Data (gdalinfo)

Use ```gdalinfo``` to list information about raster data. This will output data properties including file format, projection, extent, metadata, and raster band information

Run the following command

```
$ gdalinfo SF/SF1987.tif
```

You should see a large block of output text, beginning with

```
Driver: GTiff/GeoTIFF
```

This indicates that the file is a GeoTIFF, which is a special type of TIFF that stores the information necessary to place each pixel in the image on the surface of the Earth. The next lines of text display the filename, and the image size (in pixels)

```
Files: SF/SF1987.tif
Size is 6244, 7581
```

Below that is the projection infomration. This is the information that places this image correctly over the city of San Francisco, and specifies the location of each pixel.

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
There is also some generic metadata for the file
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

The last block of output shows the corner points of the image in two different units (meters and minutes, degrees, seconds), as well as some information about each band (a.k.a. channel). Each channel is byte (8-bit) format, there are three bands (red, green, and blue, respectively).

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

Use the```-nomd``` flag to supress output of metadata

```
$ gdalinfo -norat -nomd SF/SF1987.tif
```

Let's look at the information for one of the digital elevation models:

```
$ gdalinfo DEM/gt30w140n40_dem/gt30w140n40.dem

```

```
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
## Converting Data (gdal_translate)

The gdal_translate utility can be used to convert raster data between different formats, as well as perform operationssuch as resampling, rescaling, and adding NoData values.

The ```-of``` flag is used to specify the output format. If not specified, the format is guessed from the extension. Use the short format name

Converting a GeoTIFF to a PNG:

```
$ gdal_translate -of png SF/SF1987.tif SF/SF1987_converted.png
```

Use the creation options flag```-co``` along with ```COMPRESS=JPEG``` output a JPEG compressed GeoTIFF
```
$ gdal_translate -co COMPRESS=JPEG SF/SF1993.tif SF/SF1993_compressed.tif
```
## Warping Data (gdalwarp)

gdalwarp is a reprojection warping, and image mosaicing utility. It can reproject to any supported projection, and can also apply ground control points stored with the image if the image is “raw” with control information.

```
$ gdalwarp -t_srs EPSG:4326 SF/SF1987.tif SF/SF1987_wgs84.tif
```

## Tile Indexing

Create a shapefile containing a record for each input raster file and a polygon geometry outlining the extent

From one raster

```
gdaltindex SF/index_sf1938.shp SF/SF1938.tif
```

![Index](https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/index_1.png)

From multiple rasters

```
gdaltindex -t_srs EPSG:4326 SF/maps.shp SF/SF1987.tif SF/SF1993.tif SF/california.tif
```
