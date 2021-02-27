---
layout: default
title: Mosaicing
nav_order: 6
---

## Creating a Raster Mosaic

<img src="https://raw.githubusercontent.com/kimdurante/intro-to-gdal/master/images/mosaic.png" width="500">

```
for file in DOQQ/*/*.tif*; do echo "$file" >> doqq.txt; done
```

```
gdalbuildvrt DOQQ/doqqs_merged.vrt -input_file_list DOQQ/doqqs.txt
```

```
gdal_translate -co COMPRESS=JPEG DOQQ/doqqs_merged.vrt DOQQ/doqqs_merged.tif
```
