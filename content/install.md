---
layout: default
title: Getting Started
nav_order: 1
---

## Getting Started

* [Workshop Data](#workshop-data)
* [Installing GDAL](#installing-gdal)

## Workshop Data


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
