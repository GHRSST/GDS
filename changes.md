# History of changes

## GDS-{{gds_version}} 

```{warning}
Products in GDS-3.* version are not backward compatible with GDS-2.* products. Users need to revise their reading and 
processing procedures.
```

- filenaming and product identifier convention was changed for improved consistency and allow for multiple sea and 
  sea-ice temperature
- `total_water_vapour_content` added to the list of L2P/L3U/L3C auxiliary weather fields
- completely revised uncertainty variables, replacing former `sses_bias` and `sses_standard_deviation`
- added rules to better optimize NetCDF format (chunking, metadata storage) for cloud computing infrastructures
- added rules to include multiple water and even surface (e.g. sea ice) temperature variables within GHRSST products