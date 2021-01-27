---
layout: default
title: Installing GDAL
nav_order: 1
---

## Installing GDAL

There are several options for downloading GDAL packages. 

### On a Mac

Download the appropriate framework for your MacOS:

[http://www.kyngchaos.com/software/frameworks/#gdal_complete](http://www.kyngchaos.com/software/frameworks/)

Once installed, open a terminal window and run the folowing command:

```export PATH=/Library/Frameworks/GDAL.framework/Programs:$PATH```

Or, save it to your profile:

Test the installation:

```gdalinfo --version```

### On Windows:

Make sure Python is already installed. Download the appropriate binary for your version of Python:

[https://www.gisinternals.com/release.php](https://www.gisinternals.com/release.php)

### Download Data

Get the data

## Exploring Vector Data

* List information about a vector data source using ogrinfo

`ogrinfo SF/ZipCodes.shp`

