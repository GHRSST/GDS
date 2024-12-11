'''
Create GDS Compliant L4 from an existing (imperfect) L4 
'''

import xarray as xr
import numpy as np

ds = xr.open_dataset('samples/20240229000000-IFR-L4_GHRSST-SSTfnd-ODYSSEA-GLOB_010-v02.1-fv01.0.nc')

ds['lat'].encoding['_FillValue'] = None
ds['lat'].attrs['coverage_content_type'] = 'coordinate'

ds['lon'].encoding['_FillValue'] = None
ds['lon'].attrs['coverage_content_type'] = 'coordinate'

ds['time'].encoding['_FillValue'] = None
ds['time'].attrs['coverage_content_type'] = 'coordinate'

ds['analysed_sst'].attrs['units'] = 'K'
ds['analysed_sst'].attrs['coverage_content_type'] = 'physicalMeasurement'
ds['analysed_sst'].attrs.pop('valid_min')
ds['analysed_sst'].attrs.pop('valid_max')

ds['analysis_error'].attrs['units'] = 'K'
ds['analysis_error'].attrs['coverage_content_type'] = 'qualityInformation'
ds['analysis_error'].attrs.pop('valid_min')
ds['analysis_error'].attrs.pop('valid_max')

ds['sea_ice_fraction'].attrs['units'] = '1'
ds['sea_ice_fraction'].attrs['coverage_content_type'] = 'auxiliaryInformation'
ds['sea_ice_fraction'].attrs.pop('valid_min')
ds['sea_ice_fraction'].attrs.pop('valid_max')
ds['sea_ice_fraction'].attrs['source'] = ds['sea_ice_fraction'].attrs.pop('source_data')

ds['sea_ice_fraction_error'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="Sea ice area fraction error estimate",
        units='1',
        source="EUMETSAT SAF O&SI sea ice version 1.0",
        scale_factor=0.01,
        add_offset=0.0,
        coverage_content_type="auxiliaryInformation",
        comment="This will be different for each system"
))
ds['sea_ice_fraction_error'].encoding['_FillValue'] = np.int16(-128)


ds['sst_anomaly'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int16),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="SST anomaly from a seasonal SST climatology based on data over 2003-2014 period",
        units='K',
        source="ODYSSEA L4",
        scale_factor=0.001,
        add_offset=0.0,
        coverage_content_type="auxiliaryInformation",
        comment="anomaly reference to the day-of-year average between 2003 and 2014"
))
ds['sst_anomaly'].encoding['_FillValue'] = np.int16(-32768)



ds.to_netcdf('./samples/l4_full_example.nc')
