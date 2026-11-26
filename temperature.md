# Surface temperature variables

In conjunction with the NetCDF Climate and Forecast (CF) community the GHRSST Science Team agreed on the CF standard 
names for “SST” as 
detailed in {numref}`sst_definitions`. The names were first included in CF-1.3, 
and the current version of the standard name table can be found in the CF 
table of standard names [^footnote1]. In addition, the GHRSST 
Science Team agreed to use the CF Naming Convention for variable names that 
already exist as part of the CF Convention. CF definitions are used in the 
GDS and across GHRSST and are shown schematically in {numref}`sst_definitions` 
together with the relevant `<SST Type>` codes to be used in 
the filenames are provided.

The SST codes and CF standard names defined in {numref}`sst_definitions` and 
used within GHRSST are summarized along with their key characteristics in
{numref}`sst_types`.


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