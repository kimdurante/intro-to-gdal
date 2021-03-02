---
layout: default
title: Getting Started
nav_order: 1
---

## Getting Started

* [Installing GDAL](#installing-gdal)
* [Workshop Data](#workshop-data)

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


## Workshop Data

Download the zip file of workshop data

[Download Data](https://drive.google.com/file/d/0B0WoZmauQebXWXlJVllKNEZWd1U/view?usp=sharing)

Unzip the folder to your machine. Open a terminal and navigate into the 'data' directory

Summary of files included with this download

* Raster Data
  - SF1915.tif - georeferenced map of San Francisco (1915)
  - SF1938.tif - composite image of a set of 164 large format black and white vertical aerial photographs of San Francisco (1938)
  - SF1987.tif - aerial photgraph of northeast quandrangle of San Francisco (1987)
  - houston.tif - urban footprint of Houston, TX
  - los_angeles.tif - urban footprint of Los Angeles, CA
  - gt30w140n40_dem/gt30w140n40.dem - Global 30 Arc-Second Elevation (GTOPO30) - digital elevation model 
  - doqq/* - Digital Orthophoto Quadrangles - 9 tiles from a section of Louisiana

* Vector Data
  - Bus_Stops.shp - San Francisco Bay Area bus stops
  - Civic_Art.shp - locations of artwork around San Francisco
  - sfzipcodes.shp - Zip Code boundaries in San Francisco
  - sfbayhighways.geojson - San Francisco Bay Area highways
  - SanFranciscoESI.gdb - Geodatabase created by the San Francisco Estuary Institute 

* Scripts
  - clipTiffs.py - clip GeoTIFFs to polygon boundary
  - projectShapes.py - reproject shapefiles to WGS84
  - projectTiffs.py - reproject GeoTIFFs to WGS84
  - shp2geojson.py - convert shapefiles to GeoJSON

* Text
  - colorramp.txt - color configuration file for relief mapping
