---
layout: default
title: Querying Data
nav_order: 5
---

## Selecing Data with SQL Queries

* [Querying Data](#querying-data)
* [Saving Data](#saving-data)
<br/>

Use the `-sql` flag to find and subset data by specific fields, attributes, or geometry

### Querying Data
<br/>
Use `ogrinfo` find the total number of stops listed in _bus_stops_wgs84.shp_
<br/>

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
$ ogrinfo bus_stops_wgs84.shp -sql "SELECT COUNT(DISTINCT STOPID) FROM bus_stops_wgs84"
```

Total unique stops: 23954

How many stops are serviced by San Francisco MUNI?

```
$ ogrinfo bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84 WHERE AGENCY = 'San Francisco MUNI'"
```

```
Layer name: bus_stops_wgs84
...
OGRFeature(bus_stops_wgs84):0
  COUNT_* (Integer) = 13880
```

### Saving Data

SF MUNI stops: 13880

Find all the SF MUNI stops and save it to CSV

```
$ ogr2ogr sf_muni_stops.csv bus_stops_wgs84.shp -sql "SELECT * FROM bus_stops_wgs84 WHERE AGENCY = 'San Francisco MUNI'"
```

Find the boundary of zipcode 94109 and save it to GeoJSON

```
$ ogr2ogr sf_94109.geojson sfzipcodes.shp -sql "SELECT * FROM sfzipcodes WHERE ZIP_CODE ='94109'"
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/94109.png" width="500">
