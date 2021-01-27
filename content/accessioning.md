---
layout: default
title: Accessioning Data
nav_order: 6
---
## SDR Accessioning and EarthWorks Indexing

Once metadata have been completed for all layers, the files need to be organized and staged for accessioning.

### Staging Data

Make a directory for the collection on a staging environment.<br/>
Example: California_Farmland_Mapping_2012

In the collection directory, make a folder for each layer using the DRUID as the name. In each DRUID folder, make a folder called ```temp```.

Example:
```
California_Farmland_Mapping_2012
 
-bd235mg0255  
--temp

-bw755mz6720  
--temp
```

[Run this script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/scripts/makeFolders.py) in the collection directory to create ```DRUID/temp``` folders for each layer.


Move all files associated with the layer into the appropriate ```DRUID/temp``` folder. [This script](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/scripts/moveFiles.py) will find all files and move them into the staging environment.

### SDR Accessioning and EarthWorks

Accessioning Data into SDR and indexing them into EarthWorks relies on 4 robot workflows which are documented in the [gis-robot-suite](https://github.com/sul-dlss/gis-robot-suite/tree/master/robots)

[Follow these instructions for Accessioning Data into SDR and EarthWorks](https://consul.stanford.edu/display/SULAIRGIS/HOWTO+-+Accession+layers)
