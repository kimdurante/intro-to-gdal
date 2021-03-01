---
layout: default
title: Digital Elevtion Models
nav_order: 7
---

## Digital Elevtion Models

### Hillshade

```
$ gdaldem hillshade -of png gt30w140n40_clipped.dem hillshade.png
```

### Color Relief

```
$ gdaldem color-relief gt30w140n40_clipped.dem colorramp.txt color_relief.tif
```

### Contour Lines

```
$ gdal_contour -a elev -i 20 gt30w140n40_clipped.dem contours.shp

```
