'''
Create GDS Compliant L3S from an existing L3S
'''

import xarray as xr
import numpy as np

ds = xr.open_dataset('samples/20240101000000-IFR-L3S_GHRSST-SSTfnd-ODYSSEA'
                     '-GLOB_010-v02.1-fv01.0.nc')

ds.or_longitude.attrs.pop('binning_method')
ds.or_longitude.attrs.pop('cell_methods')
ds.or_longitude.attrs.pop('valid_range')

ds.or_latitude.attrs.pop('binning_method')
ds.or_latitude.attrs.pop('cell_methods')
ds.or_latitude.attrs.pop('valid_range')

ds.or_number_of_pixels.attrs.pop('binning_method')
ds.or_number_of_pixels.attrs.pop('valid_range')

ds.bias_to_reference_sst.attrs.pop('valid_range')

ds.sources_of_sst.attrs.pop('valid_range')
ds.sources_of_sst.attrs['flag_values'] = np.concatenate(
    [[0], ds.sources_of_sst.attrs['flag_values']]).astype(np.int8)
ds.sources_of_sst.attrs['flag_meanings'] = (
        'no_data ' + ds.sources_of_sst.attrs['flag_meanings'])
ds['sources_of_sst'].encoding.pop('_FillValue')

ds['source_of_sst'] = ds['sources_of_sst']
ds = ds.drop_vars('sources_of_sst')

ds['sum_sst'] = xr.DataArray(
    data=np.zeros(ds.sea_surface_temperature.shape, dtype=np.float32),
    dims=ds.sea_surface_temperature.dims,
    attrs=dict(
        long_name="Sum of original contributing pixel sst values",
        units='K',
        coverage_content_type="auxiliaryInformation",
))
ds['sum_sst'].encoding['_FillValue'] = np.float32(1e20)

ds['sum_square_sst'] = xr.DataArray(
    data=np.zeros(ds.sea_surface_temperature.shape, dtype=np.float32),
    dims=ds.sea_surface_temperature.dims,
    attrs=dict(
        long_name="Sum of contributing pixel sst value squares",
        units='K2',
        coverage_content_type="auxiliaryInformation",
))
ds['sum_square_sst'].encoding['_FillValue'] = np.float32(1e20)

ds['adjusted_standard_deviation_error'] = xr.DataArray(
    data=np.zeros(ds.sea_surface_temperature.shape, dtype=np.int8),
    dims=ds.sea_surface_temperature.dims,
    attrs=dict(
        long_name="standard deviation error based on L2P SSES and "
                  "adjustment method",
        units='K',
        coverage_content_type="qualityInformation",
        comment='Cumulated errors of SSES and adjustment method'
))
ds['adjusted_standard_deviation_error'].encoding['_FillValue'] = np.int8(-128)
ds['adjusted_standard_deviation_error'].attrs['scale_factor'] = 0.01
ds['adjusted_standard_deviation_error'].attrs['add_offset'] = 1.0

ds['standard_deviation_to_reference_sst'] = xr.DataArray(
    data=np.zeros(ds.sea_surface_temperature.shape, dtype=np.int8),
    dims=ds.sea_surface_temperature.dims,
    attrs=dict(
        long_name="standard deviation of the reference error",
        units='K',
        coverage_content_type="qualityInformation",
        comment='This represents the error standard deviation estimate '
                'resulting from the bias estimation method'
))
ds['standard_deviation_to_reference_sst'].encoding['_FillValue'] = np.int8(-128)
ds['standard_deviation_to_reference_sst'].attrs['scale_factor'] = 0.01
ds['standard_deviation_to_reference_sst'].attrs['add_offset'] = 1.0

ds['lat'].encoding['_FillValue'] = None
ds['lon'].encoding['_FillValue'] = None

ds.attrs['publisher_email'] = 'cersat@ifremer.fr'
ds.attrs['publisher_type'] = 'institution'
ds.attrs['publisher_institution'] = 'Ifremer'


ds.to_netcdf('./samples/l3s_full_example.nc')

