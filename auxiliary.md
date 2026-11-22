# Auxiliary variables

## Overview description of the GHRSST auxiliary variables

There are a number of auxiliary fields that shall be provided before a GHRSST data product is admitted into the GHRSST 
R/GTS,  including:
- fields related to the sensing geometry such as the **view angle** ([satellite_zenith_angle](__satellite_zenith_angle)) 
  or the **sun zenith angle** ([solar_zenith_angle](__solar_zenith_angle))
- the **difference between satellite SST measurements and a defined reference climatology of SST** ([dt_analysis](__dt_analysis))
- atmospherical conditions from weather model forecasts or analyses:
  - An estimate of **surface wind speed** ([wind_speed](__wind_speed))
  - An estimate of **sea ice fraction** ([sea_ice_fraction](__sea_ice_fraction))
  - An estimate of the **total water vapour content** ([total_water_vapour_content](__total_water_vapour_content)))
  - An estimate of **atmospheric aerosol** (as an aerosol dynamic indicator, [aerosol_dynamic_indicator](__aerosol_dynamic_indicator))
  - An estimate of **surface solar irradiance**, [surface_solar_irradiance](__surface_solar_irradiance))

Some of these auxiliary fields are mandatory for a given processing level (L2P, L3U, L3C, L3S or L4) while others may be
optional or not applicable as summarized in {numref}`auxiliary_variables_table`.

```{note}
Auxiliary fields having an observation or forecast time can be optionally associated with a time difference to the actual
SST observation time, using `<auxiliary field>_dtime_from_sst` (example: `sea_ice_fraction_dtime_from_sst`). Refer to
{numref}`auxiliary_dtime`.

An auxiliary field composed of multiple observation or forecast sources can be optionally associated with a source identification
field, using `source_of_<auxiliary field>` (example: `source_of_sea_ice_fraction`). Refer to {numref}`auxiliary_source`.

Both variables can be replaced is some cases by a variable attribute of the `<auxiliary field>` variable.
```

```{table} Summary description of GHRSST auxiliary data records, with their applicability to a specific processing level (M: mandatory, O: optional, N/A: not applicable)
:name: auxiliary_variables_table 

| Variable Name         | Description            | Units  | Science data type | L2P | L3U | L3C | L3S | L4 |
|-----------------------|------------------------|--------|-----|-----|-----|-----|-----|-----|
| [satellite_zenith_angle](__satellite_zenith_angle) | Calculated satellite zenith angle (measured at the Earth's surface between the satellite and the zenith)| angular_degree | float | M | M | M | O | N/A 
| [solar_zenith_angle](__solar_zenith_angle) | Calculated solar zenith angle (the angle between the local zenith and the line of sight to the sun, measured at the Earth's surface)| degree | float | M | M | M | O | N/A
| [dt_analysis](__dt_analysis) | The difference between input SST and a GHRSST L4 SST analysis from the previous 24 hour period | K (kelvin)| float | M | M | M | O | N/A
| [wind_speed](__wind_speed) | Closest (in time) 10 m surface wind speed from satellite or analysis  | m s-1 | float | M | M | M | O | N/A
| [sea_ice_fraction](__sea_ice_fraction) | Closest (in time) sea ice fraction from satellite or analysis | 1 | float | M | M | M | M | M
| [total_water_vapour_content](__total_water_vapour_content) | Total Water Vapour Content | kg m-2 | float | M | M | M | O | N/A
| [aerosol_dynamic_indicator](__aerosol_dynamic_indicator) | Atmospheric aerosol indicator | | float | O | O | O | O | N/A
| [surface_solar_irradiance](__surface_solar_irradiance) | Near contemporaneous surface solar irradiance| W m-2| float | O | O | O | O | N/A
| [\<auxiliary field\>_dtime_from_sst](auxiliary_dtime) | Time difference between the auxiliary field value and SST measurement in hours | h (hour)| float | O | O | O | O | N/A
| [source_of_\<auxiliary field\>`](auxiliary_source) | Source(s) of the auxiliary field value | code | byte | O | O | O | O | N/A
```


## Auxiliary data record format specification

(__dt_analysis)=
### `dt_analysis`

```{list-table} Specifications of **<span style="font-family:courier;">dt_analysis</span>** variable
:widths: 20 80
:name: spec_dt_analysis

* - **Applicability**
  - L2P, L3U, L3C: Mandatory ; L3S: Optional
* - **Science data type**
  - float
* - **Unit**
  - K (kelvin)
* - **Description**
  - The difference between input SST and a GHRSST L4 SSTfnd analysis from the previous 24 hour period (T-1), or a reference
    mean SST climatology if not available.
```

The variable `dt_analysis` is the temperature difference between the product SST measurement and a reference SST L4 analysis 
data set. `dt_analysis` may be used to indicate potential areas of diurnal variability or gross outliers in the input SST 
measurement data set by looking for large deviations from the previous analysis SST data. Note that `dt_analysis` is an 
indicator field and the temperature anomalies may be difficult to interpret in regions of high SST gradients. Furthermore,
interpretation requires a good understanding of the strengths and weaknesses (e.g. space and time de-correlations) of the 
chosen reference L4 analysis system.

`dt_analysis` shall be derived using:

```{math}
:label: eq_dt_analysis
dt\_analysis = SST_{input} – L4_{SST}
```

Where SST<sub>input</sub> is the product satellite measurement and L4<sub>SST</sub> is a previous day analysis from a 
GHRSST L4 System selected by the data provider. The GHRSST L4 analysis chosen for a given product should be consistent 
for all files from this product as far as practically possible. If a previous analysis SSTfnd data file is not available 
for use in {eq}`eq_dt_analysis`, then a mean reference SST or climatology should be used in its place as defined in 
{numref}`dt_analysis_code`.

```{table} Reference SST data sets for use in dt_analysis computation
:name: dt_analysis_code
| Name                      | Description                                                                                                                                      | Reference                                                              |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Use code from L4 analysis | The mean SSTfnd computed for a n-1 day period. This product is computed from data provider SSTfnd data products in real time each day             | https://www.ghrsst.org/ghrsst-data-services/ghrsst-catalogue/          |
| GMPE_GLOBAL               | Daily, 25 km median average SST and sea ice product created using 10 operational SST analysis products from operational centres around the world | https://ghrsst-pp.metoffice.gov.uk/ostia-website/gmpe-monitoring.html  |
```

The `dt_analysis` value shall be inserted into the `dt_analysis` field of the product for the pixel in question as described 
{numref}`ex_dt_analysis` (here in the case of a L2P).


**Example:**

```{code-block}
---
caption: CDL for `dt_analysis` variable in a L2P file
name: ex_dt_analysis
---
dimensions:
	time = UNLIMITED ; // (1 currently)
	nj = 1080 ;
	ni = 2048 ;
variables:
	float dt_analysis(time, nj, ni) ;
		dt_analysis:_FillValue = 1e20 ;
		dt_analysis:long_name = "deviation from SST analysis or reference climatology" ;
		dt_analysis:units = "K" ;
		dt_analysis:reference = "OSTIA" ;
		dt_analysis:comment = "The difference between this SST and the previous day\'s SST analysis" ;
		dt_analysis:coverage_content_type = "auxiliaryInformation" ;
		dt_analysis:coordinates = "lat lon" ;
```

```{note}
The `reference` variable attribute should be used to specify the analysis or climatology used to compute `dt_analysis` 
as shown in the example above following the guidelines in {numref}`dt_analysis_code`.
```


(__wind_speed)=
### `wind_speed`

```{list-table} Specifications of **<span style="font-family:courier;">wind_speed</span>** variable
:widths: 20 80
:name: spec_wind_speed

* - **Applicability**
  - L2P, L3U, L3C: Mandatory ; L3S: Optional
* - **Science data type**
  - float
* - **Unit**
  - m s-1
* - **CF standard name**
  - wind_speed
* - **Description**
  - Surface wind speed at 10m height. Resolution should be no less than 1 m s-1
```

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
{numref}`auxiliary_dtime`. In the case of an analysis field, 
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

If multiple sources of data are used, source information should be indicated in the L2P variable `source_of_wind_speed` 
as defined by the data provider and as described in detail in {numref}`auxiliary_source`, and the  `source` variable 
attribute of `wind_speed` shall have the value `source_of_wind_speed`. In addition, the units of all sources used in the 
file shall be identical.


**Example:**

```{code-block}
---
caption: CDL for `wind_speed` variable in a L2P file
name: ex_wind_speed
---
dimensions:
	time = UNLIMITED ; // (1 currently)
	nj = 1080 ;
	ni = 2048 ;
variables:
	float wind_speed(time, nj, ni) ;
		wind_speed:_FillValue = -128b ;
		wind_speed:long_name = "10m wind speed" ;
		wind_speed:standard_name = "wind_speed" ;
		wind_speed:units = "m s-1" ;
		wind_speed:height = "10 m" ;
		wind_speed:time_offset = 0. ;
		wind_speed:source = "WSP-ECMWF-Forecast" ;
		wind_speed:comment = "These wind speeds were created by the ECMWF and represent winds at 10 metres above the sea surface. " ;
		wind_speed:coordinates = "lat lon" ;
```


A single source of wind data is shown in this example which is reported as 
`wind_speed:source = "ECMWF_Anaylsis_V2"` the code has been defined by the data
provider using the ancillary data naming rules given in {numref}`product_codes`. 
Since all of the wind speeds have the same time, the attribute `time_offset` is
used instead of the variable `wind_speed_dtime_from_sst`.

(__sea_ice_fraction)=
### `sea_ice_fraction`

```{list-table} Specifications of **<span style="font-family:courier;">sea_ice_fraction</span>** variable
:widths: 20 80
:name: spec_sea_ice_fraction

* - **Applicability**
  - L2P, L3U, L3C, L3S, L4: Mandatory (except for regional products with no sea ice)
* - **Science data type**
  - float
* - **Unit**
  - 1 (unitless)
* - **CF standard name**
  - sea_ice_area_fraction
* - **Description**
  - fractional of sea ice contamination in a given pixel. Ranges from 0 to 1. 
```

Some SST data are contaminated in part or wholly by sea ice and the variable`sea_ice_fraction` is used to quantify 
the fraction of an area contaminated with sea ice, ranging from 0 to 1. 

Some input SST data streams (L2) provide a flag to indicate that the SST measurement is contaminated by sea ice (e.g., 
passive microwave radiometers such as AMSR-E). If an input data set pixel fractional sea ice estimate exists, this should
be used to fill in the variable `sea_ice_fraction` as described in the table {numref}`spec_sea_ice_fraction`. If an 
input data set pixel sea ice flag exists (i.e. indicating sea ice but not the fractional amount of coverage), this 
should be used to set the L2P variable `sea_ice_fraction` to 1 (zero otherwise).

In most cases, such input data set pixel fractional sea ice estimate or pixel sea ice flag does not exist; if a pixel 
located in or close to a region that may be ice contaminated, a reference sea ice fraction data set should be used to 
determine the value of the variable `sea_ice_fraction`. This reference sea ice fraction data set may come from a model
or an auxiliary remote sensing product (such as sea ice concentration maps provided by microwave radiometers).

The difference in time expressed in hours between the time of SST measurement and the time of sea ice fraction measurement 
should be entered into the variable `sea_ice_fraction_dtime_from_sst` as described in {numref}`auxiliary_dtime`. In 
the case of an analysis field, this should be the central (mean) time of an integrated value. If all ice observations 
have a single time value, as in the case of an analysis or model that gives the sea ice values at an instant in time, 
then the `sea_ice_fraction_dtime_from_sst` variable is not needed and instead a variable attribute named `time_offset` 
is used. The attribute `time_offset` should store the difference in hours between the `sea_ice_fraction` and the 
reference time, stored in the variable `time`.

If a single source of data is used in the variable `sea_ice_fraction`, the L2P variable `source_of_sea_ice_fraction` is 
not required and instead the `source` variable attribute value of `sea_ice_fraction` is sufficient. It shall 
be a single source text string defined by the data provider using the text string naming best practice given in 
{numref}`product_codes`.

If multiple sources of data are used, source information should be indicated in the L2P variable `source_of_sea_ice_fraction` 
as defined by the data provider and as described in detail in {numref}`auxiliary_source`, and the `source` variable 
attribute of `sea_ice_fraction` shall have the value `source_of_sea_ice_fraction`. In addition, the units of all sources
used in the file shall be identical.

The variable attribute `sea_ice_treatment` shall specify how the sea ice information has been treated by the data 
provider. Valid options are: 
- *"Used unmodified (one source)"*, 
- *"used unmodified (multiple ice sources)”*,
- *“modified using onboard sensors"*.


**Example:**

```{code-block}
---
caption: CDL for `sea_ice_fraction` variable in a L2P file
name: ex_sea_ice_fraction
---
dimensions:
	time = UNLIMITED ; // (1 currently)
	nj = 1080 ;
	ni = 2048 ;
variables:
	float sea_ice_fraction(time, nj, ni) ;
		sea_ice_fraction:_FillValue = 1e20 ;
		sea_ice_fraction:long_name = "sea ice fraction" ;
		sea_ice_fraction:standard_name = "sea_ice_area_fraction" ;
		sea_ice_fraction:units = "1" ;
		sea_ice_fraction:time_offset = 3. ;
		sea_ice_fraction:source = "ICE-OSISAF" ;
		sea_ice_fraction:comment = "Fractional sea ice cover from OSISAF ice product" ;
		sea_ice_fraction:coverage_content_type = "auxiliaryInformation" ;
		sea_ice_fraction:coordinates = "lat lon" ;
        sea_ice_fraction:sea_ice_treatment = "Used unmodified (one source)" ;
```

A single source of sea ice fraction data is shown in this example which is reported as 
`sea_ice_fraction:source = "ICE-OSISAF"` following the ancillary data naming conventions specified in 
{numref}`product_codes`. Since all of ice values have the same time, the attribute `time_offset` is used 
instead of the variable `sea_ice_fraction_dtime_from_sst`.


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

(auxiliary_dtime)=
###  `<auxiliary field>_dtime_from_sst`




(auxiliary_source)=
###  `source_of_<auxiliary field>`

The source of data used to set the GHRSST auxiliary data variables shall be indicated in the variable 
`source_of_<auxiliary field>`, where `<auxiliary field>` is the variable name of the auxiliary field, when more than one
source of auxiliary field data is used in the product. 

When only one source is used, this variable is not needed and the appropriate text string indicating the source is placed 
in the sources attribute of the `<auxiliary field>` variable. 

For multiple sources, The variable in question should contain an attribute called `flag_meanings` and another one 
called `flag_values`. The `flag_values` attribute shall contain a comma-separated list of the numeric codes for the 
sources of data used whose order matches the space-separated text strings in the `flag_meanings` attribute. These text 
strings and numeric codes do not need to be unique across different data sets or even ancillary variables, but must be 
consistent within a given variable and clearly specified within each netCDF variable and its attributes. A best practice 
for naming the text strings in provided in {numref}`product_codes`.

Instead of using a `_FillValue` attribute and value for missing data, it is recommended to set missing pixel values to 
**0** and add the corresponding **no_data** meaning in `flag_meanings` attribute.

The variable `source_of_<auxiliary field>` shall conform to the with the format requirements shown in the 
{numref}`source_of_auxiliary`.

```{table} CDL example description of **<span style="font-family:courier;">source_of_<auxiliary field></span>** variable
:name: source_of_auxiliary

| **Storage type** | **Name**     | **Description**                  | **Unit** |
|-------------------|--------------|----------------------------------|----------|
| byte | `source_of_<auxiliary field>` | Sources of auxiliary field values, as a code | None |
```

```{code-cell}
:tags: [remove-input]
:name: l2p_source_of_adi

!ncdump -h samples/l2p_full_example.nc | grep $'[ , \t]source_of_adi[(,:]'| sed 's/[[:space:]]//'
```

In this example, `flag_meanings` and `flag_values` contain strings and numeric codes provided by the data provider 
according to the best practices specified in {numref}`product_codes`.



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
