---
layout: default
title: Digital Elevation Models
nav_order: 7
---

## Digital Elevation Models

* [Hillshade](#hillshade)
* [Color Relief](#color-relief)
* [Contour Lines](#contour-lines)

The `gdaldem` utility can be used to analyze and visualize DEMs. 

Let's analyze our clipped DEM 

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/dem_clip.png" width="500">

### Hillshade

Generate a hillshade (shaded relief map)

```
$ gdaldem hillshade -of png gt30w140n40_clipped.dem hillshade.png
```


<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/hillshade.png" width="500">

### Color Relief

Generate a color relief map with values are computed from the elevation and a color configuration file (colorramp.txt)

```
$ gdaldem color-relief gt30w140n40_clipped.dem colorramp.txt color_relief.tif
```


<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/colorrelief.png" width="500">

### Contour Lines

Build vector contour lines from a raster elevation model. Use the `-a` flag to set the elevation attribute and `-i` flag to specify elevation intervals. 

```
$ gdal_contour -a elev -i 100 gt30w140n40_clipped.dem contours_100m.shp
```


<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/contours_100m.png" width="500">


[Working with Terrain Data](https://tilemill-project.github.io/tilemill/docs/guides/terrain-data/)
