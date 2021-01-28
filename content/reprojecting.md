---
layout: default
title: Reprojecting Data
nav_order: 4
---

## Reprojecting Data


### gdal_warp

Use ```gdal_warp``` to reproject raster data.

```
gdalwarp -t_srs (srs, old, new)```
```

```
gdalwarp -t_srs EPSG:4326 SF/SF1987.tif SF/SF1987_wgs84.tif
```

### ogr2ogr

Use ```ogr2ogr``` with the target SRS flag (```t_srs```) to reproject vector data. 

```ogr2ogr -t_srs (srs, new, old)```

```ogr2ogr -t_srs EPSG:4326 SF/bus_stops_wgs84.shp SF/Bus_Stops.shp```

See a list of available formats:

```$ ogr2ogr --formats```
