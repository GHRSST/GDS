# Document Conventions

The following sub-sections describe the notation conventions and data storage
types that are used throughout this GDS Technical Specification. Implementation
projects are expected to adhere to the nomenclature and style of the GDS in
their own documentation as much as possible to facilitate international
coordination of documentation describing the data products and services within
the GHRSST R/GTS framework.

## Use of text types
The text styles defined in {numref}`text_styles`  are used throughout the GDS.


```{table} Definition of text styles used in the GDS
:name: text_styles
**Text type**|**Meaning**|**Example**
-----|-----|-----
Liberation Mono|Denotes a variable name|`dt_analysis`
Liberation Mono|Denotes a netCDF attribute name|`gds_version_id`
Arial|Denotes regular text.|This is normal text.
```


## Use of colour in tables
The colours defined in {numref}`colour_styles` are used throughout the GDS.

<style>
    .cstyles-css tbody tr:nth-child(1) td:nth-child(3) { background: #b6bab7; }
    .cstyles-css tbody tr:nth-child(2) td:nth-child(3) { background: #42d1f5; }
    .cstyles-css tbody tr:nth-child(3) td:nth-child(3) { background: #dfadf7; }
    .cstyles-css tbody tr:nth-child(4) td:nth-child(3) { background: #f2f564; }
    .cstyles-css tbody tr:nth-child(5) td:nth-child(3) { background: #b5ebbb; }
    .cstyles-css tbody tr:nth-child(6) td:nth-child(3) { background: #f5c9d7; }
</style>

```{table} Storage type definitions used in the GDS
:name: colour_styles
:class: cstyles-css
**Colour**|**Meaning**|**Example**
:-----:|:-----:|:-----:
Grey|Denotes a table column name|`Variable`
Blue|Denotes a mandatory item|`analysed_sst`
Violet|Denotes an item mandatory for only certain situations|`dt_analysis`
Yellow|Denotes an optional item|experimental_field
Green|Denotes grid dimensions|`ni=1024`
Pink|Denotes grid variable dimensions|`float lat(nj, ni)`
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

