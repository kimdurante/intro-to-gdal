---
layout: default
title: Data Wrangling
nav_order: 7
---

## Data Wrangling

### Filenaming

* Filenames should contain only letters, numbers, or underscores. No other special characters should be used. When renaming files, be sure to rename all files uniformly.


| Invalid| Valid   |
| :----- |:-----|
|RIVERS&TRIBUTARIES.shp|RIVERS_TRIBUTARIES.shp|
|RIVERS&TRIBUTARIES.prj|RIVERS_TRIBUTARIES.prj|
|RIVERS&TRIBUTARIES.shx|RIVERS_TRIBUTARIES.shx|
|RIVERS&TRIBUTARIES.dbf|RIVERS_TRIBUTARIES.dbf|


* In some cases errors can occur when file extensions are capitalized. Renaming the file should resolve this error.


| Old  | New   |
| :----- |:-----|
|ZONING.CPG|ZONING.cpg|
|ZONING.DBF|ZONING.dbf|

* Use this script to find and fix errors in filenaming.


### Spatial Reference Systems

* All GIS layers must have an associated spatial reference system (SRS). SRS metadata are recorded using a code (ex. EPSG) and a codespace (ex. 2227). 

* All layers with an SRS that is not EPSG:4326 (WGS84) are transformed during accessioning and made available for download in both the original and transformed ('generated') versions.

Use of the Web Mercator (EPSG:3857) SRS is not recommended.
{: .note}

###  Data Properties

In some cases data will need to be inspected using GIS or geospatial toolkits.  

**GDAL/OGR**

Inspect vector data with GDAL/OGR

```
>>> ogrinfo -al -so AirMonitoringStations.shp

Layer name: AirMonitoringStations
Metadata:
  DBF_DATE_LAST_UPDATE=2003-05-12
Geometry: Point
Feature Count: 294
Extent: (-351223.407414, -624485.505426) - (437272.916273, 422258.624752)
Layer SRS WKT:
PROJCS["NAD83 / California Albers",
```
Inspect raster data with GDAL

```
>>> gdalinfo gcw0678500a.tif

Driver: GTiff/GeoTIFF
Files: gcw0678500a.tif
       gcw0678500a.aux
       gcw0678500a.rrd
Size is 13511, 10390
Coordinate System is:
GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0],
    UNIT["degree",0.0174532925199433],
    AUTHORITY["EPSG","4326"]]
Origin = (-77.176496000000000,38.998134200000003)
Pixel Size = (0.000020000000000,-0.000020000000000)
Metadata:
  AREA_OR_POINT=Area
  TIFFTAG_RESOLUTIONUNIT=1 (unitless)
  TIFFTAG_SOFTWARE=IMAGINE TIFF Support

```

**ArcGIS**

In a GIS, viewing layer properties, preview images, and attribute tables are useful methods for inspecting data. Opening the layer over a basemap may also be necessary. 

**QGIS**

View layer properties, attribute tables and overlay data in QGIS

![QGIS Layer Properties](https://github.com/kimdurante/metadataWorkflow/blob/master/images/QGISprop.jpeg)


### List Data Properties in a CSV

[Run this script to create a csv list of filenames, SRSs, and data types for shapefiles and/or GeoTIFFs.](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/checkData.py)

| FILENAME       | SRS   | TYPE |
| ------------- |-------------|-----------------|
|airmonitoringstations.shp|3310|Point|
|arb_california_airbasins_aligned_03.shp|3310|Polygon|
|arb_california_airdistricts_aligned_03.shp|3310| Polygon|
|arb_california_counties_aligned_03.shp|3310| Polygon|
|fed_1hr_coabdis.shp|3310| Polygon|
