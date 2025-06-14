---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

(l2p)=
# Level 2 Pre-processed (L2P) Product Specification

## Overview description of the GHRSST L2P data product

The GHRSST Level-2 Pre-processed (L2P) products are the basic building blocks 
from which all other GHRSST SST data products can be derived. L2P data products 
should ideally be made available within the GHRSST R/GTS framework to the user 
community in real time within 3 hours after the reception of data at the 
satellite.

L2P products include SST data as delivered by a data provider in their native 
format (swath for polar orbiting satellite), together with a number of 
ancillary fields that simplify interpretation and application of the SST data. 
The main difference between input L2 SST data file and the output GHRSST L2P 
data file is that additional confidence data and sensor specific error estimates
for each pixel value are included and the original SST data files are 
reformatted into the L2P specification. No adjustments to the input L2 SST 
measurements are allowed but instead, sensor specific error statistics are used 
to provide bias error and standard deviation estimates. A user wishing to 
correct L2P SST data can apply these estimates to the SST values directly. 
Full orbit input data files may be split into ascending and descending files or 
smaller granules and a unique L2P output may be generated for each file. 
The common format of L2P products allows data users to code with the security 
so that as new satellite derived SST data sets are brought on-line, very minimal
code changes are required to make full use of new L2P data. Time previously 
spent on coding different i/o routines for each satellite data set can now be 
spent applying the data to various applications and societal benefits instead. 

The GHRSST Science Team agreed at *the 6th GHRSST Science Team Meeting, Met 
Office, Exeter, United Kingdom, May 14th – 20th 2005*, 6 mandatory fields form 
the core data content of a GHRSST L2P data file. These fields will be known as 
**L2P ‘core’ (L2Pcore)** fields. In addition to global attributes and 
geo-location and time information, GHRSST producers must provide the following
L2Pcore fields within an L2P file:

- Sea Surface Temperature data (`sea_surface_temperature`)
- Time differences of SST measurements from a reference time (`sst_dtime`)
- SST Sensor Specific Error Statistic (SSES) measurement bias estimate 
  (`sses_bias`)
- SSES measurement standard deviation estimate (`sses_standard_deviation`)
- Flags specific to each L2P data set that help users interpret data 
  (`l2p_flags`) 
- A quality level for each measurement (`quality_level`)

In addition there are a number of auxiliary fields (**L2Paux**) that must be 
provided before the L2P data product is admitted into the GHRSST R/GTS:
- the difference between satellite SST measurements and a 
  defined reference climatology of SST (`dt_analysis`)
- An estimate of surface wind speed (`wind_speed`)
- An estimate of sea ice fraction (`sea_ice_fraction`)
- An estimate of atmospheric aerosol (as an aerosol dynamic indicator, 
  `aerosol_dyanamic_indicator`)

When an L2P file contains all L2Pcore and L2Paux fields together, it will be 
called a **full-L2P** file. Only full L2P data files should be registered 
into the GHRSST R/G TS central catalogue. These distinctions will assist in the 
data management of the GHRSST GDS-{{gds_version}}.

Missing L2Paux fields not provided by a producer may be added by a GHRSST 
distributor (DAC), if different from the producer, with prior arrangement. In 
this case data required the L2Paux files will be procured, checked for quality 
and interpolated or processed according to the GDS-{{gds_version}} specification
by the DAC. 

Optional experimental fields may be used by producers to provide additional 
information at their discretion. It may be necessary to use an additional 
netCDF coordinate variable when including experimental fields.

GDS-{{gds_version}} L2P data products are configured as shown in the table 
{numref}`l2p_content_summary`, which can be used to locate appropriate 
information in this document. 

```{table} Summary description of the contents of a GHRSST L2P data product
:name: l2p_content_summary

| netCDF File Contents | Description                                                                                               |
|----------------------|-----------------------------------------------------------------------------------------------------------|
| **Coordinate variables**  | Information to allow locating data on non-orthogonal grids, as defined in {numref}`coordinate_variables` | 
| **Data record variables** | Core and auxiliary variables as defined in {numref}`l2p_records`                                          | 
| **Global Attributes**     | A collection of required global attributes describing general characteristics of the file, as defined in section {numref}`global_attributes`  |
```

(l2p_records)=
## L2P data record format specification
The {numref}`l2p_variables` provides an overview of the GHRSST L2P 
product pixel data record that should be created for each input L2 SST 
measurement contained within a L2P file. In the following sections, each 
variable within the L2P data file is described in detail.

<style>
.l2p-variables-css tbody tr:nth-child(n+1):nth-child(-n+6) { background:#42d1f5; }
.l2p-variables-css tbody tr:nth-child(n+7):nth-child(-n+8) { background:#dfadf7; }
.l2p-variables-css tbody tr:nth-child(9) { background:#42d1f5; }
.l2p-variables-css tbody tr:nth-child(n+10):nth-child(-n+14) { background:#dfadf7; }
.l2p-variables-css tbody tr:nth-child(n+15):nth-child(-n+16) { background:#42d1f5; }
.l2p-variables-css tbody tr:nth-child(n+17):nth-child(-n+22) { background:#f2f564; }
</style>

```{table} Summary description of GHRSST L2P data records
:name: l2p_variables
:class: l2p-variables-css

| Variable Name          | Description            | Units  | Storage type |
|-----------------------|------------------------|--------|-----|
| [sea_surface_temperature](__l2p_sea_surface_temperature) | SST measurement values from input L2 satellite data set. | K (kelvin) | short |
| [sst_dtime](__l2p_sst_dtime) | The deviation in time of SST measurement from reference time | s (second)| short |
| [sses_bias](__l2p_sses_bias) | Sensor Specific Error Statistic (SSES) bias error | K (kelvin)| byte |
| [sses_standard_deviation](__l2p_sses_standard_deviation) | Sensor Specific Error Statistic (SSES) standard deviation uncertainty | K (kelvin)| byte |
| [dt_analysis](__l2p_dt_analysis) | The difference between input SST and a GHRSST L4 SST analysis from the previous 24 hour period | K (kelvin)| byte or short|
| [wind_speed](__l2p_wind_speed) | Closest (in time) 10 m surface wind speed from satellite or analysis  | m s-1 | byte |
| [wind_speed_dtime_from_sst](__l2p_wind_speed_dtime_from_sst) | Time difference of `wind_speed` data from input L2 SST measurement specified in hours.| h (hour) | byte |
| [source_of_wind_speed](__l2p_source_of_wind_speed) | Source(s) of `wind_speed` data. Mandatory when multiple sources used. | Code| byte |
| [sea_ice_fraction](__l2p_sea_ice_fraction) | Closest (in time) sea ice fraction from satellite or analysis | 1 | byte |
| [sea_ice_fraction_dtime_from_sst](__l2p_sea_ice_fraction_dtime_from_sst) | Time difference of `sea_ice_fraction` data from input L2 SST measurement specified in hours| h (hour)| byte |
| [source_of_sea_ice_fraction](__l2p_source_of_sea_ice_fraction) | Source(s) of `sea_ice_fraction` data | code | byte |
| [aerosol_dynamic_indicator](__l2p_aerosol_dynamic_indicator) | Atmospheric aerosol indicator | | byte |
| [adi_dtime_from_sst](__l2p_adi_dtime_from_sst) | Time difference between the `aerosol_dynamic_indicator` value and SST measurement | h (hour) | byte |
| [source_of_adi](__l2p_source_of_adi) | Source(s) of `aerosol_dynamic_indicator` data  | code | byte |
| [l2p_flags](__l2p_l2p_flags) | Data flag values | mask of bits | short |
| [quality_level](__l2p_quality_level) | Overall indication of L2P data quality | enum | byte |
| [satellite_zenith_angle](__l2p_satellite_zenith_angle) | Calculated satellite zenith angle (measured at the Earth's surface between the satellite and the zenith)| angular_degree | byte or short|
| [solar_zenith_angle](__l2p_solar_zenith_angle) | Calculated solar zenith angle (the angle between the local zenith and the line of sight to the sun, measured at the Earth's surface)| degree | byte |
| [surface_solar_irradiance](__l2p_surface_solar_irradiance) | Near contemporaneous surface solar irradiance| W m-2| byte |
| [ssi_dtime_from_sst](__l2p_ssi_dtime_from_sst) | Time difference between the `surface_solar_irradiance` value and SST measurement in hours | h (hour)| byte |
| [source_of_ssi](__l2p_source_of_ssi) | Source(s) of `surface_solar_irradiance` data | code | byte |
| [other fields](__l2p_optional_fields) | Optional/experimental fields defined by data provider | | |
```


(__l2p_sea_surface_temperature)=
### `sea_surface_temperature`

The variable `sea_surface_temperature` contains the native unmodified L2 SST 
of the input data file. L2 SST data are not adjusted in any manner and are 
identical to the input data set. 

The `sea_surface_temperature` variable shall be included in a L2P product 
with the format requirements shown in table 
{numref}`l2p_sea_surface_temperature`.

```{table} CDL example description of **<span style="font-family:courier;">sea_surface_temperature</span>** variable
:name: l2p_sea_surface_temperature

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| short             | `sea_surface_temperature` | Pixel sea surface temperature value | K (kelvin)   |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_sea_surface_temperature

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]sea_surface_temperature[(,:]'| sed 's/[[:space:]]//'
```

The standard_name attribute should be CF-1.7 or later compliant[^footnote1] as 
described in table {numref}`sst_standard_names`:

```{table} GHRSST short SST names and CF-1.7 standard names for sea_surface_temperature
:name: sst_standard_names
| GHRSST name | CF-1.7 standard name definitions      |
|-------------|---------------------------------------|
| SSTint      | `sea_surface_temperature`  |
| SSTskin     | `sea_surface_skin_temperature`  |                                                                                                                                                                                                                                                          |
| SSTsubskin  | `sea_surface_subskin_temperature`  |
| SSTfnd      | `sea_surface_foundation_temperature`   |
| SSTdepth    | `sea_water_temperature`  |
```

````{note}
for `SSTdepth`, the attribute `depth` should be used to indicate the depth for 
which the SST data are valid e.g.:
```
sea_surface_temperature:standard_name="sea_water_temperature";   
sea_surface_temperature:units = "K" ;   
sea_surface_temperature:depth = "1 metre" ;
``` 
````

(__l2p_sst_dtime)=
### `sst_dtime`

The deviation in time of SST measurement from reference time stored in the 
netCDF coordinate variable `time` (defined as the start time of granule for L2P). 
Minimum resolution should be one second.

The `sst_dtime` variable shall be included in a L2P product with the format 
requirements shown in table {numref}`l2p_sst_dtime`.

```{table} CDL example description of **<span style="font-family:courier;">sst\_dtime</span>** variable
:name: l2p_sst_dtime

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| short             | `sst_dtime` | Deviation from reference time stored in the coordinate variable, `time` | s (seconds) |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_sst_dtime

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]sst_dtime[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_sses_bias)=
### `sses_bias`

Providing uncertainty estimates for each SST measurement is one of the key user
requirements for GHRSST L2P SST data products. Uncertainty estimates allow users
to select the accuracy level suitable for their application and to make optimum
use of the SST observations (e.g. in data assimilation).

The uncertainties associated with each observation in a data stream are provided
as **Sensor Specific Error Statistic (SSES)**. The SSES are based on 
understanding the errors associated with the in-flight performance of an 
individual satellite instrument for the retrieval of SST from the measured 
radiances. The SSES are provided as a **mean bias error** and its associated 
**standard deviation** (in variable `sses_standard_deviation`, see 
{numref}`__l2p_sses_standard_deviation`).

There are a variety of methods for determining SSES as they depend on the
specific characteristics of each satellite instrument. Consequently, the L2P
provider can define their own scheme for producing SSES that is tailored to
their specific dataset. However, the SSES scheme must conform to a set of agreed
SSES common principles.

The SSES common principles are maintained on the 
[GHRSST website](https://www.ghrsst.org/resources/single-sensor-error-statistic-sses/), and
have been approved by the GHRSST Science Team. The L2P provider must provide
documentation that summarizes the theoretical basis of their SSES scheme, its
implementation, any recommendations for users, and its conformance to the agreed
SSES common principles.

The variable `sses_bias` is used to store SSES bias estimates and shall be
included with the L2P format requirements shown in {numref}`l2p_sses_bias`. Data
producers are reminded to choose appropriate `scale_factor` and `add_offset`
attributes for their data, and to strive for `scale_factor` as close to 0.01 as 
possible without “oversaturating” the values.


```{table} CDL example description of **<span style="font-family:courier;">sses_bias</span>** variable
:name: l2p_sses_bias

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|------------------|--------------|----------------------------------|----------|
| byte | sses_bias | SSES bias estimate | K (kelvin) |
```
```{code-cell}
:tags: [remove-input]
:name: l2p_sses_bias

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]sses_bias[(,:]' | sed 's/[[:space:]]//'
```


(__l2p_sses_standard_deviation)=
### `sses_standard_deviation`

**Sensor Specific Error Statistic (SSES) standard deviation** estimates are 
generated by the L2P data provider and are specific to a particular satellite 
instrument, and must conform to the SSES common principles. See 
{numref}`__l2p_sses_bias` for the general description of SSES concept and 
associated variables.

The variable `sses_standard_deviation` shall be included with the format
requirements shown in {numref}`l2p_sses_standard_deviation`.

Data producers are reminded to choose appropriate `scale_factors` and 
`add_offsets` for their data, and to strive for `scale_factors` as close to
0.01 as possible without “oversaturating” the values.


```{table} CDL example description of **<span style="font-family:courier;">sses_standard_deviation</span>** variable
:name: l2p_sses_standard_deviation

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | sses_standard_deviation | SSES standard deviation. | K (kelvin) |
```
```{code-cell}
:tags: [remove-input]
:name: l2p_sses_standard_deviation

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]sses_standard_deviation[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_dt_analysis)=
### `dt_analysis`

The difference between input SST and a GHRSST L4 SST analysis from the 
previous 24 hour period.  If storage as byte 
does not allow the provider to offer the full precision required for this 
field,  storage as a short is optionally permitted though byte is preferred. 

The L2P variable `dt_analysis` is the temperature difference between an input
L2 SST measurement and a reference SST L4 analysis data set. `dt_analysis` may
be used to indicate potential areas of diurnal variability or gross outliers in
the L2 input SST measurement data set by looking for large deviations from the
previous analysis SST data. Note that `dt_analysis` is an indicator field and
the temperature anomalies may be difficult to interpret in regions of high SST
gradients. Furthermore, interpretation requires a good understanding of the
strengths and weaknesses (e.g. space and time de-correlations) of the chosen
reference L4 analysis system.

`dt_analysis` shall be derived using:

```{math}
:label: eq_dt_analysis
dt\_analysis = SST_{input} – L4_{SST}
```

Where SST<sub>input</sub> is the input satellite L2 measurement and L4<sub>
SST</sub> is a previous day analysis from a GHRSST L4 System selected by the
data provider. The GHRSST L4 analysis chosen for a given L2P data set variable 
should be consistent for all L2P products as far as practically possible. If a 
previous analysis SSTfnd data file is not available for use in 
{eq}`eq_dt_analysis`, then a mean reference SST or climatology should be 
used in its place as defined in {numref}`l2p_dt_analysis_code`.

```{table} Reference SST data sets for use in dt_analysis computation
:name: l2p_dt_analysis_code
| Name                      | Description                                                                                                                                      | Reference                                                              |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Use code from L4 analysis | The mean SSTfnd computed for a n-1 day period. This product is computed from data provider SSTfnd data products in real time each day             | https://www.ghrsst.org/ghrsst-data-services/ghrsst-catalogue/          |
| GMPE_GLOBAL               | Daily, 25 km median average SST and sea ice product created using 10 operational SST analysis products from operational centres around the world | https://ghrsst-pp.metoffice.gov.uk/ostia-website/gmpe-monitoring.html  |
```

The `dt_analysis` value shall be inserted into the `dt_analysis` field of
the L2P product for the pixel in question as described 
{numref}`l2p_dt_analysis`.


```{table} CDL example description of **<span style="font-family:courier;">dt_analysis</span>** variable
:name: l2p_dt_analysis

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte or short | dt_analysis | Deviation from previous day (T-1) L4 SSTfnd analysis as defined in the {numref}`l2p_dt_analysis_code`. If no analysis is available, the reference mean SST climatology should be used| K (kelvin) |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_dt_analysis

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]dt_analysis[(,:]'| sed 's/[[:space:]]//'
```

```{note}
The `reference` variable attribute should be used to specify the analysis or 
climatology used to compute `dt_analysis` as shown in the example above 
following the guidelines in {numref}`l2p_dt_analysis_code`.
```


(__l2p_wind_speed)=
### `wind_speed`

The L2P variable `wind_speed` contains a best estimate of the **10m surface
wind speed, ideally at the time of SST data acquisition** (although this is
rarely possible). Wind speed measurements are required within the GDS as an
indicator of the turbulent state of the air sea interface to interpret the
relationship between satellite and subsurface SST data and assess the severity
of any skin SST temperature deviation, thermal stratification and for use in
diurnal variability adjustment schemes. At low wind speeds, especially in clear
sky conditions, stronger diurnal variability is expected leading to higher
surface layer temperature gradients and the potential for significant
de-coupling of the skin/sub-skin SST from the SST at depth.

Ideally a near contemporaneous wind speed measurement from satellite sensors
should be used but this is impossible for all sensors due to the limited number
of satellite wind speed sensors available. As a surrogate for a measured wind
speed value, analysis product estimates (e.g., from numerical weather prediction
models) may be used as an indication of the surface wind speed. The GDS
specifies the following rules:

> Simultaneous microwave 10m wind speed measurements obtained from the same
> instrument providing the SST measurement shall be used when available to set the
> L2P confidence data variable `wind_speed`.
> In the absence of a simultaneous surface wind speed measurement, an analysis
> product estimated 10m surface wind speed shall be used to set the L2P variable 
> `wind_speed`.

The difference in time expressed in hours between the time of SST measurement
and the time of wind speed data should be entered into the L2P confidence data
variable `wind_speed_dtime_from_sst` as described in 
{numref}`__l2p_wind_speed_dtime_from_sst`. In the case of an analysis field, 
this should be the central (mean) time of an integrated value.
If all of the wind speeds have a single time value, as in the case of an
analysis or model that gives the wind speeds at an instant in time, then the 
`wind_speed_dtime_from_sst` variable is not needed and instead a variable level
attribute named `time_offset` is used. The attribute `time_offset` should
store the difference in hours between the `wind_speed` and the reference time,
stored in the variable `time`.

If a single source of data is used in the L2P variable `wind_speed` 
(recommended), the L2P variable `source_of_wind_speed` is not required and a 
`source` variable attribute of `wind_speed` is sufficient. In that case, it 
shall be a single source text string defined by the data provider using the text
string naming best practice given in {numref}`product_codes`.

If multiple sources of data are used, source information should be indicated in
the L2P variable `source_of_wind_speed` as defined by the data provider and as
described in detail in {numref}`__l2p_source_of_wind_speed`, and the 
`source` variable attribute of `wind_speed` shall have the value 
`source_of_wind_speed`. In addition, the units of all sources used in the file 
shall be identical.

The GDS L2P variable `wind_speed` shall be included in L2P products
with the format requirements shown in the {numref}`l2p_wind_speed`.

```{table} CDL example description of **<span style="font-family:courier;">wind_speed</span>** variable
:name: l2p_wind_speed

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | wind_speed | Surface wind speed at 10m height. Resolution should be no less than 1 m s-1 | m s-1 |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_wind_speed

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]wind_speed[(,:]'| sed 's/[[:space:]]//'
```

A single source of wind data is shown in this example which is reported as 
`wind_speed:source = "ECMWF_Anaylsis_V2"` the code has been defined by the data
provider using the ancillary data naming rules given in {numref}`product_codes`. 
Since all of the wind speeds have the same time, the attribute `time_offset` is
used instead of the variable `wind_speed_dtime_from_sst`.

(__l2p_wind_speed_dtime_from_sst)=
### `wind_speed_dtime_from_sst`

The variable `wind_speed_dtime_from_sst` reports the time difference between
wind speed data and SST measurement in hours. The variable 
`wind_speed_dtime_from_sst` shall be included with the format requirements
shown in {numref}`l2p_wind_speed_dtime_from_sst`. In the
case of an analysis field, the central (mean) time of an integrated value should
be used. If all values are the same, this variable is not required.
Instead, use the variable level attribute named `time_offset` with the
variable `wind_speed`.

```{table} CDL example description of **<span style="font-family:courier;">wind_speed_dtime_from_sst</span>** variable
:name: l2p_wind_speed_dtime_from_sst

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `wind_speed_dtime_from_sst` | This variable reports the time difference of wind speed measurement from SST measurement in hours. | h (hour) |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_wind_speed_dtime_from_sst

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]wind_speed_dtime_from_sst[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_source_of_wind_speed)=
### `source_of_wind_speed`

The source of data used to set the L2P ancillary data variable `wind_speed`
shall be indicated in the L2P variable `source_of_wind_speed` when more than
one source of wind speed data is used in the L2P product. 

When only one source is used, this variable is not needed and the appropriate 
text string indicating the source is placed in the `source` attribute of the 
`wind_speed` variable. If the values in  that single source all have the same 
time, then a variable attribute `time_offset` set as the difference time in 
hours is considered sufficient and the variable `wind_speed_dtime_from_sst` 
is not required. 

For multiple sources, the GDS-{{gds_version}} requires the following:

- The variable in question should contain an attribute called `flag_meanings`
  and another one called `flag_values`. The `flag_values` attribute shall
  contain a comma-separated list of the numeric codes for the sources of data
  used whose order matches the comma-separated text strings in the 
  `flag_meanings` attribute.
- These text strings and numeric codes do not need to be unique across different
  data sets or even ancillary variables, but must be consistent within a given
  variable and clearly specified within each netCDF variable and its attributes.
  A best practice for naming the text strings in provided in  
  {numref}`product_codes`.
- instead of using a `_FillValue` attribute and value for missing data, it is 
  recommended to set missing pixel values to **0** and add the corresponding 
  **no_data** meaning in `flag_meanings` attribute.

The variable `source_of_wind_speed` shall conform to the format requirements
shown in the {numref}`l2p_source_of_wind_speed`.


```{table} CDL example description of **<span style="font-family:courier;">source_of_wind_speed</span>** variable
:name: l2p_source_of_wind_speed

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `source_of_wind_speed` | Sources of `wind_speed` values. | code |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_source_of_wind_speed

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]source_of_wind_speed[(,:]'| sed 's/[[:space:]]//'
```

In this example, `flag_meanings` and `flag_values` contain strings and
numeric codes provided by the data provider according to the best practices
specified in {numref}`l2p_source_of_wind_speed`.

(__l2p_sea_ice_fraction)=
### `sea_ice_fraction`

Some SST data are contaminated in part or wholly by sea ice and the L2P variable
`sea_ice_fraction` is used to quantify the fraction of an area contaminated
with sea ice, ranging from 0 to 1. Some input SST data streams provide a 
flag to indicate that the SST measurement is contaminated by sea ice 
(e.g., passive microwave radiometers such as AMSR-E).

If an input data set pixel fractional sea ice estimate exists, this should be
used to in the L2P variable `sea_ice_fraction` as described in the
table {numref}`l2p_sea_ice_fraction`.

Best practice suggests that one should approach the issue in the following
way. If an input data set pixel sea ice flag does not exist, and the pixel is
located in or close to a region that may be ice contaminated, a reference sea
ice data set should be used to determine the value of the L2P variable 
`sea_ice_fraction`.

If an input data set pixel sea ice flag exists (i.e. indicating sea ice but
not the fractional amount of coverage), this should be used to set the L2P
variable `sea_ice_fraction` to 1.

If the SST input data set includes a sea ice flag in the data stream, bit 3 of
the L2P confidence data variable `l2p_flags` should be set for this pixel as
described in {numref}`__l2p_l2p_flags`.

The difference in time expressed in hours between the time of SST measurement
and the time of sea ice fraction measurement should be entered into the L2P
variable `sea_ice_fraction_dtime_from_sst` as described in 
in {numref}`__l2p_sea_ice_fraction_dtime_from_sst`. In the case of an
analysis field, this should be the central (mean) time of an integrated value.
If all ice observations have a single time value, as in the case of an
analysis or model that gives the sea ice values at an instant in time, then the
`sea_ice_fraction_dtime_from_sst` variable is not needed and instead a
variable attribute named `time_offset` is used. The attribute `time_offset` 
should store the difference in hours between the `sea_ice_fraction`
and the reference time, stored in the variable `time`.

If a single source of data is used in the L2P variable `sea_ice_fraction`, the
L2P variable `source_of_sea_ice_fraction` is not required and instead the 
`source` variable attribute value of `sea_ice_fraction` is sufficient. It shall 
be a single source text string defined by the data provider using the text 
string naming best practice given in {numref}`product_codes`.

If multiple sources of data are used, source information should be indicated in
the L2P variable `source_of_sea_ice_fraction` as defined by the data provider
and as described in detail in {numref}`__l2p_source_of_sea_ice_fraction`, and 
the `source` variable attribute of `sea_ice_fraction` shall have the value 
`source_of_sea_ice_fraction`. In addition, the units of all sources used in the 
file shall be identical.

The variable attribute `sea_ice_treatment` shall specify how
the sea ice information has been treated by the data provider. Valid options
are: *"Use unmodified (one source)"*, *"use unmodified (multiple ice sources)”*,
or *“modified using onboard sensors"*.

The variable `sea_ice_fraction` will be included with the format requirements
shown in {numref}`l2p_sea_ice_fraction`.

```{table} CDL example description of **<span style="font-family:courier;">sea_ice_fraction</span>** variable
:name: l2p_sea_ice_fraction

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `sea_ice_fraction` | fractional of sea ice contamination in a given pixel. Ranges from 0 to 1. | 1 (unitless) |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_sea_ice_fraction

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]sea_ice_fraction[(,:]'| sed 's/[[:space:]]//'
```

A single source of sea ice fraction data is shown in this example which is
reported as `sea_ice_fraction:source = "REMSS_AMSRE_V5"` following the
ancillary data naming conventions specified in {numref}`product_codes`. Since 
all of ice values have the same time, the attribute `time_offset` is used 
instead of the variable `sea_ice_fraction_dtime_from_sst`.

(__l2p_sea_ice_fraction_dtime_from_sst)=
### `sea_ice_fraction_dtime_from_sst`

The variable `sea_ice_fraction_dtime_from_sst` reports the time difference
between sea ice fraction data from SST measurement in hours. This variable is 
mandatory when multiple sources of `sea_ice_fraction` are used. 

If only one source is used, simply set a variable attribute `time_offset` in 
`sea_ice_fraction` variable, as the difference time in hours.

The variable `sea_ice_fraction_dtime_from_sst` shall be included with the format
requirements shown {numref}`l2p_sea_ice_fraction_dtime_from_sst`.

In the case of an analysis field, this should be the central (mean) time of an
integrated value. If all of the values are the same, this variable is not
required. Instead, use the variable level attribute named `time_offset` with
the variable `sea_ice_fraction`. The attribute `time_offset` should store
the difference in hours between the sea ice analysis time and the reference 
time, stored in the variable `time`.

```{table} CDL example description of **<span style="font-family:courier;">sea_ice_fraction_dtime_from_sst</span>** variable
:name: l2p_sea_ice_fraction_dtime_from_sst

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `wind_speed_dtime_from_sst` | This variable reports the time difference between sea ice fraction data from SST measurement in hours. | hour |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_sea_ice_fraction_dtime_from_sst

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]sea_ice_fraction_dtime_from_sst[(,:]'| sed 's/[[:space:]]//'
```

This variable is mandatory when multiple sources for `sea_ice_fraction` are 
used. If only one source is used, instead simply set a variable attribute 
`sea_ice_fraction:sea_ice_fraction_dtime_from_sst = \<difference time in
hours\>`.

(__l2p_source_of_sea_ice_fraction)=
### `source_of_sea_ice_fraction`

The source of data used to set the L2P ancillary data variable 
`sea_ice_fraction` shall be indicated in the L2P variable 
`source_of_sea_ice_fraction` when more than one source of sea ice fraction data
is used in the L2P product. 

When only one source is used, this variable is not needed and the appropriate 
text string indicating the source is placed in the source attribute of the 
`sea_ice_fraction` variable. 

For multiple sources, the GDS-{{gds_version}} requires the following:
- The variable in question should contain an attribute called `flag_meanings` 
  and another one called `flag_values`. The `flag_values` attribute shall 
  contain a comma-separated list of the numeric codes for the sources of data 
  used whose order matches the comma-separated text strings in the 
  `flag_meanings` attribute.
- These text strings and numeric codes do not need to be unique across 
  different data sets or even ancillary variables, but must be consistent 
  within a given variable and clearly specified within each netCDF variable 
  and its attributes. A best practice for naming the text strings in 
  provided in {numref}`product_codes`.
- Instead of using a `_FillValue` attribute and value for missing data, it is 
  recommended to set missing pixel values to **0** and add the corresponding 
  **no_data** meaning in `flag_meanings` attribute.

The variable `source_of_sea_ice_fraction` shall conform to the format requirements 
shown in {numref}`l2p_source_of_sea_ice_fraction`.


```{table} CDL example description of **<span style="font-family:courier;">source_of_sea_ice_fraction</span>** variable
:name: l2p_source_of_sea_ice_fraction

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `source_of_sea_ice_fraction` | Source(s) of sea ice values | None |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_source_of_sea_ice_fraction

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]source_of_sea_ice_fraction[(,:]'| sed 's/[[:space:]]//'
```

In this example, `flag_meanings` and `flag_values` contain strings and
numeric codes provided by the data provider according to the best practices
specified in {numref}`product_codes`.

(__l2p_aerosol_dynamic_indicator)=
### `aerosol_dynamic_indicator`

**Mandatory (only for infrared instruments).**

The L2P variable `aerosol_dynamic_indicator` contains an indicator of potential
atmospheric aerosol contamination of infrared satellite SST data.
Infrared-absorbing atmospheric aerosols are a major source of error in
satellite-derived sea surface temperature retrievals. Atmospheric aerosol, such
as Saharan dust outbreaks, volcanic eruptions or from coastal mega cities causes
errors in the atmospheric correction of top of the atmosphere radiances when
retrieving SST from infrared and visible band data sets. A systematic bias in
the tropical North Atlantic Ocean and Arabian Sea due to desert dust outflows in
those regions is apparent.

An aerosol indicator (e.g., derived from satellite measurements or models) 
value is assigned to the L2P variable `aerosol_dynamic_indicator` for each 
corresponding infrared retrieved SST measurement pixel using data chosen 
by the data provider to indicate aerosol contamination. The aerosol 
indicator data nearest in space and time to the input pixel SST value 
should  be used. In the case of microwave SST measurements there is no
requirement to include the `aerosol_dynamic_indicator` L2P variable as 
microwave SST retrievals are not affected by atmospheric aerosols. However,
microwave SST data providers may include `aerosol_dynamic_indicator` in an 
L2P product.

If a single source of data is used in the L2P variable 
`aerosol_dynamic_indicator`, the L2P variable `source_of_adi` is not 
required and instead the `source` variable attribute value in 
`aerosol_dynamic_indicator` is sufficient. It shall be a single source 
text string defined by the data provider using the text string naming best 
practice given in {numref}`product_codes`. If all the times have the same 
value, then using a variable attribute `time_offset` with variable 
`aerosol_dynamic_indicator` is sufficient and the variable 
`adi_dtime_from_sst` is not required.

If multiple sources of ADI information are used then, the `source` 
variable attribute of `aerosol_dynamic_indicator` variable shall have the 
value `source_of_adi`. In addition, the units of all sources used in the 
file shall be identical. 

The difference in time expressed in hours between the time of SST measurement
and the time of aerosol indicator data should be entered into the L2P variable 
`adi_dtime_from_sst` as described in {numref}`__l2p_adi_dtime_from_sst`. In 
the case of an analysis field, this should be the central (mean) time of an 
integrated value.

If the variable `aerosol_dynamic_indicator` is provided in an L2P product,
it shall be included with the format requirements shown in the 
{numref}`l2p_aerosol_dynamic_indicator`.

```{table} CDL example description of **<span style="font-family:courier;">aerosol_dynamic_indicator</span>** variable
:name: l2p_aerosol_dynamic_indicator

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `aerosol_dynamic_indicator` | Indicator of potential aerosol contamination of infrared satellite data | Provider defined |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_aerosol_dynamic_indicator

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]aerosol_dynamic_indicator[(,:]'| sed 's/[[:space:]]//'
```

A single source of `aerosol_dynamic_indicator` has been used in this example
indicated using the `aerosol_dynamic_indicator:source` and are defined by the
data provider using the ancillary data naming best practice given in 
{numref}`product_codes`. Since all of the values have the same time, the 
attribute `time_offset` is used instead of the variable 
`aerosol_sst_dtime_from_sst` to indicate the offset in hours from the
reference variable `sst_dtime`.


(__l2p_adi_dtime_from_sst)=
### `adi_dtime_from_sst`

The variable adi_dtime_from_sst reports the time difference between aerosol
indicator data from input L2 SST measurement in hours. The variable
`adi_dtime_from_sst` shall be included in L2P products with the format
requirements shown in the {numref}`l2p_adi_dtime_from_sst`. In
the case of an analysis field, this should be the central (mean) time of an
integrated value. If all of the values are the same, this variable is not
required. Instead, use the variable level attribute named `time_offset` with
the variable `aerosol_dynamic_indicator`.

```{table} CDL example description of **<span style="font-family:courier;">adi_dtime_from_sst</span>** variable
:name: l2p_adi_dtime_from_sst

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `adi_dtime_from_sst` | Time difference of aerosol dynamic indicator data from SST measurement in hours | hour |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_adi_dtime_from_sst

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]sea_ice_fraction_dtime_from_sst[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_source_of_adi)=
### `source_of_adi`

The source of data used to set the L2P ancillary data variable 
`aerosol_dynamic_indicator` shall be indicated in the L2P variable
`source_of_adi` when more than one source of SSI data is used in the L2P
product. 

When only one source is used, this variable is not needed and the
appropriate text string indicating the source is placed in the sources attribute
of the `aerosol_dynamic_indicator` variable. 

For multiple sources, The variable in question should contain an attribute 
called `flag_meanings` and another one called `flag_values`. The 
`flag_values` attribute shall contain a comma-separated list of the numeric 
codes for the sources of data used whose order matches the space-separated text 
strings in the `flag_meanings` attribute. These text strings and numeric 
codes do not need to be unique across different data sets or even ancillary 
variables, but must be consistent within a given variable and clearly 
specified within each netCDF variable and its attributes. A best practice 
for naming the text strings in provided in {numref}`product_codes`.

Instead of using a `_FillValue` attribute and value for missing data, it is 
recommended to set missing pixel values to **0** and add the corresponding 
**no_data** meaning in `flag_meanings` attribute.

The variable `source_of_adi` shall conform to the with the format requirements
shown in the {numref}`l2p_source_of_adi`.

```{table} CDL example description of **<span style="font-family:courier;">source_of_adi</span>** variable
:name: l2p_source_of_adi

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `source_of_adi` | Sources of aerosol dynamic indicator values | None |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_source_of_adi

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]source_of_adi[(,:]'| sed 's/[[:space:]]//'
```

In this example, `flag_meanings` and `flag_values` contain strings and numeric 
codes provided by the data provider according to the best practices specified
in {numref}`product_codes`.

(__l2p_l2p_flags)=
### `l2p_flags`

**Mandatory.**

The GDS-{{gds_version}} L2P variable `l2p_flags` is used to 
- Specify the type of input SST data (either infrared or passive microwave
  instrument derived),
- Pass through native flags from the input L2 SST data set and
- Record any additional information considered important for the user of an L2P
  data set.

The L2P variable `l2p_flags` holds Boolean (single bit) codes detailed in its
`flag_meanings` and `flag_masks` attributes, and split into two sections:

- The first 6 bits of the L2P variable `l2p_flags` are generic flags that are
  common to all L2P data files as defined in the {numref}`l2p_flags_bits`
- Bits 6-15 are defined by the L2P data provider and are specific to each L2
  input data stream


```{table} List of bits composing the **<span style="font-family:courier;">l2P_flags</span>** variable
:name: l2p_flags_bits

| Bit  | Common flags | 
|------|--------------|
| 0    | Set if passive microwave data (not set is assumed to be infrared) |
| 1    | Set if over land (not set is assumed to be ocean) |
| 2    | Set if pixel is over ice |
| 3    | Set if pixel is over a lake (if known) |
| 4    | Set if pixel is over a river (if known) |
| 5    | Reserved for future data |
| 6-15 | Defined by L2 data provider |
```

The `flag_meanings` attribute shall contain a space-separated list of 
(string with no space) descriptions for each distinct flag value. For 
descriptions containing multiple words, the words shall be linked 
by underscores.

The `flag_masks` attribute shall contain a comma-separated list of (numeric)
mask values that isolate the bit or bits that encode each flag value, whose
order matches that of the `flag_meanings` values. 

It is recommended not to use `_FillValue` attribute as it is prone to 
misinterpretation of the bit mask.

- **Bit 0** of the L2P `l2p_flags` is used to record if an input pixel SST is
  derived from an infrared satellite sensor or a passive microwave sensor. If 
  an input pixel is derived from a passive microwave sensor, bit 0 of the L2P
  `l2p_flags` variable should be set to 1. By not setting this flag the pixel is
   assumed to be from an infrared sensor.
- **Bit 1** of the L2P `l2p_flags` variable is used to record if an input 
  pixel is over land or ocean surfaces. If an input pixel is classified as 
  land covered bit 1 of the L2P `l2p_flags` variable should be set to equal 1. 
  By not setting this flag the pixel is assumed to be classified as over ocean.
- **Bit 2** of the L2P `l2p_flags` variable is used to record if an input pixel 
  records ice contamination. If an input pixel is classified as ice 
  contaminated bit 2 of the L2P `l2p_flags` variable should be set to 1.
- **Bit 3** of the L2P `l2p_flags` variable is used to record if an input pixel 
  contains any part of a lake, as defined by the GHRSST definition of lakes 
  (mask). If an input pixel contains any part of a lake, as defined by the 
  GHRSST definition of lakes (mask), bit 3 of the L2P `l2p_flags` variable 
  should be set to 1.
- **Bit 4** of the L2P `l2p_flags` variable is optionally used to record if an 
  input pixel contains any part of a river, as defined by the GHRSST 
  definition of rivers (mask). If an input pixel contains any part of a 
  river, as defined by the GHRSST definition of rivers (mask), bit 4 of the 
  L2P `l2p_flags` variable should be set to 1.

Flags or other information provided with the input L2 SST data should be defined
and assigned to the `l2p_flags` variable using bits 6-15 of the L2P variable
l2p_flags. It is recommended to use single bits for any information, no
combination of multiple bits. If that is not possible, then an additional
experimental byte field should be used instead. Definitions for bits 6-15, if
used, should be given using the variable comment attribute.

The L2P variable `l2p_flags` shall be included in GDS-{{gds_version}} L2P 
data files with the format requirements shown in {numref}`l2p_l2p_flags`.

```{table} CDL example description of **<span style="font-family:courier;">source_of_adi</span>** variable
:name: l2p_l2p_flags

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| short | `l2p_flags` | The variable l2p_flags is used to <br> (a) specify the type of input SST data (either infrared or passive microwave instrument derived), <br> (b) pass through native flags from the input L2 SST data set and <br> (c) record any additional information considered important for the user of an L2P data set | None |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_source_of_adi

!ncdump -h samples/l2p_full_example.nc | grep $'[, \t]l2p_flags[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_quality_level)=
### `quality_level`

**Mandatory.**

The L2P variable `quality_level` provides an indicator of the overall quality
of an SST measurement in an L2P file. The GDS requires the following:

The L2P variable `quality_level` shall use an incremental scale from **0 to 
5** to provide the user with an indication of the quality of the L2P SST data, 
reflecting the CEOS QA4EO (Quality Indicator) guidelines. The value **0** 
shall be used to indicate missing data and the value **1** shall be used to 
indicate invalid data (e.g. cloud, rain, too close to land - under no conditions
use this data). The remaining values from **2-5** are set at the discretion of 
the L2P provider with the proviso that the value **2** shall be used to 
indicate the worst quality of usable data and the value **5** shall be used to 
indicate the best quality usable data. The L2P provider is required to provide 
a description of the quality levels provided as part of the product 
documentation.

The L2P variable `quality_level` reflects the quality of SST data from a 
single sensor and does not provide an indication of the relative quality 
between sensors.

The L2P variable `quality_level` shall be included with the format 
requirements shown in the {numref}`l2p_quality_level`.

We recommend not to use the `_FillValue` attribute but rather to use the 
value **0** to fill in missing data pixels.

```{table} CDL example description of **<span style="font-family:courier;">quality_level</span>** variable
:name: l2p_quality_level

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `quality_level` | Overall indicator of SST measurement quality | n/a  |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_quality_level

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]quality_level[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_satellite_zenith_angle)=
### `satellite_zenith_angle`

**Optional.**

Sea surface temperature retrievals from satellite instruments degrade as the
sensor zenith angle increases. Measurements made with high viewing angles
relative to nadir appear to be considerably colder than they are in reality. The
L2P variable `satellite_zenith_angle` contains the calculated satellite zenith
angle (measured at the Earth's surface between the satellite and the zenith) for
the input L2 SST based on the satellite geometry at the time of SST data
acquisition.

The GDS L2P variable `satellite_zenith_angle` is an optional field that may be
provided by a data provider. The satellite zenith angle for each input pixel 
measurement should be recorded in the L2P variable `satellite_zenith_angle` 
having a range of 0° to +90°.

If the L2P variable `satellite_zenith_angle` is included in a L2P data product 
it shall conform to the format requirements shown in 
{numref}`l2p_satellite_zenith_angle`.

```{table} CDL example description of **<span style="font-family:courier;">satellite_zenith_angle</span>** variable
:name: l2p_satellite_zenith_angle

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte or short | `satellite_zenith_angle` | Calculated satellite zenith angle (measured at the Earth's surface between the satellite and the local zenith) for the input L2 SST based on the satellite geometry at the time of SST data acquisition. <br> Ranges from 0 to 90 degrees.| angular_degree  |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_satellite_zenith_angle

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]satellite_zenith_angle[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_solar_zenith_angle)=
### `solar_zenith_angle`

**Optional.**

The L2P variable `solar_zenith_angle` contains the calculated solar zenith
angle (the angle between the local zenith and the line of sight to the sun,
measured at the Earth's surface) for the input L2 SST based on the satellite
geometry at the time of SST data acquisition. Solar zenith angle is a function
of time, day number and latitude.

The GDS L2P variable `solar_zenith_angle` is an optional field that may be
provided by a data provider. The solar zenith angle for each input pixel 
measurement should be recorded in the L2P variable `solar_zenith_angle` having 
a range of 0° to 180°. If the L2P variable `solar_zenith_angle` is included in 
a L2P data product it shall conform to the format requirements shown in 
{numref}`l2p_solar_zenith_angle`.


```{table} CDL example description of **<span style="font-family:courier;">solar_zenith_angle</span>** variable
:name: l2p_solar_zenith_angle

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte or short | `solar_zenith_angle` | Calculated solar zenith angle (measured at the Earth's surface between the sun and the local zenith) for the input SST based on the solar geometry at the time of SST data acquisition. <br> Ranges from 0 to 180 degrees.| angular_degree  |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_solar_zenith_angle

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]solar_zenith_angle[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_surface_solar_irradiance)=
### `surface_solar_irradiance`

**Optional.**

Surface Solar Irradiance (SSI) data were originally required within the GDS 1.6
to assess the magnitude and variability of significant diurnal SST variations,
for use in diurnal variability correction schemes, for use in L4 SST analysis
procedures and to interpret the relationship between satellite and in situ SST
data. In the GDS-{{gds_version}}, it is an optional variable. Ideally a near 
contemporaneous SSI measurement from satellite sensors should be used but this 
is impossible for all areas due to the limited number of geostationary satellite
sensors available. As a surrogate for a measured SSI value, analysis estimates 
may be used.

Surface solar Irradiance (SSI) data may be assigned to each L2P SST measurement
pixel using the variable `surface_solar_irradiance`. 

An integrated down-welling SSI measurement (e.g., derived from satellite
measurements) should be assigned to each SST pixel value using the 
`surface_solar_irradiance` L2P variable. The SSI measurement nearest in space
and time before the input pixel SST value should be used. If no SSI measurement
is available, an integrated SSI value derived from an analysis system nearest in
space and time to the SST measurement should be used to set the value of 
`surface_solar_irradiance`.

The difference in time expressed in hours between the time of SST measurement
and the time of surface solar irradiance data should be entered into the L2P
confidence data variable `ssi_dtime_from_sst`. In the case of an analysis
field, this should be the central (mean) time of an integrated value. If all of
the values have the same time, the attribute `time_offset` is used instead of
the variable `ssi_dtime_fraction_dtime_from_sst`. The attribute `time_offset`
should store the difference in hours between the `surface_solar_irradiance`
and the reference time, stored in the variable `time`.

If a single source of data is used in the L2P variable 
`surface_solar_irradiance`, the L2P variable `source_of_ssi` is not required
and instead the `surface_solar_irradiance:source` attribute value is sufficient.
It shall be a single source text string defined by the data provider using the 
text string naming best practice given in {numref}`product_codes`.

If multiple sources of data are used, source information should be indicated in 
the L2P variable `source_of_ssi` as defined by the data provider and as 
described in detail in {numref}`l2p_surface_solar_irradiance`. Then,
the `surface_solar_irradiance:source` attribute shall have the value 
`source_of_ssi`.

The L2P variable `surface_solar_irradiance` may be included by a data provider 
with the format requirements shown in {numref}`l2p_surface_solar_irradiance`.


```{table} CDL example description of **<span style="font-family:courier;">surface_solar_irradiance</span>** variable
:name: l2p_surface_solar_irradiance

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `surface_solar_irradiance` | Near contemporaneous integrated Surface Solar Irradiance (SSI) data. | $W m^{-2}$ |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_surface_solar_irradiance

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]surface_solar_irradiance[(,:]'| sed 's/[[:space:]]//'
```

A single source of SSI data is shown in this example which is reported as
`surface_solar_irradiance:source = "SSI-MSG_SEVIRI-V1"` The text string has been
defined by the data provider using the text string naming best practice given
in {numref}`product_codes`. Since all of the SSI values have the same time, the
attribute `time_offset` is used instead of the variable `ssi_dtime_from_sst`.


(__l2p_ssi_dtime_from_sst)=
### `ssi_dtime_from_sst`

**Optional (Mandatory only if multiple observation time for 
`surface_solar_irradiance` are provided).**

The variable `ssi_dtime_from_sst` reports the time difference between SSI data
from SST measurement in hours. The variable `ssi_dtime_from_sst` shall be
included with the format requirements shown in {numref}`l2p_ssi_dtime_from_sst`.

In the case of an analysis field, the central (mean) time of an integrated value
should be used.

If all of the values are the same, this variable is not required. Instead, use
the variable level attribute named `time_offset` with the variable 
`surface_solar_irradiance`.


```{table} CDL example description of **<span style="font-family:courier;">ssi_dtime_from_sst</span>** variable
:name: l2p_ssi_dtime_from_sst

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `ssi_dtime_from_sst` | This variable reports the time difference between SSI data from SST measurement in hours | hour |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_ssi_dtime_from_sst

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]ssi_dtime_from_sst[(,:]'| sed 's/[[:space:]]//'
```

(__l2p_source_of_ssi)=
### `source_of_ssi`

**Optional (Mandatory only if multiple sources for `surface_solar_irradiance` 
are provided).**

The source of data used to set the L2P ancillary data variable
`surface_solar_irradiance` shall be indicated in the L2P variable `source_of_ssi`
when more than one source of SSI data is used in the L2P product. When only one
source is used, this variable is not needed and the appropriate text string
indicating the source is placed in the `source` attribute of the 
`surface_solar_irradiance` variable. 

For multiple sources, the variable `source_of_ssi` should contain an attribute 
called `flag_meanings` and another one called `flag_values`. The `flag_values` 
attribute shall contain a comma-separated list of the numeric codes for the 
sources of data used whose order matches the space-separated text strings in 
the `flag_meanings` attribute. 

These text strings and numeric codes do not need to be unique across different
data sets or even ancillary variables, but must be consistent within a given
variable and clearly specified within each netCDF variable and its attributes. A
best practice for naming the text strings in provided in 
{numref}`product_codes`.

Instead of using a `_FillValue` attribute and value for missing data, it is 
recommended to set missing pixel values to **0** and add the corresponding 
**no_data** meaning in `flag_meanings` attribute.

The variable `source_of_ssi` shall conform to the format requirements shown
in the {numref}`l2p_source_of_ssi`.

```{table} CDL example description of **<span style="font-family:courier;">source_of_ssi</span>** variable
:name: l2p_source_of_ssi

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte             | `source_of_ssi` | Sources of surface solar irradiance values | code  |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_source_of_ssi

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]source_of_ssi[(,:]'| sed 's/[[:space:]]//'
```

In this example, `flag_meanings` and `flag_values` contain code data provided 
by the data provider according to the best practices specified
in {numref}`product_codes`. An example of these codes is given in the 
{numref}`l2p_source_of_ssi_codes`.

```{table} Example text string and numeric codes used to identify the sources of data in surface_solar_irradiance:sources and source_of_ssi
:name: l2p_source_of_ssi_codes

| Numeric Code   | Text String          | Sources of surface solar irradiance Description  | 
|----------------|----------------------|--------------------------------------------------|
| 0 |no_data |No surface solar irradiance set|
|   1    | SSI-MSG_SEVIRI-V1 |SSI from Meteosat Second Generation SEVIRI instrument (EUMETSAT OSI-SAF|
|   2    | SSI-NOAA-GOES_E-V1 |GOES_E SSI data from NOAA |
|   3    | SSI-NOAA-GOES_W-V1 |GOES_W SSI data from NOAA|
|   4    | SSI-ECMWF-V1 |SSI data from European Centre for Medium Range Weather Forecasting|
|   5    | SSI-NCEP-V1 |SSI data from NOAA’s National Center for Environmental Prediction|
|   6    | SSI-NAVY-NAAPS-V1|SSI data from the US Navy Atmospheric aerosol Prediction system|
|   7    |  |Spare to be defined as required|
```

(__l2p_optional_fields)=
### Optional experimental L2P variables included by data provider

Flexibility of L2P product content is provided through the netCDF API, which
allows fully self-describing fields and additional L2P variables may be included
by L2P data providers if they are considered relevant for L2P users. The GDS-{{gds_version}}
also permits the inclusion of R&D variables (e.g. channel radiance data sets,
estimates of Chlorophyll A, fields that facilitate flagging of diurnal
variability, etc.) and 32 bytes per pixel are available in total for
optional/experimental variables in any combination (i.e., variables can be
defined as 32 x byte, 16 x short, 3 x int + 4 x byte, etc). The use of
optional/experimental variables provides a limited amount of flexibility within
the GDS-{{gds_version}} for regional user requirements while maintaining an overall upper
limit on GDS-{{gds_version}} L2P products for data management groups and archive scaling. In
exceptional cases a waiver on the 32 byte ceiling can be requested to extend up
to 64 bytes per pixel.

The GDS-{{gds_version}} issues the following guidance on the inclusion of optional or
experimental variables within L2P data products:

- The sum total of all experimental variables shall not increase L2P record 
  size by more than **32 bytes** per SST pixel. A **waiver** can be requested 
  for   higher amounts up to 64 bytes.
- CF-1.7 or later compliance should be maintained for all 
  optional/experimental variables. Where available, a standard_name 
  attribute should be used.
- It is permitted to use a provider defined coordinate variable associated 
  with experimental fields but this shall be documented in data provider 
  documentation.
- Time difference data (dtime values) should be provided for variables when 
  appropriate.
- The source of data should be indicated: in the single source case as a 
  variable attribute; as a dedicated variable when mixed data sources are 
  present.
- Use of experimental variables requires clear documentation by the GHRSST 
  producer. They shall provide adequate documentation that describes each 
  variable following the CDL examples provided in this document.
- The variable attribute `comment` shall be used to provide a URL link to a 
  full description of each data producer defined variable included in the 
  L2P product.
- Experimental L2P variables if present in an L2P product will be included 
  with the minimum format requirements shown in {numref}`l2p_experimental`
- Additional global variables may be declared within the L2P product.


```{table} CDL template for data provider defined L2P variables
:name: l2p_experimental
| Storage type definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Variable name definition | Description                  | Unit |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|------|
| byte    | Provide a variable name in lower case using underscore separators e.g. `my_variable` | Provide a description of `my_variable` stating content purpose and units | Units of `my_variable` |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_experimental

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]my_variable[(,:]'| sed 's/[[:space:]]//'
```

## CDL example L2P dataset

The following CDL has been generated for a L2P dataset by OSI SAF derived from 
the AVHRR sensor on Metop-C platform (https://doi.org/10.15770/EUM_SAF_OSI_NRT_2013). 
It includes a number of optional and experimental variables.

```{code-cell}
:tags: [remove-input]
:name: l2p_full_cdl

!ncdump -h samples/l2p_full_example.nc
```

[^footnote1]: netCDF Climate and Forecast (CF) Metadata Conventions version 1.7 
or later available from http://cfconventions.org