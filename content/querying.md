---
layout: default
title: Querying Data
nav_order: 5
---

## Querying Data

Use the `-sql` flag with `ogrinfo` to query vector datasets.

Find the total number of stops listed in the Bus Stops file

```
ogrinfo SF/bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84"
```
Find the number of stops serviced by Sonoma County Transit

```
$ ogrinfo -q SF/bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84 WHERE AGENCY = 'Sonoma County Transit'"
```

How many unique bus stops are contained in this layer
```
ogrinfo -q SF/bus_stops_wgs84.shp -sql "SELECT COUNT(DISTINCT STOPID) FROM bus_stops_wgs84"
```

How many zip codes are in San Francisco

```
ogrinfo SF/ZipCodes.shp -sql "SELECT COUNT(*) FROM ZipCodes WHERE po_name ='San Francisco'"
```

Saving query results to a new file

```
ogr2ogr SF/sf_zipcodes.geojson SF/ZipCodes.shp -sql "SELECT * FROM ZipCodes WHERE po_name ='San Francisco'"
```

Save a GeoJSON file containing the boundary of 94109

```
ogr2ogr SF/sf_94109.geojson SF/ZipCodes.shp -sql "SELECT * FROM ZipCodes WHERE zip ='94109'"
```
