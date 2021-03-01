---
layout: default
title: Digital Elevtion Models
nav_order: 7
---

## Digital Elevation Models

The `gdaldem` utility can be used to analyze and visualize DEMs. 

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/dem_clip.png" width="500">

### Hillshade

```
$ gdaldem hillshade -of png gt30w140n40_clipped.dem hillshade.png
```


<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/hillshade.png" width="500">

### Color Relief

```
$ gdaldem color-relief gt30w140n40_clipped.dem colorramp.txt color_relief.tif
```


<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/colorrelief.png" width="500">

### Contour Lines

```
$ gdal_contour -a elev -i 20 gt30w140n40_clipped.dem contours.shp
```


<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/contours.png" width="500">
