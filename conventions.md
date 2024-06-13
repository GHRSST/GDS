# Document Conventions
The following sub-sections describe the notation conventions and data storage types that are used throughout this GDS Technical Specification. Implementation projects are expected to adhere to the nomenclature and style of the GDS in their own documentation as much as possible to facilitate international coordination of documentation describing the data products and services within the GHRSST R/GTS framework [RD-2]. {cite:ps}holdgraf_evidence_2014

## Use of text types
The text styles defined in {numref}`text_styles`  are used throughout the GDS.


```{table} Definition of text styles used in the GDS
:name: text_styles
**Text type**|**Meaning**|**Example**
-----|-----|-----
Bold Courier font|Denotes a variable name|**<span style="font-family:courier;">dt\_analysis</span>**
Bold Courier font|Denotes a netCDF attribute name|**<span style="font-family:courier;">gds\_version\_id</span>**
Arial|Denotes regular text.|This is normal text.
```


## Use of colour in tables
The colours defined in {numref}`colour_styles` are used throughout the GDS.

```{table} Definition of colour styles used in the GDS
:name: colour_styles
**Colour**|**Meaning**|**Example**
:-----:|:-----:|:-----:
Grey|Denotes a table column name|**<span style="font-family:courier;background-color:#b6bab7">Variable</span>**
Blue|Denotes a mandatory item|**<span style="font-family:courier;background:#42d1f5">analysed\_sst</span>**
Violet|Denotes an item mandatory for only certain situations|**<span style="font-family:courier;background:#dfadf7">dt\_analysis</span>**
Yellow|Denotes an optional item|**<span style="font-family:courier;background:#f2f564">experimental\_field</span>**
Green|Denotes grid dimensions|**<span style="font-family:courier;background:#b5ebbb">ni=1024</span>**
Pink|Denotes grid variable dimensions|**<span style="font-family:courier;background:#f5c9d7">float lat(nj, ni)</span>**
```

## Definitions of storage types
Computer storage types referred to in the GDS are defined in {numref}`storage_types` and follow those used in netCDF.

```{table} Storage type definitions used in the GDS
:name: storage_types
**Name**|**Storage Type**
:-----:|:-----:
byte|8 bit signed integer
short|16 bit signed integer
int (or long)|32 bit signed integer
float|32 bit floating point
double|64 bit floating point
string|Character string 
```

