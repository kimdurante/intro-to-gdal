---
layout: default
title: Querying Data
nav_order: 5
---

## Finding and Selecing Data with SQL Queries

* [Querying Data](#querying-data)
* [Saving Query Results](#saving-query-results)
<br/>

Use the `-sql` flag to find and subset data by specific fields, attributes, or geometry

### Querying Data

Querying data with `ogrinfo`

Q: How many bus stops are contained in this file (_bus_stops_wgs84.shp_)

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
A: 79810

---


Q: How many unique stops are contained in this layer?


```
$ ogrinfo bus_stops_wgs84.shp -sql "SELECT COUNT(DISTINCT STOPID) FROM bus_stops_wgs84"
```
```
Layer name: bus_stops_wgs84
Geometry: None
Feature Count: 1
Layer SRS WKT:
(unknown)
COUNT_STOPID: Integer (0.0)
OGRFeature(bus_stops_wgs84):0
  COUNT_STOPID (Integer) = 23954
```

A: 23954

---


Q: How many stops are serviced by San Francisco MUNI?

```
$ ogrinfo bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84 WHERE AGENCY = 'San Francisco MUNI'"
```

```
Layer name: bus_stops_wgs84
...
OGRFeature(bus_stops_wgs84):0
  COUNT_* (Integer) = 13880
```

A: 13880

---

### Saving Query Results


Creating data from query results with `ogr2ogr`

Find all the SF MUNI stops and save it to a shapefile

```
$ ogr2ogr sf_muni_stops.shp bus_stops_wgs84.shp -sql "SELECT * FROM bus_stops_wgs84 WHERE AGENCY = 'San Francisco MUNI'"
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/sfmuni.png" width="500">

---
Clip the 94103 zipcode boundary and save it to a shapefile

```
ogr2ogr sf_94103.shp sfzipcodes.shp -t_srs EPSG:4326 -sql "SELECT * FROM sfzipcodes WHERE ZIP_CODE ='94103'"
```

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/94103.png" width="500">

Clip the 94109 zipcode boundary and save it to GeoJSON

```
$ ogr2ogr sf_94109.geojson -t_srs EPSG:4326 sfzipcodes.shp -sql "SELECT * FROM sfzipcodes WHERE ZIP_CODE ='94109'"
```
<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/94109.png" width="500">
