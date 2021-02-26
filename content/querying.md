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

How many unique stops are contained in this layer?
```
ogrinfo bus_stops_wgs84.shp -sql "SELECT COUNT(DISTINCT STOPID) FROM bus_stops_wgs84"
```

Total unique stops: 23954

How many stops aRE serviced by Sonoma County Transit?

```
$ ogrinfo bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84 WHERE AGENCY = 'Sonoma County Transit'"
```

```
Layer name: bus_stops_wgs84

COUNT_*: Integer (0.0)
OGRFeature(bus_stops_wgs84):0
  COUNT_* (Integer) = 5719
```

Sonoma County Transit stops: 5719


How many zip codes are in San Francisco?

```
ogrinfo sfzipcodes.shp -sql "SELECT COUNT(*) FROM sfzipcodes"
```

Find the boundary of zipcode 94109 and save it to GeoJSON

```
ogr2ogr sf_94109.geojson sfzipcodes.shp -sql "SELECT * FROM sfzipcodes WHERE ZIP_CODE ='94109'"
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/94109.png" width="500">
