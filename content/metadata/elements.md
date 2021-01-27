---
layout: default
title: Required and Recommended Metadata Elements
nav_order: 1
parent: Metadata
---

## Required and Recommended Metadata Elements for Geospatial Data

### Brief

|Element|Required?|
|:-----|:--|
|[Metadata file identifier](#metadata-file-identifier)|Y|
|[Dataset URI](#dataset-uri)|Y|
|[Reference system identifier](#reference-system-identifier)|Y|
|[Title](#title)|Y|
|[Identifier](#identifier)|Y|
|[Geographic Extent](#geographic-extent)|Y|
|[Publication Date](#publication-date)||
|[Originator](#originator)||
|[Publisher](#publisher)||
|[Abstract](#abstract)|Y|
|[Credit](#credit)||
|[ISO Topic Category](#iso-topic-category)||
|[Theme Keyword](#theme-keyword)|Y|
|[Place Keyword](#place-keyword)|Y|
|[Parent metadata identifier](#parent-metadata-identifier)||
|[Status](#status)||
|[Dataset Language](#dataset-language)||
|[Temporal Extent](#temporal-extent)||
|[Point of Contact](#point-of-contact)||
|[Maintenance and Update Frequency](#maintenance-and-update-frequency)||
|[Access Constraints](#access-constraints)||
|[Use Constraints](#use-constraints)||
|[Data Source Citation Title](#data-source-citation-title)||
|[Data Source Citation Identifier](#data-source-citation-identifier)||
|[Distribution Format](#distribution-format)||
|[Distributor](#distributor)||
|[Digital Transfer Online Linkage](#digital-transfer-online-linkage)||
|[Digital Transfer Online Protocol](#digital-transfer-online-protocol)||
|[Digital Transfer Online Name](#digital-transfer-online-name)||
|[Aggregate Dataset Title](#aggregate-dataset-title)||
|[Aggregate Dataset Identifier](#aggregate-dataset-identifier)||
|[Feature Catalog Identifier](#feature-catalog-name)||
|[Thumbnail Preview](#thumbnail-preview)|Y|

### Detailed

#### Metadata File Identifier

|Element|Metadata file identifier|
|:-----|:------|
|Required|Y|
|Type|string|
|Description|Unique identifier for the metadata|
|Entry Guidelines|Codespace and identifier. For all SUL objects, the codespace is 'edu.stanford.purl' and the identifier is the DRUID|
|Controlled Vocabulary|no|
|Example|edu.stanford.purl:rp378rd3804|

#### Dataset URI

|Element|Dataset URI|
|:-----|:------|
|Required|Y|
|Type|string|
|Description|Universal Resource Identifier (URI) for the dataset|
|Entry Guidelines|PURL|
|Controlled Vocabulary|no|
|Example|https://purl.stanford.edu/rp378rd3804|

#### Reference System Identifier

|Element|Reference System Identifier|
|:-----|:------|
|Required|Y|
|Type|string|
|Description|Namespace and numeric code that identifies a spatial reference assigned by a formally registered ontology|
|Entry Guidelines|Recommended: [EPSG Geodetic Parameter Registry](http://www.epsg-registry.org)|
|Controlled Vocabulary|yes|
|Example|EPSG:4326

#### Title

|Element|Title|
|:-----|:------|
|Required|Y|
|Type|string|
|Description|The name of the resource|
|Entry Guidelines|If the data already have an existing title, use it. For georeferenced maps, use the original map title plus '(Raster Image)'. Otherwise, create a title using the pattern: *What, Where, When*.|
|Controlled Vocabulary|no|
|Example|Bat Ranges, United States and Canada, 1830-2008|

#### Identifier

|Element|Identifier|
|:-----|:------|
|Required|Y|
|Type|string|
|Description|Unique identifier for layer as a URI|
|Entry Guidelines|PURL|
|Controlled Vocabulary|no|
|Example|https://purl.stanford.edu/jm039td8162|

#### Geographic Extent

|Element|Geographic Extent|
|:-----|:------|
|Required|Y|
|Type|string|
|Description|The rectangular extents of the resource|
|Entry Guidelines|A bounding box. Westernmost, easternmost, northernmost, and southernmost coordinates in decimal degrees. These metadata should auto-populate when data are opened or refreshed in ArcCatalog.|
|Controlled Vocabulary|no|
|Example|-121.031785<br/>-120.070960<br/>38.709194<br/>38.217118|

#### Publication Date

|Element|Publication Date|
|:-----|:------|
|Required|no|
|Type|dateTime|
|Description|This is the publication date for the resource|
|Entry Guidelines|In ArcCatalog, use the calendar to input the year, month, and day of publication. If day or month is unknown, use 01. If entering data outside of Arc, use the format: YYYY-MM-DDT00:00:00.|
|Controlled Vocabulary|no|
|Example|2019-01-01|


#### Originator

|Element|Originator|
|:-----|:------|
|Required||
|Type|string|
|Description|The person(s) or organization(s) that created the resource|
|Entry Guidelines|This may be one or more individuals or organizations. If available, it should match with the Library of Congress Name Authority File.|
|Controlled Vocabulary|Suggested vocabulary is the Library of Congress Name Authority File.|
|Example|Sullivan, Elaine A.|


#### Publisher

|Element|Publisher|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The organization that made the original resource available|
|Entry Guidelines|This may be one or more organizations. If available, it should match with the Library of Congress Name Authority File.|
|Controlled Vocabulary|Suggested vocabulary is the Library of Congress Name Authority File.|
|Example|California. Farmland Mapping and Monitoring Program|

#### Abstract

|Element|Abstract|
|:-----|:------|
|Required|yes|
|Type|string|
|Description|A description of the data. This can include the data type (point, line, polygon, GeoTIFF, etc.), key features, geography, source data, and temporal extent. Other details such as the scale resolution, should be included when applicable|
|Entry Guidelines|Free text summary|
|Controlled Vocabulary|no|
|Example|This polygon dataset represents our current understanding of the distributions of United States and Canadian bat species during the past 100-150 years. The specimen and capture data were obtained from a variety of data sources, including U.S. State natural heritage programs, Canadian conservation data centres, published literature, unpublished reports, museum collections, and personal communications from university, federal, State and local biologists. Records are all specimen, roost, capture, or positive visual identification-based; no acoustic-only identifications were used for this map layer.|

#### Credit

|Element|Credit|
|:-----|:------|
|Required|no|
|Type|string|
|Description|A citation for the resource|
|Entry Guidelines|[ORIGINATOR. (PUB YEAR). TITLE. PUBLISHER. Available at: PURL. <br/>SUL MODS uses this value for the Preferred Citation element.|
|Controlled Vocabulary|no|
|Example|International Livestock Research Institute. (2007). Wildebeest Distribution, Kenya, 1994-1996. ILRI. Available at: http://purl.stanford.edu/kg342gc4695|

#### ISO Topic Category

|Element|ISO Topic Category|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Topic keywords|
|Entry Guidelines|In ArcCatalog, use the checkboxes to select one or more topics.|
|Controlled Vocabulary|[MD_TopicCategoryCode](http://wiki.esipfed.org/index.php/ISO_19115_and_19115-2_CodeList_Dictionaries#MD_TopicCategoryCode)|
|Example|Transportation|

#### Theme Keyword

|Element|Theme Keyword|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Theme keywords|
|Entry Guidelines|These should be consistent and chosen from a controlled vocabulary. In ArcCatalog, enter one keyword per line.|
|Controlled Vocabulary|[Library of Congress Subject Headings](http://id.loc.gov/authorities/subjects.html)|
|Example|Census<br/>Housing|

#### Place Keyword

|Element|Place Keyword|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Keywords containing place names|
|Entry Guidelines|These should be consistent and chosen from a controlled vocabulary. In ArcCatalog, enter one keyword per line.|
|Controlled Vocabulary|Use either [Library of Congress Name Authority File](http://id.loc.gov/authorities/name.html) or [Library of Congress Subject Headings](http://id.loc.gov/authorities/subjects.html)|
|Example|Alameda County (Calif.)|

#### Status

|Element|Status|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Status of the dataset or progress of a review.|
|Entry Guidelines|Codelist|
|Controlled Vocabulary|[MD_ProgressCode](http://wiki.esipfed.org/index.php/ISO_19115_and_19115-2_CodeList_Dictionaries#MD_ProgressCode)|
|Example|Completed|

#### Maintenance and Update Frequency

|Element|Maintenance and Update Frequency|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The frequency of changes and additions made to the resource.|
|Entry Guidelines|Codelist|
|Controlled Vocabulary|[MD_MaintenanceFrequencyCode](http://wiki.esipfed.org/index.php/ISO_19115_and_19115-2_CodeList_Dictionaries#MD_MaintenanceFrequencyCode)|
|Example|Biannually|

#### Access Constraints

|Element|Access Constraints|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Restrictions on user access to the data|
|Entry Guidelines|In ArcCatalog, use the drop-down menu: leave empty for 'Public', or use 'Restricted' for Stanford-only data|
|Controlled Vocabulary|[MD_RestrictionCode](http://wiki.esipfed.org/index.php/ISO_19115_and_19115-2_CodeList_Dictionaries#[MD_RestrictionCode)||
|Example|Restricted|

#### Use Constraints

|Element|Use Constraints|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Restrictions on use and reproduction of the data|
|Entry Guidelines|If there is a use/reproduction statement, select 'Other Restrictions' from the drop-down menu and provide the statement as free-text. Otherwise, leave empty for 'Public' data, or use 'Restricted' for Stanford-only data|
|Controlled Vocabulary|[MD_RestrictionCode](http://wiki.esipfed.org/index.php/ISO_19115_and_19115-2_CodeList_Dictionaries#[MD_RestrictionCode)|
|Example|Attribution Non-Commercial Share Alike 3.0 Unported|

#### Aggregate Dataset Title

|Element|Aggregate Dataset Title|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The title of the collection|
|Entry Guidelines|For aggregate dataset information, set the type to "Larger Work Citation".|
|Controlled Vocabulary|no|
|Example|California Farmland Mapping and Monitoring Program, 2012|

#### Aggregate Dataset Identifier

|Element|Aggregate Dataset Identifier|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The collection PURL|
|Entry Guidelines|Collection PURL|
|Controlled Vocabulary|no|
|Example|https://purl.stanford.edu/qf529ms0562|

#### Parent Metadata Identifier

|Element|Parent Metadata Identifier|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The collection metadata|
|Entry Guidelines|The URL to the MODS metadata|
|Controlled Vocabulary|no|
|Example|https://purl.stanford.edu/qf529ms0562.mods|

#### Temporal Extent

|Element|Temporal Extent|
|:-----|:------|
|Required|no|
|Type|dateTime|
|Description|Date or date range for which the content of the resource is valid. Sometimes this is referred to as ground condition or date of situation.|
|Entry Guidelines| In ArcCatalog, use the calendar to input the year, month, and day for the date or date range. If day or month is unknown, use 01. If entering data outside of Arc, use the format: YYYY-MM-DDT00:00:00. <br/> If the ground condition date is unknown, use the publication date.|
|Controlled Vocabulary|no|
|Example|1984-01-01|

#### Data Source Citation Title

|Element|Data Source Citation Title|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Title of the source data used to create the data. Used primarily for georeferenced maps|
|Entry Guidelines|Title of the original data|
|Controlled Vocabulary|no|
|Example|Ancient Africa or Libya, Part I (western section)|

#### Data Source Citation Identifier

|Element|Data Source Citation Identifier|
|:-----|:------|
|Required|no|
|Type|string|
|Description|URL to the source data used to create the data.|
|Entry Guidelines|PURL or other URI|
|Controlled Vocabulary|no|
|Example|https://purl.stanford.edu/hg645tg2944|


#### Distribution Format

|Element|Distribution Format|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The format of the data|
|Entry Guidelines| Choose from values:<br/>Shapefile<br/>GeoTIFF<br/>ArcGRID|
|Controlled Vocabulary|[Format Controlled Vocabulary](https://github.com/geoblacklight/geoblacklight/wiki/Format-values)|
|Example|GeoTIFF|

#### Distributor

|Element|Distributor|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The name of the institution that holds the resource or acts as the custodian for the metadata record|
|Entry Guidelines|For all layers in SDR, this is always Stanford Geospatial Center. Includes contact information.|
|Controlled Vocabulary|no|


#### Digital Transfer Online Linkage

|Element|Digital Transfer Online Linkage|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Link to page displaying information about the resource.|
|Entry Guidelines|PURL|
|Controlled Vocabulary|no|
|Example|https://purl.stanford.edu/rp378rd3804|

#### Digital Transfer Online Protocol

|Element|Digital Transfer Online Protocol|
|:-----|:------|
|Required|no|
|Type|string|
|Description|Protocol for accessing the resource|
|Entry Guidelines|Always http|
|Controlled Vocabulary|[CatInterop Vocabulary](https://github.com/OSGeo/Cat-Interop/blob/master/LinkPropertyLookupTable.csv)|

#### Digital Transfer Online Name

|Element|Digital Transfer Online Name|
|:-----|:------|
|Required|no|
|Type|string|
|Description|The name of the file|
|Entry Guidelines|Filename|
|Controlled Vocabulary|no|
|Example|alameda.shp|

#### Temporal Extent

|Element|Temporal Extent|
|:-----|:------|
|Required|no|
|Type|dateTime|
|Description|Date or date range for which the content of the resource is valid. Sometimes this is referred to as ground condition or date of situation.|
|Entry Guidelines| In ArcCatalog, use the calendar to input the year, month, and day for the date or date range. If day or month is unknown, use 01. If entering data outside of Arc, use the format: YYYY-MM-DDT00:00:00. <br/> If the ground condition date is unknown, use the publication date.|
|Controlled Vocabulary|no|
|Example|1984-01-01|

#### Thumbnail Preview

|Element|Thumbnail Preview|
|:-----|:------|
|Required|yes|
|Type|image|
|Description|Thumbnail preview|
|Entry Guidelines|A thumbnail preview image. In ArcGIS use the generate thumbnail tool to create a preview.|
|Controlled Vocabulary|no|
|Example|![Santa Cruz](https://github.com/kimdurante/metadataWorkflow/blob/master/images/thumbnail.jpg)|
