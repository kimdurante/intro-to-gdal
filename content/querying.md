---
layout: default
title: Querying Data
nav_order: 5
---

## Selecing Data with SQL Queries
<br/>

Use the `-sql` flag to find and subset data by specific fields, attributes, or geometry

Use `ogrinfo` find the total number of stops listed in _bus_stops_wgs84.shp_

```
$ ogrinfo bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84"
```

```
Layer name: bus_stops_wgs84
Geometry: None
Feature Count: 1
Layer SRS WKT:
(unknown)
COUNT_*: Integer (0.0)
OGRFeature(bus_stops_wgs84):0
  COUNT_* (Integer) = 79810
```

Total number of stops: 79810

Find the number of stops serviced by Sonoma County Transit

```
$ ogrinfo -q bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84 WHERE AGENCY = 'Sonoma County Transit'"
```

```
Layer name: bus_stops_wgs84
Geometry: None
Feature Count: 1
Layer SRS WKT:
(unknown)
COUNT_*: Integer (0.0)
OGRFeature(bus_stops_wgs84):0
  COUNT_* (Integer) = 5719
```

Sonoma County Transit stops: 5719

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
