---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

(coordinate_variables)=
# Coordinate variables and dimensions
NetCDF coordinate variables provide scales for the space and time axes for the multidimensional data arrays, and must be
included for all dimensions that can be identified as spatio-temporal axes. The selected coordinate system and product
processing level also guides the dimensions and coordinate references that shall be provided for a science data variable
(like `sea_surface_temperature`). The following subsections provide detailed specifications and examples for the 
different processing levels and coordinate reference systems.


## Temporal coordinates and dimensions
The temporal coordinates and dimensions are defined differently depending on the product processing level as detailed in 
the following subsections. 

Time values should be computed **at least to the nearest second**  (milliseconds are allowed if needed) and then coded as 
continuous UTC time coordinates. integer (if time values are rounded to the nearest second) or float types (32 or 64 bits) 
are allowed, depending on the time precision.

The GDS-{{gds_version}} requires that any time variable should be expressed in *seconds from 00:00:00 UTC January 1, 1981* 
(which is the definition of the GHRSST origin time, chosen to approximate the start of useful AVHRR SST data record). 
Note that the use of UDUNITS in GHRSST implies that the calendar to be used is the default mixed Gregorian/Julian calendar.


### Level 2P
A variable `time` must be provided, defining a time value for each observation pixel (dimensions are the across-track and 
along-track axes) or sensor scan line (along-track axis). Elements of the time array need not be monotonically and 
chronologically ordered in the along-track dimension.

```{code-block}
---
caption: Full pixel observation time
name: __example_time_2p_2d
---
dimensions:
	nj = 1080 ;
	ni = 2048 ;
variables:
	int time(nj, ni) ;
		time:long_name = "pixel observation time" ;
		time:standard_name = "time" ;
		time:authority = "CF-1.11, ACDD-1.3" ;
		time:axis = "T" ;
		time:coordinates = "lat lon" ;
		time:units = "seconds since 1981-01-01" ;
		time:calendar = "proleptic_gregorian" ;
		time:coverage_content_type = "coordinate" ;
		time:comment = "includes leap seconds since 1981" ;
```

```{code-block}
---
caption: Scan line observation time
name: __example_time_2p_1d
---
dimensions:
	nj = 1080 ;
	ni = 2048 ;
variables:
	int time(nj) ;
		time:long_name = "scan line observation time" ;
		time:standard_name = "time" ;
		time:authority = "CF-1.11, ACDD-1.3" ;
		time:axis = "T" ;
		time:coordinates = "lat lon" ;
		time:units = "seconds since 1981-01-01" ;
		time:calendar = "proleptic_gregorian" ;
		time:coverage_content_type = "coordinate" ;
		time:comment = "includes leap seconds since 1981" ;
```

```{important}
There shall not be any missing value in a time array for a Level 2 product (and therefore no `_FillValue` attribute is 
required.
```

```{note}
if an additional SST variable `<variable>` is added with a different observation time (for instance adjusted to a given 
local time of day), it should be named `time_of_<variable>`. The same above definition rules apply.
```

### Level 3U, Level 3C, Level 3S, Level 4 

Two time arrays must be provided: 
- a unidimensional `time` variable giving  a single reference time for the whole file
  content. this `time` variable facilitates aggregation of all files of a given dataset along the time axis with such 
  tools as THREDDS or when building data cubes. This reference time is chosen, for each processing level, as defined in
  table {numref}`__reference_time_convention`.
- a 3-dimensional ((time, lat, lon) or (time, nj, ni)) variable `or_time` providing the observation time of each valid 
  pixel, for Level 3U, 3C, 3S products (this variable is not required for L4 analysis products)

```{important}
It is recommended that the `time` dimension be specified as **unlimited**. Although there is only one `time` dimension 
and variable `time` has only one value, setting an unlimited dimension for `time` dimension will allow netCDF tools and 
utilities to easily concatenate (and average for example) a series of time consecutive granules.
```


```{table} Reference time convention for "time" variable value in GHRSST gridded datasets
:name: __reference_time_convention

| Processing level | Reference time                     |
|------------------|----------------------------------- |
| L3U              | start time of granule              | 
| L3C              | centre time of the collation window|
| L3S              | centre time of the collation window|
| L4               | nominal time of the analysis       |
```

```{note}
if an additional SST variable `<variable>` is added with a different observation time (for instance adjusted to a given 
local time of day), it should be named `or_time_of_<variable>`. The same above definition rules apply.
```

```{warning}
In previous GDS versions (<3), the `or_time` was named `sst_dtime` and contained the relative offset to the reference 
time. The `or_time` array contains absolute time values, like any other temporal variable.
```

```{code-block}
---
caption: Full pixel observation time (L3U, L3C, L3S)
name: __example_time_l3
---
dimensions:
	lat = 1600 ;
	lon = 3600 ;
	time = 1 ;
variables:
	int or_time(time, lat, lon) ;
		or_time:long_name = "pixel observation time" ;
		or_time:standard_name = "time" ;
		or_time:authority = "CF-1.11, ACDD-1.3" ;
		or_time:coordinates = "lat lon" ;
		or_time:units = "seconds since 1981-01-01" ;
		or_time:calendar = "proleptic_gregorian" ;
		or_time:coverage_content_type = "coordinate" ;
		or_time:comment = "includes leap seconds since 1981" ;
	double time(time) ;
		time:_FillValue = 1.e+20 ;
		time:axis = "T" ;
		time:long_name = "reference time of sst file" ;
		time:standard_name = "time" ;
		time:authority = "CF-1.11, ACDD-1.3" ;
		time:coverage_content_type = "coordinate" ;
		time:units = "seconds since 1981-01-01" ;
		time:calendar = "proleptic_gregorian" ;
		time:coordinates = "lat lon" ;
		time:comment = "includes leap seconds since 1981" ;
```

```{code-block}
---
caption: Single reference time (Level 4)
name: __example_time_l4
---
dimensions:
	lat = 1600 ;
	lon = 3600 ;
	time = 1 ;
variables:
	double time(time) ;
		time:_FillValue = 1.e+20 ;
		time:axis = "T" ;
		time:long_name = "reference time of sst file" ;
		time:standard_name = "time" ;
		time:authority = "CF-1.11, ACDD-1.3" ;
		time:coverage_content_type = "coordinate" ;
		time:units = "seconds since 1981-01-01" ;
		time:calendar = "proleptic_gregorian" ;
		time:coordinates = "lat lon" ;
		time:comment = "includes leap seconds since 1981" ;
```


## Spatial coordinates and dimensions

Spatial coordinate arrays are used to locate spatially data arrays on orthogonal, such as regular geographical grids, 
or non-orthogonal grids, such as images in the original pixel/scan line space or complicated map projections.  

**x** (columns) and **y** (lines) grid dimensions are labelled either as `lat` and `lon` or as `ni` and `nj`:
- `lon` and `lat` must be used only if data are mapped on a orthogonal grid projection allowing for unidimensional, but not 
   necessarily regularly spaced, latitude and longitude axes, like cylindrical geographic (lat-lon) projections used for 
   many L3U, L3C, L3S or L4 products. If `lat` and `lon` are axis dimensions, there should be a one dimension vector 
   array called `lat` containing the latitude values in degrees along the `lat` axis and a one dimension vector array 
   called `lon` containing the longitude values in degrees along the `lon` axis.
- `ni` and `nj` are used if data are mapped on a non-regular grid (curvilinear coordinates) or following the sensor 
   scanning pattern (scan line, swath). It is preferred that `ni` should be used for the X-axis or across-track dimension 
   and `nj` for the Y-axis or along-track dimension. It the data are mapped using a defined geographic projection, there 
   should be a unidimensional vector array called `ni` containing the X-axis values in degrees or meters along the `ni` 
   axis and a unidimensional vector array called `nj` containing the Y-axis values in degrees along the `nj` axis in the
   used projection.

```{note}
Elements of coordinate vectors (unidimensional axis variables) need to be in monotonically increasing or decreasing 
order, except when crossing the date line for a longitude axis. 
```

`lat` and `lon` coordinate variables are **mandatory for Level 2P** products in the sensor scanning pattern (scan line, swath). 
They are **optional if a associated geographic projection is defined**, from which the latitude and longitude for each grid cell 
can be computed, though **highly recommended**. They should be only omitted if product size is critical. The used 
projection must be defined in a dimensionless coordinate reference system (CRS) variable with the name of the projection.

The following subsections describe the different cases applicable to GHRSST products and give examples.

```{important}
- Longitudes are expressed in degrees and should range from -180 to +180, corresponding to 180 degrees West to 180 
  degrees East. 
- Latitudes are expressed in degrees should range from -90 to +90, corresponding to 90 degrees South to 90 degrees North. 
- There should be no missing value in any spatial coordinate variable (and therefore no `_FillValue` attribute is needed)
  and all SST pixels should have valid coordinates in the product coordinate reference system.
```


### Coordinates in sensor geometry (Level 2P)
In this case where data are gridded following the sensor pattern (swath), no projection can be associated and lat/lon 
data have to be stored in 2-D arrays, as it is the case for along-swath data for low earth orbiting sensors or 
geostationary orbiting sensor data in their native projection. Therefore it only applies to **L2P** processing level 
products.

Dimensions cannot be referred to as lat/lon anymore since x and y axes of the grid are no more related to the latitude 
or longitude axis. Instead, dimensions `ni` and `nj`should be used to describe the swath. As a best practice, the `ni` 
dimension should refer to the cross-track direction and the `nj` dimension should refer to the along-track direction of 
a polar orbiting (or similar) satellite sensor swath. For geostationary sensors `ni` also refers to the cross-disk 
direction and `nj` the along-disk direction. Each variable must explicitly provide a reference to its coordinate 
variables (using the coordinates variable attribute) as detailed in {numref}`__coordinate_reference`.

Dimension and coordinate variables shall be used for a non-regular lat/lon grid (swath product file) as shown in 
{numref}`non_regular_grid_coords`. The specific variable attribute `coordinates = "lon lat"` is required for each of the 
variables (like `sea_surface_temperature` below).

```{code-block}
---
caption: CDL for non-regular latitude/longitude grids (swath)
name: non_regular_grid_coords
---
dimensions:
	time = 1 ;
	nj = 40000 ;
	ni = 1000 ;
variables:
	float lat(nj, ni) ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
		lat:coverage_content_type = "coordinate" ;
		lat:units = "degrees_north" ;
	float lon(nj, ni) ;
		lon:long_name = "longitude" ;
		lon:standard_name = "longitude" ;
		lon:coverage_content_type = "coordinate" ;
		lon:units = "degrees_east" ;
```

For level 2P products, the dimensions of the science data variables are the same as `lat` and `lon` coordinate variables.
A `coordinates` variable attribute (`coordinates = "lon lat" ;`) must be provided, as shown in 
{numref}`non_regular_grid_science_data`.

```{code-block}
---
caption: CDL for science data dimensions and coordinate reference attributes in non-regular latitude/longitude grids (swath)
name: non_regular_grid_science_data
---
dimensions:
	nj = 40000 ;
	ni = 1000 ;
variables:
    float sea_surface_temperature(nj, ni) ;
        sea_surface_temperature:_FillValue = 1e20 ;
        sea_surface_temperature:long_name = "sea surface subskin temperature" ;
        sea_surface_temperature:standard_name = "sea_surface_subskin_temperature" ;
        sea_surface_temperature:units = "K" ;
        sea_surface_temperature:depth = "1 millimeter" ;
        sea_surface_temperature:source = "AVHRR_METOP_C" ;
        sea_surface_temperature:comment = "Temperature of the subskin of the ocean" ;
        sea_surface_temperature:coverage_content_type = "physicalMeasurement" ;
        sea_surface_temperature:coordinates = "time lat lon" ;
```


(_grid_coordinates)=
### Coordinates in grids (Level 3U, 3C, 3S and 4)

In these subsections, different cases are described:
- regular cyclindrical latitude/longitudes grids, in {numref}`_regular_latlon_grid`, where latitude and longitude can be
  stored in vector arrays
- non-regular projection grids with explicit latitude and longitude ({numref}`_irregular_latlon_grid_explicit`) or 
  without ({numref}`_irregular_latlon_grid_implicit`)

However for all products with an associated projection, the following rules must apply:
- the projection must be explicitly defined in a dimensionless CRS (Coordinate Reference System) variable, as 
  recommended by CF convention, even for regular geographical grids. This CRS variable is referred to by all data 
  variables with the variable attribute `grid_mapping`
- the boundaries of the latitude and longitude grid cells should be defined in explicit boundary variables `lon_bnds` 
  and `lat_bnds` as recommended by CF convention


```{code} python
---
caption: Code snippet: generating a CF compliant CRS variable
name: generating_crs
---
import numpy as np
import xarray as xr
import rioxarray

# 1. Create mockup dimensions and coordinates
lats = np.linspace(-90, 90, 180)
lons = np.linspace(-180, 180, 360)
temperature_data = np.random.rand(180, 360)

# 2. Build the xarray Dataset
ds = xr.Dataset(
    data_vars={
        "sea_surface_temperature": (["lat", "lon"], temperature_data)
    },
    coords={
        "lat": lats,
        "lon": lons
    }
)

# 3. Assign the Plate Carrée (EPSG:4326) CRS
# This automatically generates the spatial_ref variable and grid_mapping attributes
ds = ds.rio.write_crs("EPSG:4326")
ds = ds.rename_vars({'spatial_ref': 'crs'})

```

(_regular_latlon_grid)=
#### Regular latitude/longitude grids
This is the simplest case. Many Level 3 and Level 4 products are provided on a regular lat/lon grid. On such a 
projection, `lat` and `lon` can be stored as vector arrays and they are both coordinate and axis (dimension) variables.

For these cases, dimension and coordinate variables shall be used for a regular lat/lon grid as shown in 
{numref}`regular_grid_coords`.

```{code-block}
---
caption: CDL for geographic regular latitude/longitude grids
name: regular_grid_coords
---
dimensions:
	time = UNLIMITED ; // (1 currently)
	lat = 1800 ;
	lon = 3600 ;
	bnds = 2 ;
variables:
	float lat(lat) ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
		lat:coverage_content_type = "coordinate" ;
		lat:units = "degrees_north" ;
		lat:comment = "geographical coordinates, WGS84 projection" ;
		lat:valid_range = -90., 90. ;
	float lon(lon) ;
		lon:axis = "X" ;
		lon:long_name = "longitude" ;
		lon:standard_name = "longitude" ;
		lon:coverage_content_type = "coordinate" ;
		lon:units = "degrees_east" ;
		lon:comment = "geographical coordinates, WGS84 projection" ;
		lon:valid_range = -180., 180. ;
	float lat_bnds(lat, bnds) ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
		lat:coverage_content_type = "coordinate" ;
		lat:units = "degrees_north" ;
		lat:comment = "geographical coordinates, WGS84 projection" ;
		lat:valid_range = -90., 90. ;
	float lon_bnds(lon, bnds) ;
		lat:axis = "Y" ;
		lat:long_name = "latitude" ;
		lat:standard_name = "latitude" ;
		lat:coverage_content_type = "coordinate" ;
		lat:units = "degrees_north" ;
		lat:comment = "geographical coordinates, WGS84 projection" ;
		lat:valid_range = -90., 90. ;
    int64 crs ;
            spatial_ref:crs_wkt = "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.0174532925199433,AUTHORITY[\"EPSG\",\"9122\"]],AXIS[\"Latitude\",NORTH],AXIS[\"Longitude\",EAST],AUTHORITY[\"EPSG\",\"4326\"]]" ;
            spatial_ref:semi_major_axis = 6378137. ;
            spatial_ref:semi_minor_axis = 6356752.31424518 ;
            spatial_ref:inverse_flattening = 298.257223563 ;
            spatial_ref:reference_ellipsoid_name = "WGS 84" ;
            spatial_ref:longitude_of_prime_meridian = 0. ;
            spatial_ref:prime_meridian_name = "Greenwich" ;
            spatial_ref:geographic_crs_name = "WGS 84" ;
            spatial_ref:horizontal_datum_name = "World Geodetic System 1984" ;
            spatial_ref:grid_mapping_name = "latitude_longitude" ;
            spatial_ref:spatial_ref = "GEOGCS[\"WGS 84\",DATUM[\"WGS_1984\",SPHEROID[\"WGS 84\",6378137,298.257223563,AUTHORITY[\"EPSG\",\"7030\"]],AUTHORITY[\"EPSG\",\"6326\"]],PRIMEM[\"Greenwich\",0,AUTHORITY[\"EPSG\",\"8901\"]],UNIT[\"degree\",0.0174532925199433,AUTHORITY[\"EPSG\",\"9122\"]],AXIS[\"Latitude\",NORTH],AXIS[\"Longitude\",EAST],AUTHORITY[\"EPSG\",\"4326\"]]" ;

	    
```

For science data variables, the `coordinates` variable attribute is not required for a horizontal grid defined as a 
Cartesian product of latitude and longitude axes. A `grid_mapping` variable attribute (`grid_mapping = "<projection name>" ;`) 
shall be provided if the data are mapped following a projection. Refer to the CF convention[^footnote2] for standard 
projection names, as shown in {numref}`regular_grid_science_data`.

```{code-block}
---
caption: CDL for science data dimensions and coordinate reference attributes in regular latitude/longitude grids
name: regular_grid_science_data
---
dimensions:
	time = UNLIMITED ; // (1 currently)
	nj = 40000 ;
	ni = 1000 ;
variables:
    float sea_surface_temperature(time, nj, ni) ;
		sea_surface_temperature:_FillValue = 1e20 ;
		sea_surface_temperature:long_name = "Skin temperature of the sea surface" ;
		sea_surface_temperature:standard_name = "sea_surface_skin_temperature" ;
		sea_surface_temperature:coverage_content_type = "physicalMeasurement" ;
		sea_surface_temperature:units = "K" ;
		sea_surface_temperature:grid_mapping = "Lambert_Azimuthal_Grid" ;
		sea_surface_temperature:coordinates = "Lambert_Azimuthal_Grid or_time lat lon" ;
```

```{code-block}
---
caption: CDL for science data dimensions and coordinate reference attributes in regular latitude/longitude grids
name: regular_l4_grid_science_data
---
dimensions:
	time = UNLIMITED ; // (1 currently)
	nj = 40000 ;
	ni = 1000 ;
variables:
    float sea_surface_temperature(time, nj, ni) ;
		sea_surface_temperature:_FillValue = 1e20 ;
		sea_surface_temperature:long_name = "Skin temperature of the sea surface" ;
		sea_surface_temperature:standard_name = "sea_surface_skin_temperature" ;
		sea_surface_temperature:coverage_content_type = "physicalMeasurement" ;
		sea_surface_temperature:units = "K" ;
		sea_surface_temperature:grid_mapping = "Lambert_Azimuthal_Grid" ;
		sea_surface_temperature:coordinates = "Lambert_Azimuthal_Grid time lat lon" ;
```

(_irregular_latlon_grid_explicit)=
#### Non-regular latitude/longitude grids (projection)
For gridded data using a specific projection (such as stereographic projection),
lat/lon have to be stored in 2-D arrays. When data are gridded following the 
sensor pattern, no projection can be associated and lat/lon data have to be 
stored in 2-D arrays. Dimensions cannot be referred to as lat/lon anymore since
the **x** and **y** axes of the grid are not related to the latitude or 
longitude axis. Each variable must explicitly provide a reference to its 
coordinate variables (`coordinates` variable attribute) and to the related 
projection (`grid_mapping` variable attribute) described in a specific variable 
(for example, `Lambert_Azimuthal_Grid",` in the example given in 
{numref}`non_regular_grid_coords_projection`, refer to CF convention 
[^footnote2] for standard projection names).

In these cases, dimension and coordinate variables shall be used for a 
non-regular lat/lon grid (projection) as shown in 
{numref}`non_regular_grid_coords_projection`. A specific projection coordinate 
variable shall be added (for example, `Lambert_Azimuthal_Grid`), following the 
CF-1.7 or later convention. The specific variable attributes 
`coordinates = "lon lat"` and`grid_mapping = "Lambert_Azimuthal_Grid"` are 
required for each other variable (like `sea_surface_temperature` in the example
given in {numref}`non_regular_grid_coords_projection`).

Note that variable attributes such as `grid_mapping` may be set differently 
(when using a different kind of projection) or completely removed (for swath 
products or regular grids if required).


```{table} Example CDL for non-regular latitude/longitude grids (projection)
:name: non_regular_grid_coords_projection

| non-regular latitude/longitude grids (projections) |
| -------------------------------------------------- |
```
```{code-cell}
:tags: [remove-input]
:name: non_regular_grid_coords_projection

!ncdump -h samples/nonregular_grid_projection.nc
```



(__coordinate_reference)=
## Associating coordinates to a variable
A `coordinates` variable attribute (`coordinates = "lon lat" ;`) must be 
provided if the data are on a non-regular lat/lon grid (map projection or 
swath data).

The latitude and longitude coordinates of a horizontal grid that was not defined as a Cartesian product of latitude and 
longitude axes, can sometimes be represented using two-dimensional coordinate variables. These variables are identified as coordinates by use of the coordinates attribute.

A `grid_mapping` variable attribute (`grid_mapping = "<projection name>" ;`) 
must be provided if the data are mapped following a projection. Refer to the 
CF convention[^footnote2] for standard projection names.


(_irregular_latlon_grid_implicit)=

#### Non-regular latitude/longitude grids (projection) – alternative without explicit latitude/longitude
For gridded data using a fixed specific projection (such as geostationary 
projection), the same lat/lon 2-D arrays are repeated from file to file. If a 
fixed projection can be associated to lat/lon data, it is also permitted by CF 
convention to provide a projection variable defining this projection, instead of
providing explicit latitude/longitude 2-D arrays as in the previous section. 
This usually allows to save significant storage (which is interesting for 
products with a high temporal repetitiveness such as geostationary products in 
satellite projection) while being less user friendly since users will have to 
calculate their own latitude/longitude 2-D arrays from the projection parameters
(this is done automatically in some CF compliant tools). The projection variable
must be named with the projection name used in the product (like `geostationary`
below). It is dimensionless and of type int. The naming and content of this
projection variable is described in CF conventions[^footnote2].


The **x** (abscissa) and **y** (ordinate) rectangular coordinates must be 
provided in `ni` and `nj` variables, identified by the `standard_name`attribute 
values `projection_x_coordinate` and `projection_y_coordinate` respectively. 
In the case of this geostationary projection, the projection coordinates in this
projection are directly related to the scanning angle of the satellite 
instrument, and their units are radians.

Each variable must explicitly provide a reference to its coordinate variables 
(coordinates variable attribute) and to the related projection (`grid_mapping`
variable attribute) described in a specific variable (e.g. geostationary in the 
example given in {numref}`non_regular_grid_coords_projection_no_latlon`; refer 
to CF convention[^footnote2] for standard projection names).

In these cases, dimension and coordinate variables shall be used for a 
non-regular lat/lon grid (projection) as shown in 
{numref}`non_regular_grid_coords_projection_no_latlon`. A specific projection 
coordinate variable shall be added (for example, `geostationary`), following the
CF-1.7 or later convention. The specific variable attributes 
`coordinates = "nj ni"` and `grid_mapping = "geostationary"` are required for 
each other variables (like `sea_surface_temperature` in the example given in 
{numref}`non_regular_grid_coords_projection_no_latlon`).


```{table}  Example CDL for Non-regular latitude/longitude grids (projections) alternative form with no explicit latitudes/longitudes
:name: non_regular_grid_coords_projection_no_latlon

| non-regular latitude/longitude grids (projections) with no explicit latitude/longitude |
| -------------------------------------------------- |
```
```{code-cell}
:tags: [remove-input]
:name: non_regular_grid_coords_projection_no_latlon

!ncdump -h samples/nonregular_grid_projection_no_latlon.nc
```




[^footnote2]: http://cfconventions.org/cf-conventions/cf-conventions.html#appendix-grid-mappings
