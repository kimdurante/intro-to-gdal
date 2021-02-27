---
layout: default
title: Indexing and Mosaicing
nav_order: 6
---

## Creating a Raster Mosaic

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaic.png" width="500">

```
gdalbuildvrt DOQQ/doqqs_merged.vrt -input_file_list DOQQ/doqqs.txt
```

```
gdal_translate -co COMPRESS=JPEG DOQQ/doqqs_merged.vrt DOQQ/doqqs_merged.tif
```
