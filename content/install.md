---
layout: default
title: Getting Started
nav_order: 1
---

## Getting Started

* [Workshop Data](#workshop-data)
* [Installing GDAL](#installing-gdal)

## Workshop Data

Download the zip file containing the workshop data here

Summary of files included in the workshop data

GeoTIFFs
- SF1987.tif
- SF1938.tif
- houston.tif
- los_angeles.tif

Digital Elevation Model
-gt30w140n40_dem

Shapefiles
-Bus_Stops.shp
-Civic_Art.shp
-sfzipcodes.shp

GeoJSON
- sfbayhighways.geojson

Geodatabase
-SanFranciscoESI.gdb

Python Scripts
- clipTiffs.py
- projectShapes.py
- projectTiffs.py
- shp2geojson.py

Color Configuration File
-colorramp.txt


## Installing GDAL

### On a Mac

Download the GDAL Complete framework appropriate for your operating system here

[http://www.kyngchaos.com/software/frameworks](http://www.kyngchaos.com/software/frameworks)

After the installation is complete, open your terminal and run the following command

 ```
 $ export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH
 ```

Verify that GDAL is installed properly by opening a terminal and running the following command

```
$ gdalinfo --version
```

### On Windows



Use the OSGEO4W Installer to download & install GDAL

[https://trac.osgeo.org/osgeo4w](https://trac.osgeo.org/osgeo4w)

You will use the OSGeo4W Shell to access GDAL. This shell is automatically installed when following the instructions above. 

Verify that the installation was successful by opening the OSGeo4W Shell and running the following command

```
$ gdalinfo --version
```
