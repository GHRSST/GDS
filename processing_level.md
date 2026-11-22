(product_levels)=
# Processing level

Satellite processing levels classify Earth observation data based on how much computer processing, calibration, and 
spatial or temporal transformation has been applied since the sensor recorded it. GHRSST relies on classic international
conventions, such as CEOS [^footnote1], classifying Earth observation satellite processing level from Level 0 to Level 4:

```{table} Processing Level Conventions and Codes
:name: processing_level
**Level**|**<Processing Level> Code**|**Description**
-----|-----|-----
Level 0 | L0 | Unprocessed instrument and payload data at full resolution. GHRSST does not make recommendations regarding formats or content for data at this processing level.
Level 1A| L1A| Reconstructed unprocessed instrument data at full resolution, time referenced, and annotated with ancillary information, including radiometric and geometric calibration coefficients and geo-referencing parameters, computed and appended, but not applied, to L0 data. GHRSST does not make recommendations regarding formats or content for data at this processing level.
Level 1B| L1B| Level 1A data that have been processed to sensor units. GHRSST does not currently make recommendations regarding formats or content for L1B data.
Level 2 | L2 | Geophysical variables derived from Level 1 source data at the same resolution and location as the Level 1 data, typically in a satellite projection with geographic information.
Level 3 | L3 | Level 2 variables mapped on a defined grid with reduced requirements for ancillary data. 
Level 4 | L4 | Datasets created from the analysis of lower level data that result in gridded, gap-free products.
```

GHRSST extends the concept of Level 2 (L2) to **Level 2 Pre-processed (L2P)** processing level: all L2P files require a full 
set of extensive ancillary data such as wind speeds and times of observation that are provided as ‘dynamic flags’ that 
users can manipulate to filter data according to their own quality criteria.  L2P files form the basis of higher-level 
products and are often the best level products for data assimilation. The requirement for dynamic flags is particularly 
important in this context.

GHRSST also refines further the concept of L3 by defining **L3U, L3C, L3S sublevels**. Higher-level L3 products are often 
intended for general use or created for input to Level 4 analysis systems so the requirement for extensive ancillary data 
is reduced. Since some GHRSST producers only process data natively on grids (especially in the case of geostationary 
platform observations), the GDS {{gds_version}} L3 specification is flexible enough to allow for the creation of L3 files 
which meet all the content requirements of a L2P file (L3U, L3C). In all L2P and L3 cases, uncertainty estimates are 
mandatory.

Satellite data processing level definitions can lead to ambiguous situations, especially regarding the distinction between
L3 and L4 products. GHRSST identified for **L4** the use of analysis procedures to fill gaps where no observations exist to 
resolve this ambiguity. If no gap filling procedure (such as optimal interpolation) is used, then the product remains a 
L3 GHRSST product (**L3S**, for multi-sensor products).

Overall, GHRSST currently establishes standards for L2P ({numref}`l2p`), L3U, L3C, L3S ({numref}`l3`), and L4 ({numref}`l4`) as 
summarized in {numref}`_product_levels`.


```{table} Summary description of GHRSST processing levels
:name: _product_levels

| SST Product         | L2 Pre-Processed {numref}`l2p`  | L3 Uncollated  {numref}`l3`  | L3 Collated  {numref}`l3`   | L3 Super-collated  {numref}`l3`  | Analyzed SST  {numref}`l4`   |
|:--------------------|:--------------------------------|:------------------------------|:-----------------------------|:----------------------------------|:-----------------------------|
| Acronym             | L2P                                                                                                                                                                                                                                                                                                                                                       | L3U                                                                                                   | L3C                                                                                                 | L3S                                                                                        | L4                                                                                                                                                                  |
| Description         | Geophysical variables derived from Level 1 source data at the same resolution and location as the Level 1 data, typically in a satellite projection with geographic information. These data form the fundamental basis for higher-level GHRSST products and require ancillary data and uncertainty estimates. No adjustments to input SST have been made. | L2 data granules remapped to a space grid without combining any observations from overlapping orbits. | SST measurements combined from a single instrument into a space-time grid.                          | Multiple passes/scenes of data from multiple instruments can be combined. Adjustments may be made to input SST data. | SST measurements combined from multiple instruments into a space-time grid. Multiple passes/scenes of data are combined. Adjustments may be made to input SST data. | Data sets created from the analysis of lower level data that results in gridded, gap-free products. SST data generated from multiple sources of satellite data using optimal interpolation are an example of L4 GHRSST products |
| Grid specification  | Native to SST data format                                                                                                                                                                                                                                                                                                                                 | Defined by data provider                                                                              | Defined by data provider                                                                            | Defined by data provider                                                                   | Defined by data provider                                                                                                                                            |
| Temporal resolution | Native to SST data stream                                                                                                                                                                                                                                                                                                                                 | Native to data stream                                                                                 | Defined by data provider                                                                            | Defined by data provider                                                                   | Defined by data provider                                                                                                                                            |
| Delivery timescale  | As available, Ideally within 3 hours from acquisition at satellite                                                                                                                                                                                                                                                                                        | As available, Ideally within 3 hours from acquisition at satellite                                    | As available, Ideally within 3 hours from acquisition at satellite                                  | As available, Ideally within 3 hours from acquisition at satellite                         | Analyzed product processing window as defined by data provider.                                                                                                     |
| Target accuracy     | Native to data stream                                                                                                                                                                                                                                                                                                                                     | Native to data stream                                                                                 | <0.4 K                                                                                              | <0.4 K                                                                                     | < 0.4 K absolute, 0.1 K relative                                                                                                                                    |
| Error statistics    | Native to data stream if available, sensor specific error statistics otherwise                                                                                                                                                                                                                                                                            | Native to data stream if available, sensor specific error statistics otherwise                        | Derived from input data for each output grid point.                                                 | Derived from input data for each output grid point.                                        | Analysis error defined by data provider for each output grid point (no input data statistics are retained)                                                          |
| Coverage            | Native to data stream                                                                                                                                                                                                                                                                                                                                     | Native to data stream                                                                                 | Defined by data provider                                                                            | Defined by data provider                                                                   | Defined by data provider                                                                                                                                            |
```


[^footnote1]: https://calvalportal.ceos.org/cal/val-wiki/-/wiki/CEOS_Terms_and_Definitions/Processing+Levels