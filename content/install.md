---
layout: default
title: Getting Started
nav_order: 1
---

## Getting Started

* [Installing GDAL](#installing-gdal)
* [Workshop Data](#workshop-data)


## Installation

### Conda

GDAL can be quite complex to build and install, particularly on Windows and MacOS. Pre built binaries are provided for the conda system:

https://docs.conda.io/en/latest/

By the conda-forge project:

https://conda-forge.org/

Once you have Anaconda or Miniconda installed, you should be able to install GDAL with:

```$ conda install -c conda-forge gdal```


### pip

GDAL can be installed from the Python Package Index:

```$ pip install GDAL```

It will be necessary to have libgdal and its development headers installed if pip is expected to do a source build because no wheel is available for your specified platform and Python version.

To install the version of the Python bindings matching your native GDAL library:

### Windows

You will need the following items to complete an install of the GDAL Python bindings on Windows:

[GDAL Windows Binaries](https://www.gisinternals.com) - Download the package that best matches your environment.

As explained in the README_EXE.txt file, after unzipping the GDAL binaries you will need to modify your system path and variables. If you’re not sure how to do this, read the Microsoft Knowledge Base doc

1. Add the installation directory bin folder to your system PATH, remember to put a semicolon in front of it before you add to the existing path.
    
    ```C:\gdalwin32-1.7\bin```
    
2. Create a new user or system variable with the data folder from your installation.

    ```Name : GDAL_DATA```
    
    ```Path : C:\gdalwin32-1.7\data```
    
 Verify that the installation was successful by opening a terminal and running the following command:
 
```
$ gdalinfo --version
```
    
## Workshop Data

Download the zip file of workshop data

[Download Data](https://drive.google.com/file/d/1R7IymHj5XLfTy61WvEvkEpgNjCBxGAIv/view?usp=sharing)

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
