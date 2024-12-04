'''
Create GDS Compliant L2P from an existing L2P 
'''

import xarray as xr

ds = xr.open_dataset('samples/20240101000103-OSISAF-L2P_GHRSST-SSTsubskin-AVHRR_SST_METOP_C-sstmgr_metop03_20240101_000103-v02.0-fv01.0.nc')

ds['lat'].encoding['_FillValue'] = None
ds['lon'].encoding['_FillValue'] = None

ds['sea_surface_temperature'].attrs['units'] = 'K'
ds['sea_surface_temperature'].attrs['coverage_content_type'] = 'physicalMeasurement'

ds['sses_bias'].attrs['units'] = 'K'
ds['sses_bias'].attrs['coverage_content_type'] = 'qualityInformation'

ds['sses_standard_deviation'].attrs['units'] = 'K'
ds['sses_standard_deviation'].attrs['coverage_content_type'] = 'qualityInformation'

ds.attrs['geospatial_lat_min'] = ds.attrs['southernmost_latitude']
ds.attrs['geospatial_lat_max'] = ds.attrs['northernmost_latitude']
ds.attrs['geospatial_lon_max'] = ds.attrs['easternmost_longitude']
ds.attrs['geospatial_lon_min'] = ds.attrs['westernmost_longitude']
ds.attrs['geospatial_bounds'] = f'POLYGON (({ds.attrs["geospatial_lat_min"]} {ds.attrs["geospatial_lon_min"]}, {ds.attrs["geospatial_lat_max"]} {ds.attrs["geospatial_lon_min"]}, {ds.attrs["geospatial_lat_max"]} {ds.attrs["geospatial_lon_max"]}, {ds.attrs["geospatial_lat_min"]} {ds.attrs["geospatial_lon_max"]}, {ds.attrs["geospatial_lat_min"]} {ds.attrs["geospatial_lon_min"]}))'

ds.attrs['geospatial_bounds_crs'] = 'WGS84'

ds.attrs['instrument'] = ds.attrs['sensor']
ds.attrs['platform'] = 'Metop-C'
ds.attrs['platform_vocabulary'] = 'CEOS mission table'
ds.attrs['instrument_vocabulary'] = 'CEOS instrument table'

ds.attrs['geospatial_vertical_min'] = 0.
ds.attrs['geospatial_vertical_max'] = 0.
ds.attrs['geospatial_vertical_positive'] = 'up'
ds.attrs['geospatial_vertical_units'] = 'meters'
ds.attrs['geospatial_bounds_vertical_crs'] = "EPSG:5831"

ds.attrs['time_coverage_start'] = '2024-01-01T00:01:03Z'
ds.attrs['time_coverage_end'] = '2024-01-01T00:04:03Z'

ds.attrs['contributor_name'] = 'Stéphane Saux-Picard'
ds.attrs['contributor_role'] = 'Principal Investigator'

ds.attrs['creator_type'] = 'group'
ds.attrs['creator_institution'] = 'Meteo-France'

ds.attrs['publisher_type'] = 'institution'
ds.attrs['publisher_institution'] = 'Ifremer'

ds.attrs['date_created'] = '2024-01-01T01:50:30Z'
ds.attrs['date_modified'] = ds.attrs['date_created']
ds.attrs['date_issued'] = ds.attrs['date_created']
ds.attrs['date_metadata_modified'] = '2020-01-01T12:00:00Z'

ds.attrs['program'] = 'Group for High Resolution Sea Surface temperature (GHRSST), EUMETSAT Satellite Application Facilities (SAF)' 




deprecated = [
    'northernmost_latitude', 'southernmost_latitude', 'easternmost_longitude', 
    'westernmost_longitude', 'sensor', 'start_time', 'stop_time'
]
for att in deprecated:
    ds.attrs.pop(att)

ds.to_netcdf('l2p_full_example.nc')

