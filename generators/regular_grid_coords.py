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
            data=np.ones(1800, dtype=np.float32), 
            dims=('lat',),
            attrs={
                'axis': 'Y',
                'long_name': "latitude",
                'standard_name': "latitude",
                'coverage_content_type': "coordinate",
                'units': "degrees_north",
                'comment': 'geographical coordinates, WGS84 projection',
                'valid_range': [-90., 90.]
            }),
        'lon': xr.DataArray(
            data=np.ones(3600, dtype=np.float32), 
            dims=('lon',),
            attrs={
                'axis': 'X',
                'long_name': "longitude",
                'standard_name': "longitude",
                'coverage_content_type': "coordinate",
                'units': "degrees_east",
                'comment': 'geographical coordinates, WGS84 projection',
                'valid_range': [-180., 180.]
            }),
    },
    data_vars={
        'sst_dtime': xr.DataArray(
            data=np.ones((1, 1800, 3600), dtype=np.int16), 
            dims=('time', 'lat', 'lon',),
            attrs={
                'long_name': "time difference from reference time",
                'coverage_content_type': "coordinate",
                'units': "s",
                'comment': 'time plus sst_dtime gives seconds after 00:00:00 UTC January 1, 1981'
            }),
        'sea_surface_temperature': xr.DataArray(
            data=np.ones((1, 1800, 3600), dtype=np.int16), 
            dims=('time', 'lat', 'lon',),
            attrs={
                'long_name': "Skin temperature of the sea surface",
                'standard_name': "sea_surface_skin_temperature",
                'coverage_content_type': "physicalMeasurement",
                'units': "K",
                'comment': "These SST values are representative of the top 10 micrometers of the sea surface and were generated on a regular grid"
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

ds.to_netcdf('./samples/regular_grid.nc', unlimited_dims='time')


