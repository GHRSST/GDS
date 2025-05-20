---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

(coordinate_variables)=
# Coordinate variables
NetCDF coordinate variables provide scales for the space and time axes for the
multidimensional data arrays, and must be included for all dimensions that can 
be identified as spatio-temporal axes. 

Coordinate arrays are used to geolocate 
data arrays on non-orthogonal grids, such as images in the original pixel/scan 
line space, or complicated map projections. Required attributes are `units` and
`_FillValue`. Elements of the coordinate array need not be monotonically 
ordered. The data type can be any and scaling may be implemented if required. 
`add_offset` and `scale_factor` have to be adjusted according to the sensor 
resolution and the product spatial coverage. If the packed values can not stand 
on a short, float can be used instead (multiplying the size of these variables 
by two).

## Temporal coordinates

`time` is the reference time of the SST data array. The GDS-{{gds_version}} 
specifies that this reference time should be extracted or computed to the 
nearest second and then coded as continuous UTC time coordinates in 
**seconds from 00:00:00 UTC January 1, 1981** (which is the definition of the
GHRSST origin time, chosen to approximate the start of useful AVHRR SST data 
record). Note that the use of UDUNITS in GHRSST implies that that calendar to 
be used is the default mixed Gregorian/Julian calendar.

The reference time used is dependent on the <Processing Level> of the data and 
is defined as follows:

| Processing level | Reference time                      |
|------------------|-------------------------------------|
| L2P              | start time of granule               |
| L3U              | start time of granule               | 
| L3C              | centre time of the collation window |
| L3S              | centre time of the collation window |
| L4               | nominal time of the analysis        |

The coordinate variable `time` is intended to minimize the size of the 
`sst_dtime` variable (e.g., see {numref}`__l2p_sst_dtime`), which stores 
offsets from the reference time in seconds for each SST pixel. `time` also 
facilitates aggregation of all files of a given dataset along the time axis with 
such tools as THREDDS or when building data cubes.

## Spatial coordinates

**x** (columns) and **y** (lines) grid dimensions are referred either as `lat` 
and `lon` or as `ni` and `nj`. `lon` and `lat` must be used if data are mapped 
on a regular grid (some geostationary products). `ni` and `nj` are used if data 
are mapped on a non-regular grid (curvilinear coordinates) or following the 
sensor scanning pattern (scan line, swath). It is preferred that `ni` should be 
used for the across-track dimension and `nj` for the along-track dimension.

Coordinate vectors are used for data arrays located on orthogonal (but not 
necessarily regularly spaced) grids, such as a geographic (lat-lon) map 
projections. The only required attribute is `units`. The elements of a 
coordinate vector array should be in monotonically increasing or decreasing 
order. The data type can be any and scaling may be implemented if required.

A `coordinates` variable attribute (`coordinates = "lon lat" ;`) must be 
provided if the data are on a non-regular lat/lon grid (map projection or 
swath data).

A `grid_mapping` variable attribute (`grid_mapping = "<projection name>" ;`) 
must be provided if the data are mapped following a projection. Refer to the 
CF convention[^footnote2] for standard projection names.

```{admonition} Note on lat/lon arrays
`lat` and `lon` arrays are the only arrays stored as float in GHRSST product 
files and therefore can represent a major fraction of the overall data 
volume. As an optimization factor, producers are encouraged to make use of the
`least_significant_digit` argument when creating these NetCDF variables (refer 
for instance to https://unidata.github.io/netcdf4-python/): in most current 
GHRSST products, there is no need for a precision larger than 3 digits and 
it can be a big volume saver.
```

### Regular latitude/longitude grids
This is the simplest case. Many Level 3 and Level 4 products as well as some 
geostationary L2P products are provided on a regular lat/lon grid. On such a 
projection, only two coordinate variables are requested and they can be stored 
as vector arrays. Longitudes should range from -180 to +180, corresponding to 
180 degrees West to 180 degrees East. Latitudes should range from -90 to +90, 
corresponding to 90 degrees South to 90 degrees North. There should be no
`_FillValue` for latitude and longitude and all SST pixels should have a valid 
latitude and longitude value.

It is recommended that for Level 3 and Level 4 data products the `time` 
dimension be specified as **unlimited**. Note that the `time` dimension for L2P 
data files is strictly defined as `time=1` (unlimited dimension not allowed). 
This strict definition is because L2P data are swath based and the geospatial 
information may change across consecutive time slabs. Although in GHRSST L3 and 
L4 granules there is only one `time` dimension and variable `time` has only one
value (seconds since 1981), setting an unlimited dimension for `time` dimension 
will allow netCDF tools and utilities to easily concatenate (and average for 
example) a series of time consecutive GHRSST granules. The following CDL is 
provided as an example:

```
netcdf example {
    dimensions:
        lat = 1801 ;
        lon = 3600 ;
        time = UNLIMITED ; // (strictly set to 1 for L2P)
    variables:
...
}
```

For these cases, dimension and coordinate variables shall be used for a regular 
lat/lon grid as shown in {numref}`regular_grid_coords`. No specific variable 
attributes are required for other variables (like `sea_surface_temperature` as 
shown in the example given in {numref}`regular_grid_coords`).

```{table} Example CDL for geographic regular latitude/longitude grids
:name: regular_grid_coords

| geographic regular latitude/longitude grids |
| -------------------------------------------------- |
```
```{code-cell}
:tags: [remove-input]
:name: regular_grid_coords

!ncdump -h samples/regular_grid.nc
```

### Non-regular latitude/longitude grids (projection)
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
required for each other variables (like `sea_surface_temperature` in the example
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


### Non-regular latitude/longitude grids (projection) – alternative without explicit latitude/longitude
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

### Non-regular latitude/longitude grids (swath)
In this case where data are gridded following the sensor pattern, no projection 
can be associated and lat/lon data have to be stored in 2-D arrays, as it is 
the case for along-swath data for low earth orbiting sensors or geostationary 
orbiting sensor data in their native projection. Therefore it only applies 
to **L2P** processing level products.

Dimensions cannot be referred to as lat/lon anymore since x and y axes of the 
grid are no more related to the latitude or longitude axis. Instead, dimensions
`ni` and `nj`should be used to describe the swath. As a best practice, the `ni` 
dimension should refer to the cross-track direction and the `nj` dimension 
should refer to the along-track direction of a polar orbiting (or similar) 
satellite sensor swath. For geostationary sensors `ni` also refers to the 
cross-disk direction and `nj` the along-disk direction. Each variable must 
explicitly provide a reference to its coordinate variables (using the 
coordinates variable attribute) and pixel times must be encoded using the 
combination of `time`and `sst_dtime` coordinate variables.

Dimension and coordinate variables shall be used for a non-regular lat/lon grid 
(swath product file) as shown in {numref}`non_regular_grid_coords`. The specific
variable attribute `coordinates = "lon lat"` is required for each of the 
variables (like `sea_surface_temperature` below).

```{table} Example CDL for non-regular latitude/longitude grids (swath)
:name: non_regular_grid_coords

| non-regular latitude/longitude coordinates |
| ------------------------------------------ |
```
```{code-cell}
:tags: [remove-input]
:name: non_regular_grid_coords

!ncdump -h samples/nonregular_grid.nc
```


[^footnote2]: http://cfconventions.org/cf-conventions/cf-conventions.html#appendix-grid-mappings