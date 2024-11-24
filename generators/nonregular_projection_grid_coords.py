import xarray as xr
import numpy as np

ds = xr.Dataset(
    coords={
        'time': xr.DataArray(
            data=[np.datetime64('2020-01-01 00:00:00', 'ns')], 
            dims='time',
            attrs={
                'axis': 'T',
                'long_name': "reference time of sst file",
                'standard_name': "time",
                'coverage_content_type': "coordinate"
            }),
        'lat': xr.DataArray(
            data=np.ones((40000, 1000), dtype=np.float32), 
            dims=('nj', 'ni',),
            attrs={
                'long_name': "latitude",
                'standard_name': "latitude",
                'coverage_content_type': "coordinate",
                'units': "degrees_north",
                'valid_range': [np.float32(-90.), np.float32(90.)]
            }),
        'lon': xr.DataArray(
            data=np.ones((40000, 1000), dtype=np.float32), 
            dims=('nj', 'ni',),
            attrs={
                'long_name': "longitude",
                'standard_name': "longitude",
                'coverage_content_type': "coordinate",
                'units': "degrees_east",
                'valid_range': [np.float32(-180.), np.float32(180.)]
            }),
        'Lambert_Azimuthal_Grid': xr.DataArray(
            data=np.int32(0),
            dims=(),
            attrs={
                'grid_mapping_name': 'lambert_azimuthal_equal_area',
                'longitude_of_projection_origin': 0.,
                'latitude_of_projection_origin': 90.,
                'false_easting': 0.,
                'false_northing': 0.,
                'semi_major_axis': 6378137.,
                'inverse_flattening': 298.257223563,
                'proj4_string': "+proj=laea +lon_0=0 +datum=WGS84 +ellps=WGS84 +lat_0=90.0"
            }
        )
    },
    data_vars={
        'sst_dtime': xr.DataArray(
            data=np.ones((1, 40000, 1000), dtype=np.int16), 
            dims=('time', 'nj', 'ni',),
            attrs={
                'long_name': "time difference from reference time",
                'coverage_content_type': "coordinate",
                'units': "s",
                'grid_mapping': "lambert_Azimuthal_Grid",
                'comment': 'time plus sst_dtime gives seconds after 00:00:00 UTC January 1, 1981'
            }),
        'sea_surface_temperature': xr.DataArray(
            data=np.ones((1, 40000, 1000), dtype=np.int16), 
            dims=('time', 'nj', 'ni',),
            attrs={
                'long_name': "Skin temperature of the sea surface",
                'standard_name': "sea_surface_skin_temperature",
                'coverage_content_type': "physicalMeasurement",
                'units': "K",
                'grid_mapping': "Lambert_Azimuthal_Grid",
            }),
    }
)


ds['time'].encoding['units'] = "seconds since 1981-01-01 00:00:00"

ds['lat'].encoding['_FillValue'] = None
ds['lon'].encoding['_FillValue'] = None

ds['sea_surface_temperature'].encoding['_FillValue'] = np.int16(-32768)
ds['sea_surface_temperature'].encoding['add_offset'] = 273.15
ds['sea_surface_temperature'].encoding['scale_factor'] = 0.01
ds['sea_surface_temperature'].encoding['dtype'] = np.int16
ds['sea_surface_temperature'].attrs['valid_range'] = [np.int16(-200), np.int16(5000)]

ds['sst_dtime'].encoding['_FillValue'] = np.int16(-32768)
ds['sst_dtime'].encoding['add_offset'] = 0.
ds['sst_dtime'].encoding['scale_factor'] = 1.
ds['sst_dtime'].encoding['dtype'] = np.int16
ds['sst_dtime'].attrs['valid_range'] = [np.int16(-32767), np.int16(32767)]

ds.to_netcdf('samples/nonregular_grid_projection.nc', unlimited_dims='time')


