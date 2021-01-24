---
layout: default
title: Preparing Data
nav_order: 3
---

## Preparing Data

* Load all data into a collection folder (directory) that can be connected to ArcCatalog.

* Ensure that all layers meet the necessary requirements in order to function properly within SDR, SSDI, and EarthWorks. All layers must have a valid filename and valid coordinate metadata (geographic extent). 

* Vector and raster data delivered through GeoServer must include a valid spatial reference system (SRS).

### Checking Data Properties

* You can inspect data properites for one or more layers using ArcGIS, QGIS, or GDAL/OGR. 

* [Run this script to create a csv list of filenames, SRSs, and data types for shapefiles and/or GeoTIFFs.](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/checkData.py)

| FILENAME       | SRS   | TYPE |
| ------------- |-------------|-----------------|
|airmonitoringstations.shp|3310|Point|
|arb_california_airbasins_aligned_03.shp|3310|Polygon|
|arb_california_airdistricts_aligned_03.shp|3310| Polygon|
|arb_california_counties_aligned_03.shp|3310| Polygon|
|fed_1hr_coabdis.shp|3310| Polygon|


### Registering Data in Argo

* Create a CSV file containing a **SourceID** and a **Label** for each layer in the collection. The SourceID prefix for all GIS layers is '*branner:*' plus an abbreviation for the collection name, followed by an underscore. Append the filename to the end of this prefix to create the SourceID. (ex. branner: _fmmp12_alameda2012.shp_)

* The Label is the title of the data layer. If there is an existing title, use it. Otherwise, for georeferenced maps, use the original map title plus '(Raster Image)', for other data, create a title using the pattern: *What, Where, When* (ex. _Topographical map of the Yosemite Valley and vicinity (Raster Image)_ or _Important Farmland, Alameda County, California, 2012_)

* Format the CSV as shown below, leaving the first and third columns blank:

||SOURCEID||LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp||Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp||Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp||Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp||Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp||Important Farmland, Contra Costa County, California, 2012|


_Example layers from the California Farmland Mapping and Monitoring Program, 2012 collection._


* Register the items in Argo using the APO/Collection and the Content Type **File**. Paste the DRUIDs into the CSV.

||SOURCEID|DRUID|LABEL|
|:----|:----|:----|:----|
||branner:fmmp12_alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|
||branner:fmmp12_amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|
||branner:fmmp12_butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|
||branner:fmmp12_colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|
||branner:fmmp12_contracosta2012.shp|rc560ns7872|Important Farmland, Contra Costa County, California, 2012|

* Save the file (ex. _layers.csv_). This can used to generate metadata during cataloging.
