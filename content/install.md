---
layout: default
title: Getting Started
nav_order: 1
---

## Getting Started

* [Workshop Data](#workshop-data)
* [Installing GDAL](#installing-gdal)

## Workshop Data

Download the zip file of workshop data

[Download Data](../data/us-national-parks.geojson){: .btn .btn-blue }

Summary of files included with this download

* GeoTIFFs
  - SF1915.tif
  - SF1938.tif
  - SF1987.tif
  - houston.tif
  - los_angeles.tif

* Digital Elevation Model
  gt30w140n40_dem

* Shapefiles
  Bus_Stops.shp
  Civic_Art.shp
  sfzipcodes.shp

* GeoJSON
  sfbayhighways.geojson

 * Geodatabase
 SanFranciscoESI.gdb

 * DOQQ
 Digital Orthophoto Quarter Quads (DOQQ)
 
 * Python Scripts
- clipTiffs.py
- projectShapes.py
- projectTiffs.py
- shp2geojson.py

Color Configuration File
- colorramp.txt

</details>

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
