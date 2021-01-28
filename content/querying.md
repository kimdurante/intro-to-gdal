---
layout: default
title: Querying Data
nav_order: 5
---

## Querying Data

Use the ```-sql``` flag to query 
```
ogrinfo (file, -sql)
```

```
$ ogrinfo SF/bus_stops_wgs84.shp -sql "SELECT COUNT(*) FROM bus_stops_wgs84"
```
