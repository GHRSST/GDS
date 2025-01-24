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
        'nj': xr.DataArray(
            data=np.ones(40000, dtype=np.float32), 
            dims=('nj',),
            attrs={
                'long_name': "y coordinate of projection",
                'standard_name': "projection_y_coordinate",
                'axis': 'Y',
                'coverage_content_type': "coordinate",
                'units': "radian",
                'valid_range': [np.float32(-0.151844), np.float32(0.151844)]
            }),
        'ni': xr.DataArray(
            data=np.ones(1000, dtype=np.float32), 
            dims=('ni',),
            attrs={
                'long_name': "x coordinate of projection",
                'standard_name': "projection_x_coordinate",
                'axis': 'X',
                'coverage_content_type': "coordinate",
                'units': "radian",
                'valid_range': [np.float32(-0.151844), np.float32(0.151844)]
            }),
        'geostationary': xr.DataArray(
            data=np.int32(0),
            dims=(),
            attrs={
                'grid_mapping_name': 'geostationary',
                'semi_major_axis': 6378137.,
                'semi_minor_axis': 6356752.314245,
                'inverse_flattening': 298.257223563,
                'perspective_point_height': 35786023.,
                'longitude_of_projection_origin': 0.,
                'latitude_of_projection_origin': -75.,
                'false_easting': 0.,
                'false_northing': 0.,
                'sweep_angle_axis': 'x',
                'horizontal_datum_name': "WGS_1984",
                'reference_ellipsoid_name': "WGS 84",
                'prime_meridian_name': "Greenwich",
                'geographic_crs_name': "GEOS"
            })
    },
    data_vars={
        'sst_dtime': xr.DataArray(
            data=np.ones((1, 40000, 1000), dtype=np.int16), 
            dims=('time', 'nj', 'ni',),
            attrs={
                'long_name': "time difference from reference time",
                'coverage_content_type': "coordinate",
                'units': "s",
                'grid_mapping': "geostationary",
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
                'grid_mapping': "geostationary",
                'comment': 'These SST values are representative of the top 10 micrometers of the sea surface over the native geostationary satellite grid'
            }),
    }
)


ds['time'].encoding['units'] = "seconds since 1981-01-01 00:00:00"

ds['ni'].encoding['_FillValue'] = None
ds['nj'].encoding['_FillValue'] = None

ds['sea_surface_temperature'].encoding['_FillValue'] = np.int16(-32768)
ds['sea_surface_temperature'].attrs['add_offset'] = 273.15
ds['sea_surface_temperature'].attrs['scale_factor'] = 0.01
ds['sea_surface_temperature'].encoding['dtype'] = np.int16
#ds['sea_surface_temperature'].attrs['valid_range'] = [np.int16(-200),
# np.int16(5000)]

ds['sst_dtime'].encoding['_FillValue'] = np.int16(-32768)
ds['sst_dtime'].attrs['add_offset'] = 0.
ds['sst_dtime'].attrs['scale_factor'] = 1.
ds['sst_dtime'].encoding['dtype'] = np.int16
#ds['sst_dtime'].attrs['valid_range'] = [np.int16(-32767), np.int16(32767)]

ds.to_netcdf('samples/nonregular_grid_projection_no_latlon.nc', unlimited_dims='time')


