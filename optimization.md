# File storage optimization

This section describes how to minimize the size of the created NetCDF files and how to make them cloud optimized.

## Variable compression
There are different ways with NetCDF to optimize the disk storage volume occupied by a floating type variable, both 
involving lossy compression:
- **packing** the data into integer type
- adjusting the **number of significant digits** of floating values

```{important} 
The variable compression settings described in this section are only for saving disk storage. Once the variable arrays 
are read into memory, the inflate back to their original size (array size * data type size). For memory optimization, see 
{numref}`chunking` chunking.
```

### Data packing
Data packing consists in storing the floating values into integer type, adjusting an offset (defined in `add_offset` 
variable attribute) and scaling factor (defined in `scale_factor` variable attribute) so that: 

```text
scientific value (float) = storage value (integer) * scale_factor + add_offset
```

The integer storage type, `scale_factor` and `add_offset` values must be adjusted so that they fit the whole range and 
best precision of the floating values to pack, as shown in {numref}`float_packing_example`.

```{code-block}
---
caption: CDL for a sea surface temperature floating array packed into a short integer, retaining only a maximum 0.01 K precision
name: float_packing_example
---
dimensions:
	nj = 40000 ;
	ni = 1000 ;
variables:
    short sea_surface_temperature(nj, ni) ;
        sea_surface_temperature:_FillValue = -32768s ;
        sea_surface_temperature:long_name = "sea surface subskin temperature" ;
        sea_surface_temperature:standard_name = "sea_surface_subskin_temperature" ;
        sea_surface_temperature:units = "K" ;
        sea_surface_temperature:depth = "1 millimeter" ;
        sea_surface_temperature:source = "AVHRR_METOP_C" ;
        sea_surface_temperature:comment = "Temperature of the subskin of the ocean" ;
        sea_surface_temperature:coverage_content_type = "physicalMeasurement" ;
        sea_surface_temperature:coordinates = "lat lon" ;
        sea_surface_temperature:add_offset = 273.15 ;
        sea_surface_temperature:scale_factor = 0.01 ;
```

```{warning}
A bad adjustment of the storage data type, scaling or offset values can lead to a type overthrow and therefore 
storing completely wrong values beyond a certain valid range. Besides, although modern libraries and tools automatically
unpack the data recognizing and using the provided attributes, many users still manually unpack such variables using
hard coded values (instead of always reading the attributes) or using a wrong unpacking formulae.

Packing is therefore prone to errors by both data producers and users and then **now discouraged in GHRSST** although it
is fully compliant with CF convention. **Use with caution**. 
```
### Compression


### Float quantization
NetCDF4 libraries support lossy compression/quantization when creating variables which lock data to a fixed number of 
significant digits regardless of magnitude. Available parameters to adjust the level of quantization include:
- `least_significant_digit` available in python libraries such as Unidata `netcdf4-python` or `xarray` which cause the 
  data to be quantized using numpy.around(scale*data)/scale, where scale = 2**bits, and bits is determined so that it 
  matches the required precision. For example if the data has a precision of 0.1 (`least_significant_digit=1`), 
  then bits=4. 
- starting with netcdf-c version 4.9.0, a quantization capability is provided with `significant_digits` parameter, which
  specifies the absolute number of significant digits independent of the magnitude of the variable (the floating point 
  exponent). It is callable with python libraries based on the NetCDF4 C library.


```{code-block}
---
caption: code snippet using quantization with python Xarray
name: float_quantization_example
---
dimensions:
	nj = 40000 ;
	ni = 1000 ;
variables:
    short sea_surface_temperature(time, nj, ni) ;
        sea_surface_temperature:_FillValue = -32768s ;
        sea_surface_temperature:long_name = "sea surface subskin temperature" ;
        sea_surface_temperature:standard_name = "sea_surface_subskin_temperature" ;
        sea_surface_temperature:units = "K" ;
        sea_surface_temperature:depth = "1 millimeter" ;
        sea_surface_temperature:source = "AVHRR_METOP_C" ;
        sea_surface_temperature:comment = "Temperature of the subskin of the ocean" ;
        sea_surface_temperature:coverage_content_type = "physicalMeasurement" ;
        sea_surface_temperature:coordinates = "lat lon" ;
        sea_surface_temperature:add_offset = 273.15 ;
        sea_surface_temperature:scale_factor = 0.01 ;
```


```{admonition} Note on lat/lon arrays
`lat` and `lon` arrays are the only arrays stored as float in GHRSST product 
files and therefore can represent a major fraction of the overall data 
volume. As an optimization factor, producers are encouraged to make use of the
`least_significant_digit` argument when creating these NetCDF variables (refer 
for instance to https://unidata.github.io/netcdf4-python/): in most current 
GHRSST products, there is no need for a precision larger than 3 digits and 
it can be a big volume saver.
```

(chunking)=
## Chunking


## Cloud-optimization

