---
layout: default
title: Overview
nav_order: 1
---

Geospatial Data Abstraction Library (GDAL) provides command-line utilities to translate and process a wide range of raster and vector geospatial data formats. "GDAL/OGR" refers to the combined project containing both raster & vector tools:
   
   * GDAL: raster 
   * OGR: vector

## Installing GDAL

There are several options for downloading GDAL packages. 

### Mac

Download the appropriate framework for your MacOS:

[http://www.kyngchaos.com/software/frameworks/#gdal_complete](http://www.kyngchaos.com/software/frameworks/)

Once installed, open a terminal window and run the folowing command:

```export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH```

Or, save it to your profile:

```echo 'export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH' >> ~/.bash_profile
source ~/.bash_profile```

Test the installation by running the command

```gdalinfo --version```

On Windows:

Make sure Python is already installed. Download the appropriate binary for your version of Python:

[https://www.gisinternals.com/release.php](https://www.gisinternals.com/release.php)

### Download Data

Get the data

## Exploring Vector Data

* List information about a vector data source using ogrinfo

`ogrinfo SF/ZipCodes.shp`
