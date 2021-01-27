---
layout: default
title: Creating Metadata with ArcCatalog
nav_order: 0
parent: Metadata
---

## Creating Metadata with ArcCatalog


[Setting Up ArcCatalog](#setting-up-arccatalog)  
[Creating a Collection Template](#creating-a-collection-template)  
[Importing a Template](#importing-a-template)  
[Updating Metadata for Individual Layers](#updating-metadata-for-individual-layers)  
[Autogenerating Metadata](#autogenerating-metadata)  
[Autogenerating Thumbnail Images](#autogenerating-thumbnail-images)  

### Setting Up ArcCatalog

* Open ArcCatalog. Connect to the data folder.

* Set the Metadata Style to ISO 19139. From the Menu bar:

```Customize > ArcCatalog Options > Metadata > ISO 19139 Metadata Implementation Specification```


### Creating a Collection Template

* Copy the [the geoMetadata template](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/templates/template.xml) into the data folder.

* Open the template and add metadata values that are common among all layers. 

* This is a very straightforward example from the California Farmland Mapping and Monitoring Program, 2012 collection. Many of the values are identical for each shapefile (organization name, theme keywords, temporal extent, update frequency, rights, and attribute definitions). The abstract text varies only when specifying the county name.



|FIELD|VALUE|
|:-----|:-----|
|Abstract|This polygon shapefile represents areas of important farmland in COUNTY, California for 2012. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.|
|Purpose|The Farmland Mapping and Monitoring Program (FMMP) provides data to decision makers for use in planning for the present and future use of California's agricultural land resources. The data is a current inventory of agricultural resources. This data is for general planning purposes and has a minimum mapping unit of ten acres.|
|ISO topic category|Farming|
|Theme keywords|Land use<br/>Urbanization<br/>Agriculture|
|Collective title|California Farmland Mapping and Monitoring Program, 2012|
|Publication Date|2012-01-01|
|Publisher|California. Farmland Mapping and Monitoring Program|
|Originator|California. Farmland Mapping and Monitoring Program|
|Parent metadata identifier|https://purl.stanford.edu/rn450jx3747.mods|
|Temporal extent description|ground condition|
|Temporal extent|2012-01-01|
|Point of contact|California. Farmland Mapping and Monitoring Program|
|Maintenance and Update Frequency|Biannually|
|Use constraints|This item is in the public domain. There are no restrictions on use.|
|Aggregate dataset title|California Farmland Mapping and Monitoring Program, 2012|
|Aggregate dataset identifier|https://purl.stanford.edu/rn450jx3747|
|Attribute Labels|county_nam<br/>upd_year<br/>polygon_ty|
|Attribute Definitions|County name<br/>Update year<br/>Farmland categories: Prime Farmland (P), Farmland of Statewide Importance (S), Unique Farmland (U), Farmland of Local Importance (L), Grazing Land (G), Urban and Built-up Land (D), Other Land (X)|

* Save the template

### Importing a Template


* Import the template into each layer using one of the following methods. Note that importing a template will overwrite any existing metadata.

#### ArcGIS Metadata Importer


* ArcGIS Metadata Importer Tool can import a template into one or more layers using singular or batch import methods. 

* When importing into a single layer use the import type: ```FROM_ARCGIS```

#### ArcPy

* ArcPy is a much faster alternative to the importer tool. To apply a template to a collection, from the Menu bar: ```GeoProcessing > Python```

* Enter the code below. Replace ```C:/PATH/TO/DIRECTORY``` with the correct path:

```
>>> import os, arcpy
>>> from arcpy import env
>>> env.workspace: r‘C:/PATH/TO/DIRECTORY’
>>> layers = arcpy.ListFeatureClasses('*')
>>> for layer in layers:
    arcpy.ImportMetadata_conversion(r"C:/PATH/TO/TEMPLATE/template.xml",FROM_ARCGIS",layer)
```

#### Python

* [This python script can be run from the collection folder](https://github.com/kimdurante/metadataWorkflow/blob/master/scripts/importTemplate.py)

### Updating Metadata for Individual Layers

Select a layer from the directory. Update the metadata elements with values unique to that layer.  

Example: alameda2012.shp

|FIELD|VALUE|
|:-----|:-----|
|Title|Important Farmland, Alameda County, California, 2012|
|Abstract|This polygon shapefile represents areas of important farmland in Alameda County, California for 2012. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.|
|Credit|California Farmland Mapping and Monitoring Program. (2012). Important Farmland, Alameda County, California, 2012. California Farmland Mapping and Monitoring Program. Available at: http://purl.stanford.edu/rp378rd3804.|
|Place keywords|Alameda County (Calif.)|
|Identifier|https://purl.stanford.edu/rp378rd3804|
|Metadata File Identifier|edu.stanford.purl:rp378rd3804|
|Dataset URI|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Linkage|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Name|alameda2012.shp|
|Feature Catalog Identifier|564c855e-e45a-47dc-b0c4-001839b00864|

* Save the file.

#### Create a Thumbnail Image

* On the Preview tab use the Thumbnail Generator tool to create a thumbnail preview for the layer.

![alameda.jpg](https://raw.githubusercontent.com/kimdurante/geospatial-data-management/main/content/img/alameda.jpg)

* Open the next layer in the directory and add the individual values.

Example: amador2012.shp

|FIELD|VALUE|
|:-----|:-----|
|Title|Important Farmland, Amador County, California, 2012|
|Abstract|This polygon shapefile represents areas of important farmland in Amador County, California for 2012. Established in 1982, Government Code Section 65570 mandates FMMP to biennially report on the conversion of farmland and grazing land, and to provide maps and data to local government and the public.|
|Credit|California Farmland Mapping and Monitoring Program. (2012). Important Farmland, Amador County, California, 2012. California Farmland Mapping and Monitoring Program. Available at: http://purl.stanford.edu/mc357cj1107.|

<details><summary>See All</summary>
<br/>
<table>
  <tr>
    <td class="tg-0lax">Place Keywords</td>
    <td class="tg-0lax">Almador County (Calif.)</td>
  </tr>
  <tr>
    <td class="tg-0lax">Identifier</td>
    <td class="tg-0lax">https://purl.stanford.edu/mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Metadata File Identifier</td>
    <td class="tg-0lax">edu.stanford.purl:mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Dataset URI</td>
    <td class="tg-0lax">https://purl.stanford.edu/mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Distribution Online Linkage</td>
    <td class="tg-0lax">https://purl.stanford.edu/mc357cj1107</td>
  </tr>
  <tr>
    <td class="tg-0lax">Distribution Online Name</td>
    <td class="tg-0lax">amador2012.shp</td>
  </tr>
  <tr>
    <td class="tg-0lax">Feature Catalog Identifier</td>
    <td class="tg-0lax">e011c181-590e-4d9a-bcbd-de2df592d00c</td>
  </tr>
</table>
</details>

### Autogenerating Metadata

Even a relatively simple collection example like the one above requires lot of manual entry across dozens of files. Using tools to automate input, especially when metadata contain URLs or redundant information, can make processing XML faster and less susceptible to error.

In these examples the first four elements (title, abstract, place keyword, and credit) contain free text referencing the specific county (Alameda, Amador, etc.). The remaining elements are strings containing identifiers or filenames. 

The credit element contains the preferred citation text used MODS (PURL) metadata. In most cases this element can be derived from existing metadata elements: originator, date, title, publisher, and PURL.


Create a csv file called ```layers.csv``` containing four columns: FILENAME, DRUID, TITLE, UUID. The filename, title, and DRUID for each layer can be obtained from an Argo report. The UUID column contains the identifier for linking the ISO 19139 and ISO 19110 metadata. [Generate UUIDs here](https://www.uuidgenerator.net).

Save ```layers.csv``` to the collection directory.


|FILENAME|DRUID|TITLE|UUID|
|:-----|:-----|:-----|:-----|
|alameda2012.shp|rp378rd3804|Important Farmland, Alameda County, California, 2012|564c855e-e45a-47dc-b0c4-001839b00864|
|amador2012.shp|mc357cj1107|Important Farmland, Amador County, California, 2012|e011c181-590e-4d9a-bcbd-de2df592d00c|
|butte2012.shp|wf469qr5893|Important Farmland, Butte County, California, 2012|0cb51486-aebf-4e64-8d07-2f1039bafee1|
|colusa2012.shp|rc560ns7872|Important Farmland, Colusa County, California, 2012|8837d532-7ae4-4fa6-8adf-b1ad7abd89ac|

* Save a copy of [this Python script](https://github.com/kimdurante/metadataWorkflow/blob/master/scripts/addMetadata.py) in the collection directory. 

Change the `AUTHOR` and `PUBLISHER` variables to display names for use in the citation field. 

Run:

```>>> python addMetadata.py```

The following fields will be autogenerated:

|FIELD|VALUE|
|:-----|:-----|
|Title|Important Farmland, Alameda County, California, 2012|
|Credit|California Farmland Mapping and Monitoring Program. (2012). Important Farmland, Alameda County, California, 2012. California Farmland Mapping and Monitoring Program. Available at: http://purl.stanford.edu/rp378rd3804.|
|Identifier|https://purl.stanford.edu/rp378rd3804|
|Metadata File Identifier|edu.stanford.purl:rp378rd3804|
|Dataset URI|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Linkage|https://purl.stanford.edu/rp378rd3804|
|Distribution Online Name|alameda2012.shp|
|Feature Catalog Identifier|564c855e-e45a-47dc-b0c4-001839b00864|

#### Autogenerating Thumbnail Images

Currently only works for polygon data types.

[Use this Python script to autogenerate thumbnail images for polygon shapefile data](https://raw.githubusercontent.com/kimdurante/metadataWorkflow/master/scripts/createThumbnails.py). This script will create a JPEG and insert the binary code into the ArcGISXML metadata.
