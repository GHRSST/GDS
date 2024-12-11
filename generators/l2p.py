'''
Create GDS Compliant L2P from an existing L2P 
'''

import xarray as xr
import numpy as np

ds = xr.open_dataset('samples/20240101000103-OSISAF-L2P_GHRSST-SSTsubskin-AVHRR_SST_METOP_C-sstmgr_metop03_20240101_000103-v02.0-fv01.0.nc')

ds['lat'].encoding['_FillValue'] = None
ds['lat'].attrs['coverage_content_type'] = 'coordinate'

ds['lon'].encoding['_FillValue'] = None
ds['lon'].attrs['coverage_content_type'] = 'coordinate'

ds.drop_vars('sst_dtime')
ds['sst_dtime'] = xr.DataArray(
    data=np.zeros(ds.wind_speed.shape, dtype=np.int16),
    dims=ds.wind_speed.dims,
    attrs=dict(
        long_name="time difference from reference time",
        units='s',
        scale_factor=1.,
        add_offset=0.,
        coverage_content_type="coordinate",
        comment="time plus sst_dtime gives seconds after 00:00:00 UTC January 1, 1981"
))
ds['sst_dtime'].encoding['_FillValue'] = np.int16(-32768)

ds['sea_surface_temperature'].attrs['units'] = 'K'
ds['sea_surface_temperature'].attrs['coverage_content_type'] = 'physicalMeasurement'
ds['sea_surface_temperature'].attrs.pop('valid_min')
ds['sea_surface_temperature'].attrs.pop('valid_max')

ds['sses_bias'].attrs['units'] = 'K'
ds['sses_bias'].attrs['coverage_content_type'] = 'qualityInformation'
ds['sses_bias'].attrs.pop('valid_min')
ds['sses_bias'].attrs.pop('valid_max')

ds['sses_standard_deviation'].attrs['units'] = 'K'
ds['sses_standard_deviation'].attrs['coverage_content_type'] = 'qualityInformation'
ds['sses_standard_deviation'].attrs.pop('valid_min')
ds['sses_standard_deviation'].attrs.pop('valid_max')

ds['dt_analysis'].attrs['coverage_content_type'] = 'auxiliaryInformation'
ds['dt_analysis'].attrs.pop('valid_min')
ds['dt_analysis'].attrs.pop('valid_max')
ds['dt_analysis'].attrs['units'] = 'K'

ds['wind_speed'].attrs.pop('valid_min')
ds['wind_speed'].attrs.pop('valid_max')

ds['l2p_flags'].attrs['coverage_content_type'] = 'qualityInformation'
ds['l2p_flags'].attrs.pop('valid_min')
ds['l2p_flags'].attrs.pop('valid_max')

ds['quality_level'].attrs['coverage_content_type'] = 'qualityInformation'
ds['quality_level'].attrs.pop('valid_min')
ds['quality_level'].attrs.pop('valid_max')

ds['sea_ice_fraction'].attrs['units'] = '1'
ds['sea_ice_fraction'].attrs['coverage_content_type'] = 'auxiliaryInformation'
ds['sea_ice_fraction'].attrs.pop('valid_min')
ds['sea_ice_fraction'].attrs.pop('valid_max')
ds['sea_ice_fraction'].attrs['time_offset'] = 3.

ds['aerosol_dynamic_indicator'].attrs['units'] = '1'
ds['aerosol_dynamic_indicator'].attrs['coverage_content_type'] = 'auxiliaryInformation'
ds['aerosol_dynamic_indicator'].attrs.pop('valid_min')
ds['aerosol_dynamic_indicator'].attrs.pop('valid_max')
ds['aerosol_dynamic_indicator'].attrs['source'] = 'ADI-NAVO-SDI-V2'
ds['aerosol_dynamic_indicator'].attrs['comment'] = "Estimate of the potential for aerosol contamination based on the NAVO SDI_V2 product, in counts"
ds['aerosol_dynamic_indicator'].attrs['time_offset'] = 3.

ds['satellite_zenith_angle'].attrs['coverage_content_type'] = 'auxiliaryInformation'
ds['satellite_zenith_angle'].attrs['standard_name'] = 'sensor_zenith_angle'
ds['satellite_zenith_angle'].attrs.pop('valid_min')
ds['satellite_zenith_angle'].attrs.pop('valid_max')

ds['solar_zenith_angle'].attrs['coverage_content_type'] = 'auxiliaryInformation'
ds['solar_zenith_angle'].attrs['standard_name'] = 'solar_zenith_angle'
ds['solar_zenith_angle'].attrs.pop('valid_min')
ds['solar_zenith_angle'].attrs.pop('valid_max')

ds['source_of_wind_speed'] = xr.DataArray(
    data=np.zeros(ds.wind_speed.shape, dtype=np.int8),
    dims=ds.wind_speed.dims,
    attrs=dict(
        long_name="sources of wind speed",
        flag_meanings="no_data WSP-ESA-ASCAT-V2 WSP-NCEP-Analysis-V3 WSP-ECMWF-Forecast-V6",
        flag_values=np.array([0, 1, 2, 3], dtype=np.int8),
        coverage_content_type="auxiliaryInformation",
        comment="This variable provides a pixel by pixel description of where the wind speeds were derived from."
))

ds['wind_speed_dtime_from_sst'] = xr.DataArray(
    data=np.zeros(ds.wind_speed.shape, dtype=np.int8),
    dims=ds.wind_speed.dims,
    attrs=dict(
        long_name="time difference, in hours', of wind speed measurement from sst measurement",
        units='h',
        scale_factor=0.1,
        add_offset=0.0,
        coverage_content_type="auxiliaryInformation",
        comment="the hours between the wind speed measurement and the SST observation"
))
ds['wind_speed_dtime_from_sst'].encoding['_FillValue'] = np.int8(-128)

ds['source_of_sea_ice_fraction'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="sources of sea ice fraction",
        flag_meanings="no_data CE-NSIDC-AMSRE-V3 ICE-ECMWF-Forecast-V3",
        flag_values=np.array([0, 1, 2], dtype=np.int8),
        coverage_content_type="auxiliaryInformation",
        comment="This variable provides a pixel by pixel description of where the sea ice fraction were derived from."
))

ds['sea_ice_fraction_dtime_from_sst'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="time difference, in hours, of sea ice fraction measurement from sst measurement",
        units='h',
        scale_factor=0.1,
        add_offset=0.0,
        coverage_content_type="auxiliaryInformation",
        comment="the hours between the sea ice fraction measurement and the SST observation"
))
ds['sea_ice_fraction_dtime_from_sst'].encoding['_FillValue'] = np.int8(-128)

ds['surface_solar_irradiance'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="surface solar irradiance",
        standard_name="surface_downwelling_spherical_irradiance_in_sea_water",
        units='W m-2',
        coverage_content_type="auxiliaryInformation",
        comment="The surface solar irradiance as close to the SST observation times as possible",
        scale_factor=1.36,
        add_offset=127.0,
        source = "SSI-MSG_SEVIRI-V1",
        time_offset=2.
))
ds['sea_ice_fraction_dtime_from_sst'].encoding['_FillValue'] = np.int8(-128)

ds['source_of_ssi'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="sources of surface solar irradiance",
        flag_meanings="no_data SSI-MSG_SEVIRI-V1 SSI-NOAA-GOES_E-V1 SSI-NOAA-GOES_W-V1 SSI-ECMWF-V1 SSI-NCEP-V1 SSI-NAAPS-V1 spare",
        flag_values=np.array([0, 1, 2, 3, 4, 5, 6, 7], dtype=np.int8),
        coverage_content_type="auxiliaryInformation",
        comment="This variable provides a pixel by pixel description of where the surface solar irradiances were derived from."
))


ds['ssi_dtime_from_sst'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="time difference, in hours, of surface solar irradiance measurement from sst measurement",
        units='h',
        scale_factor=0.1,
        add_offset=0.0,
        coverage_content_type="auxiliaryInformation",
        comment="the hours between the surface solar irradiance measurement and the SST observation"
))
ds['ssi_dtime_from_sst'].encoding['_FillValue'] = np.int8(-128)

ds['source_of_adi'] = ds['sources_of_adi']
ds.drop_vars('sources_of_adi')
ds['source_of_adi'].attrs.pop('valid_min')
ds['source_of_adi'].attrs.pop('valid_max')
ds['source_of_adi'].attrs['coverage_content_type'] = "auxiliaryInformation"
ds['source_of_adi'].attrs['comment'] = "This variable provides a pixel by pixel description of where aerosol optical depth were derived from"

ds['my_variable'] = xr.DataArray(
    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
    dims=ds.sea_ice_fraction.dims,
    attrs=dict(
        long_name="estimated diurnal variability",
        standard_name='<use_a_CF_standard_name_if_available>',
        units='K',
        source="MY-SOURCES-V1",
        scale_factor=1.,
        add_offset=0.0,
        coverage_content_type="auxiliaryInformation",
        comment="This field is fully documented at http://www.mysite.com/my_variable-description.html"
))
ds['my_variable'].encoding['_FillValue'] = np.int8(-128)



#xr.DataArray(
#    data=np.zeros(ds.sea_ice_fraction.shape, dtype=np.int8),
#    dims=ds.sea_ice_fraction.dims,
#    attrs=dict(
#        long_name="sources of aerosol optical depth",
#        flag_meanings="no_data ADI-NAVO-SDI-V2",
#        flag_values=np.array([0, 1], dtype=np.int8),
#        valid_range=[np.int8(0), np.int8(1)],
#        coverage_content_type="auxiliaryInformation",
#        comment="This variable provides a pixel by pixel description of where aerosol optical depth were derived from"
#))


for v in ds.variables:
    ds[v].encoding['coordinates'] = "lat lon"

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

ds.to_netcdf('./samples/l2p_full_example.nc')

