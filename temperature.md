---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Surface temperature variables

## Overview description of the GHRSST surface temperature variables

The minimum requirement for a GHRSST file is to include **at least one variable** containing sea surface temperature 
observations. This variable shall be named:
- `sea_surface_temperature` in the case of a sea surface temperature only field for any L2P, L3U, L3C or L3S product
- `analysed_sst` for the sea surface temperature field in a L4 product, where assimilation or interpolation is involved in the processing
- `surface_temperature` in the case of multi-category (sea, sea-ice and/or land) surface temperature, for any L2P, L3U or L3C product

Additional sea surface temperature variables can be provided in the same GHRSST products. They should be appended with a 
suffix identifying their specificity compared to the main sea surface temperature variable, using as far as possible standard
suffixes such as `skin`, `subskin`, `foundation`, `depth`, `adjusted`, for instance:
- `sea_surface_temperature_depth` : SST adjusted to a standard depth and local time
- `sea_surface_temperature_adjusted` : intercalibrated SST, adjusted to a given reference, in a multi-sensor product (L3S)
- `sea_surface_temperature_osisaf11` : SST calculated using an alternative algorithm (here OSISAF11 split-window)
- ...

Each sea surface temperature variable must clearly identify which water temperature it refers to, as defined by GHRSST in
{numref}`sst_definitions`. In conjunction with the NetCDF Climate and Forecast (CF) community the GHRSST Science Team 
agreed on the CF standard names for “SST” for each definition of sea surface temperature. The names were first included
in CF-1.3, and the current version of the standard name table can be found in the CF table of standard names 
[^footnote1]. They are summarized along with their key characteristics in {numref}`sst_types`:

```{table} GHRSST SST Type code and summary table
:name: sst_types
**GHRSST SST Type**|**CF Standard Name**|**Approximate Depth**|**Typically Observed by…**
-----|-----|-----|-----
SSTint|**<span style="font-family:courier;">sea\_surface\_temperature</span>**|0 meters|Not presently measureable
SSTskin|**<span style="font-family:courier;">sea\_surface\_skin\_temperature</span>**|10 – 20 micrometers|Infrared radiometers operating in a range of wavelengths form 3.7 to 12 micrometers
SSTsubskin|**<span style="font-family:courier;">sea\_surface\_subskin\_temperature</span>**|1 – 1.5 millimetres|Microwave radiometers operating in a range of frequencies from 6-11 gigahertz 
SSTdepth|**<span style="font-family:courier;">sea\_water\_temperature</span>**|Specified by vertical coordinate (e.g., SST5m)|In situ observing systems
SSTfnd|**<span style="font-family:courier;">sea\_surface\_foundation\_temperature</span>**|1-5 meters pre-dawn|In situ observing systems
SSTblend|None|Unknown|Blend of satellite and in situ observations
```

````{note}
for `SSTdepth`, the attribute `depth` should be used to indicate the depth for which the SST data are valid e.g.:
```
sea_surface_temperature:standard_name="sea_water_temperature";   
sea_surface_temperature:units = "K" ;   
sea_surface_temperature:depth = "1 metre" ;
``` 
````

(sea_surface_temperature)=
## sea surface temperature

```{list-table} Specifications of **<span style="font-family:courier;">sea_surface_temperature</span>** variable
:widths: 20 80
:name: spec_sea_surface_temperature

* - **Applicability**
  - L2P, L3U, L3C, L3S: Mandatory
* - **Science data type**
  - float
* - **Unit**
  - K (kelvin)
* - **Description**
  - Pixel sea surface temperature value
```

**Example:**

```{code-block}
---
caption: CDL for `sea_surface_temperature` variable in a L2P file
name: ex_sea_surface_temperature
---
dimensions:
	time = UNLIMITED ; // (1 currently)
	nj = 1080 ;
	ni = 2048 ;
variables:
    float sea_surface_temperature(nj, ni) ;
        sea_surface_temperature:_FillValue = 1e20 ;
        sea_surface_temperature:long_name = "sea surface subskin temperature" ;
        sea_surface_temperature:standard_name = "sea_surface_subskin_temperature" ;
        sea_surface_temperature:units = "K" ;
        sea_surface_temperature:depth = "1 millimeter" ;
        sea_surface_temperature:comment = "Temperature of the subskin of the ocean" ;
        sea_surface_temperature:coverage_content_type = "physicalMeasurement" ;
        sea_surface_temperature:coordinates = "lat lon" ;
```


(multi_category_sea_surface_temperature)=
## multi-category water temperature

