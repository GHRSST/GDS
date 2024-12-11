# GDS Filenames and Supporting Conventions
Striving to achieve a flexible naming convention that maintains consistency across processing levels and better serves user needs, the GDS uses a single form for all GHRSST data files.  An overview of the format is presented below in {numref}`overview_filenaming` along with example filenames. Details on each of the filename convention components are provided in {numref}`indicative_date` through {numref}`segregator`. 

In addition, a best practice has been established for creating character strings used to describe GHRSST SST products and sources of ancillary data.  These strings, and associated numeric codes for the SST products, are used within some GHRSST data files but are not part of the filename convention itself.  The best practice is described in {numref}`product_codes`.

(overview_filenaming)=
## Overview of Filename Convention and Example Filenames
The filenaming convention for the GDS {{gds_version}} is shown below:

**`<Indicative Date><Indicative Time>-<RDAC>-<Processing Level>_GHRSST-<SST Type>-<Product String>-<Additional Segregator>-v<GDS Version>-fv<File Version>.<File Type>`**

The variable components within braces (“< >”) are summarized in {numref}`filenaming_components` below and detailed in the following sections.  Note that dashes (“-“) **are reserved** to separate elements of the file name and **should not** be used in any GHRSST code or the `<Additional Segregator>` element.  Example filenames are given later in this section.  While no strict limit to filename length is mandated, RDACs are encouraged to keep the length to less than 240 characters to increase readability and usability.


```{table} Filenaming convention components.
:name: filenaming_components
**Name**|**Definition**|**Description**
-----|-----|-----
`<Indicative Date>`|YYYYMMDD|The identifying date for this data set. See {numref}`indicative_date`.
`<Indicative Time>`|HHMMSS|The identifying time for this data set.  The time used is dependent on the <Processing Level> of the data set:<br>&emsp;       L2P: start time of granule<br>&emsp;  L3U: start time of granule<br>&emsp;  L3C and L3S: centre time of the collation window<br>&emsp; L4 and GMPE: nominal time of analysis<br>All times should be given in UTC. See {numref}`indicative_time`.
`<RDAC>`|The RDAC where the file was created|The Regional Data Assembly Centre (RDAC) code, listed in the GHRSST reference tables at {{gds_reference_tables}}. See {numref}`rdac`.
`<Processing Level>`|The data processing level code (L2P, L3U, L3C, L3S, or L4)|The data processing level code, defined in {numref}`processing_levels`.
`<SST Type>`|The type of SST data included in the file.|Conforms to the GHRSST definitions for SST, defined in {numref}`sst_type`.
`<Product String>`|A character string identifying the SST product set.  The string is used uniquely within an RDAC but may be shared across RDACs.|The unique “name” within an RDAC of the product line.  See {numref}`product_codes` for the product string lists, one each for L2P, L3, L4, and GMPE products.  See {numref}`product_string`.
`<Additional Segregator>`|Optional text to distinguish between files with the same <Product String>. Dashes are not allowed within this element.|This text is used since the other filename components are sometimes insufficient to uniquely identify a file.  For example, in L2P or L3U (un-collated) products this is often the original file name or processing algorithm. Note, underscores should be used, not dashes. For L4 files, this element should begin with the appropriate regional code as defined in Section . This component is optional but must be used in those cases were non-unique filenames would otherwise result.
`<GDS Version>`|nn.n |Version number of the GDS used to process the file. For example, GDS-2.1 = “02.1”.
`<File Version>`|xx.x|Version number for the file, for example, “01.0”.
`<File Type>`|netCDF data file suffix (nc) or ISO metadata file suffix (xml)|Indicates this is a netCDF file containing data or its corresponding ISO-19115 metadata record in XML.
```


**L2_GHRSST Filename Example**
`20070503132300-NAVO-L2P_GHRSST-SSTblend-AVHRR17_L-SST_s0123_e0135-v02.1-fv01.0.nc`

The above file contains GHRSST L2P blended SST data for 03 May 2007, from AVHRR LAC data collected from the NOAA-17 platform.  The granule begins at 13:23:00 hours. It is version 1.0 of the file and was produced by the NAVO RDAC in accordance with the GDS {{gds_version}}.  The `<Additional Segregator>` text is "SST_s0123_e0135". 

**L3_GHRSST Filename Example**
`20070503110153-REMSS-L3C_GHRSST-SSTsubskin-TMI-tmi_20070503rt-v02.1-fv01.0.nc`

The above file was produced by the REMSS RDAC and contains collated L3 sub-skin SST data from the TMI instrument for 03 May 2007. The collated file has a centre time of at 11:01:53 hours. It is version 1.0 of the file and was produced according to GDS {{gds_version}} specifications.  Its `<Additional Segregator>` text is “tmi_20070503rt”.
	
**L4_GHRSST Filename Example**
`20070503120000-UKMO-L4_GHRSST-SSTfnd-OSTIA-GLOB-v02.1-fv01.0.nc`

The above file contains L4 foundation SST data produced at the UKMO RDAC using the OSTIA system.  It is global coverage, contains data for 03 May 2007, was produced to GDS {{gds_version}} specifications and is version 1.0 of the file.   The nominal time of the OSTIA analysis is 12:00:00 hours.

(indicative_date)=
## `<Indicative Date>`
The identifying date for this data set, using the format YYYYMMDD, where YYYY is the four-digit year, MM is the two-digit month from 01 to 12, and DD is the two-digit day of month from 01 to 31.  The date used should best represent the observation date for the dataset.

(indicative_time)=
## `<Indicative Time>`
The identifying time for this data set in UTC, using the format HHMMSS, where HH is the two-digit hour from 00 to 23, MM is the two-digit minute from 00 to 59, and SS is the two-digit second from 00 to 59.  The time used is dependent on the `<Processing Level>` of the data set:
  
- L2P: start time of granule
- L3U: start time of granule
- L3C and L3S: centre time of the collation window
- L4 and GMPE: nominal time of analysis

All times should be given in UTC and should be chosen to best represent the observation time for this dataset.  Note: RDACs should ensure the applications they use to determine UTC proprerly account for leap seconds.

(rdac)=
## `<RDAC>`
Codes used for GHRSST Regional Data Assembly Centres (RDACs) are available on the GHRSST website (https://www.ghrsst.org/resources/ghrsst-data-specification-gds-tables/). New codes are assigned by the GHRSST Data And Systems Technical Advisory Group (DAS-TAG) and entered into the table upon agreement by the GDAC, LTSRF, and relevant RDACs.

(processing_levels)=
## `<Processing Level>`
Satellite data processing level definitions can lead to ambiguous situations, especially regarding the distinction between L3 and L4 products. GHRSST identified the use of analysis procedures to fill gaps where no observations exist to resolve this ambiguity. Within GHRSST filenames, the `<Processing Level>` codes are shown below in {numref}`processing_level`. GHRSST currently establishes standards for L2P, L3U, L3C, L3S, and L4 (GHRSST Multi-Product Ensembles known as GMPE are a special kind of L4 product for which GHRSST also provides standards).


```{table} GHRSST Processing Level Conventions and Codes
:name: processing_level
**Level**|**<Processing Level> Code**|**Description**
:-----:|:-----:|:-----:
Level 0|L0|Unprocessed instrument and payload data at full resolution. GHRSST does not make recommendations regarding formats or content for data at this processing level.
Level 1A|L1A|Reconstructed unprocessed instrument data at full resolution, time referenced, and annotated with ancillary information, including radiometric and geometric calibration coefficients and geo-referencing parameters, computed and appended, but not applied, to L0 data. GHRSST does not make recommendations regarding formats or content for data at this processing level.
Level 1B|L1B|Level 1A data that have been processed to sensor units. GHRSST does not currently make recommendations regarding formats or content for L1B data.
Level 2 Pre-processed|L2P|Geophysical variables derived from Level 1 source data at the same resolution and location as the Level 1 data, typically in a satellite projection with geographic information.  These data form the fundamental basis for higher-level GHRSST products and require ancillary data and uncertainty estimates.
Level 3|L3U L3C L3S|Level 2 variables mapped on a defined grid with reduced requirements for ancillary data. Uncertainty estimates are still mandatory. Three types of L3 products are defined:  Un-collated (L3U): L2 data granules remapped to a space grid without combining any observations from overlapping orbits Collated (L3C): observations combined from a single instrument into a space-time grid Super-collated (L3S): observations combined from multiple instruments into a space-time grid.    Note that L3 GHRSST products do not use analysis or interpolation procedures to fill gaps where no observations are available.
Level 4|L4|Data sets created from the analysis of lower level data that result in gridded, gap-free products.  SST data generated from multiple sources of satellite data using optimal interpolation are an example of L4 GHRSST products.  GMPE products are a type of L4 dataset.
```



Note that within GHRSST, all L2P files require a full set of extensive ancillary data such as wind speeds and times of observation that are provided as ‘dynamic flags’ that users can manipulate to filter data according to their own quality criteria.  L2P files form the basis of higher-level products and are often the best level products for data assimilation. The requirement for dynamic flags is particularly important in this context.  Higher-level L3 products are often intended for general use or created for input to Level 4 analysis systems so the requirement for extensive ancillary data is reduced. Since some GHRSST RDACs only process data natively on grids (especially in the case of geostationary platform observations), the GDS {{gds_version}} L3 specification is flexible enough to allow for the creation of L3 files which meet all the content requirements of a L2P file. In all L2P and L3 cases, bias and standard deviation uncertainty estimates are mandatory.

The distinction between L3 GHRSST and L4 GHRSST data is made primarily on whether or not any gap-filling techniques are employed, not on whether data from multiple instruments is used in the L3 product.  If no gap filling procedure (such as optimal interpolation) is used, then the product remains a L3 GHRSST product.  GHRSST defines three kinds of L3 files: un-collated (L3U), collated (L3C), and super-collated (L3S).  If gap filling is used to fill all observations gaps, then the resulting gap-free data are considered L4 GHRSST data products.

(sst_type)=
## `<SST Type>`
In conjunction with the NetCDF Climate and Forecast (CF) community [AD-9] the GHRSST Science Team agreed on the CF standard names for “SST” shown in the following figure and described in more detail below.  The names were first included in CF-1.3, and the current version of the standard name table can be found in [AD-8].  In addition, the GHRSST Science Team agreed to use the CF Naming Convention [AD-3] for variable names that do not already exist as part of the CF Convention. CF definitions are used in the GDS and across GHRSST and are shown schematically in {numref}`sst_definition`.  The different kinds of SST are detailed later in this section and the relevant `<SST Type>` codes to be used in the filenames are provided.


The SST codes and CF standard names defined above and used within GHRSST are summarized along with their key characteristics in {numref}`sst_types`.


```{table} GHRSST SST Type code and summary table
:name: sst_types
**GHRSST SST Type**|**CF Standard Name**|**Approximate Depth**|**Typically Observed by…**
-----|-----|-----|-----
SSTint|**<span style="font-family:courier;">sea\_surface\_temperature</span>**|0 meters|Not presently measureable
SSTskin|**<span style="font-family:courier;">sea\_surface\_skin\_temperature</span>**|10 – 20 micrometers|Infrared radiometers operating in a range of wavelengths form 3.7 to 12 micrometers
SSTsubskin|**<span style="font-family:courier;">sea\_surface\_subskin\_temperature</span>**|1 – 1.5 millimetres|Microwave radiometers operating in a range of frequencies from 6-11 gigahertz 
SSTdepth|**<span style="font-family:courier;">sea\_water\_temperature</span>**|Specified by vertical coordinate (e.g., SST5m)|In situ observing systems
SSTfnd|**<span style="font-family:courier;">sea\_surface\_foundation\_temperature</span>**|1-5 meters pre-dawn|In situ observing systems
SSTblend|None|Unknown|Blend of satellite and in situ observations
```

(product_string)=
## `<Product String>`
The product strings are used within the GHRSST filename convention and within
the GHRSST unique data set codes described in {numref}`product_codes`. The 
satellite platform and satellite sensor entries are also used in the netCDF 
global attributes, `platform` and `instrument` GHRSST product files.  See 
{numref}`global_attributes` for more information on the required 
**global attributes**.

In order to improve the consistency of these product strings across 
producers, and avoid maintaining specific GHRSST tables, we recommend to use 
the CEOS tables as vocabulary for satellite platform and satellite name:

- CEOS platform table: http://database.eohandbook.com/database/missiontable.aspx
- CEOS sensor table: http://database.eohandbook.com/database/instrumenttable.aspx 

```{note}
unfitted characters for file naming (like / or spaces) can be replaced with -.
```

The following code nomenclature is recommended for the single sensor products:
`<platform code>_<sensor code>(_<additional text if needed>)`

As an example, a product string for a METOP-A AVHRR product would be : _Metop-A\_AVHRR-3_

(segregator)=
## `<Additional Segregator>`
It is possible for the preceding combination of filename components to result in a non-unique filename for any GHRSST product level. In those situations, the use of the `<Additional Segregator>` must be used to ensure each distinct file has a unique file name.  In addition, RDACs are free to use this component to add other information to their file names.  Some providers, for example, use the name of the original L1b file.  Others enter start and stop times of the file in this component.  Note that in the case of GHRSST L4 files the `<Additional Segregator>` element must begin with a code that specifies the approximate region covered by the SST analysis product.  There are two primary reasons for this requirement, the first of which is to ensure uniqueness in the file names in the cases where an RDAC is using the same L4 analysis system (for example, “ODYSSEA”) to create products for multiple regions (for example, “GAL” (Galapagos Islands Region) and “MED” (Mediterranean Region)).  The second reason is that users need to quickly identify at a glance the approximate domain of the L4 products.  Users should note that the geographical coordinates associated with each area code are explicitly intended to be only approximate, and not strict. For example, an RDAC producing a near-global coverage data may choose to only produce data on a grid that extends to 85°S. Such a product would use the “GLOB” code. Users must retrieve the precise latitude and longitude limits directly from the L4 netCDF data files. 

(product_codes)=
## GHRSST Unique Text Strings and Numeric Codes
This section describes the best practices that have been developed for creating unique text strings and numeric codes that are needed in various places within some GHRSST files.  Note that these strings are not part of the filename convention described above, but, like filenames, they apply to all GHRSST product levels and so are described in this part of the GDS.

### SST Variable Text Strings and Numeric Codes
For each official GHRSST product, a unique numeric code and associated text string is defined. The string is listed in the global attribute id (see Section 8.2) for each netCDF file in the product collection.  The unique numerical values and text strings for GHRSST SST datasets are established by agreement between the relevant RDAC, GDAC, and the LSTRF, following the Best Practice defined later in this section. The GHRSST L2P, L3, L4 and GMPE product specifications ({numref}`l2p`, {numref}`l3`, {numref}`l4`, and 12, respectively) also require the providing RDAC to use these text strings directly within the netCDF global attribute **<span style="font-family:courier;">source</span>** to indicate the sources of SST used to create the product. In the event that a non-GHRSST dataset is used as a source, as in the case of an L2P product that uses a Level 1 dataset as its source, it too must have an established text string following the best practice below (to the extent possible).

The associated numeric codes are used in some L3S files, which must describe the SST sources pixel-by-pixel in a variable named **<span style="font-family:courier;">source_of_sst</span>** if more than one SST source is used.  If only one source is used, the variable **<span style="font-family:courier;">source_of_sst</span>** is not needed and instead the source is indicated simply by using the text string in the global attribute **<span style="font-family:courier;">source</span>** (see Section 8.2 and Section 10.29) as indicated earlier. 

### Ancillary and Optional Variable Text Strings and Numeric Codes
GHRSST L2P, L3, L4 and GMPE product specifications ({numref}`l2p`, {numref}`l3`, {numref}`l4`, and 12, respectively) also require the providing RDAC to indicate text strings and associated numeric codes directly within the netCDF global and variable attributes for the sea surface temperature or ancillary sea ice fraction, aerosol depth indicator, climatologies, surface solar irradiance, wind speed, and when relevant, for optional and experimental variables. These text strings and codes do not need to be unique across different data sets, but must be consistent within a given data set and clearly specified within each netCDF file.  In these cases, the variable in question should contain an attribute called **<span style="font-family:courier;">flag_meanings</span>** together with a variable called **<span style="font-family:courier;">flag_values</span>**. The **<span style="font-family:courier;">flag_values</span>** attribute shall contain a comma-separated list of the numeric codes for the sources of data used whose order matches the space-separated text strings in the **<span style="font-family:courier;">flag_meanings</span>** attribute.

### Best Practice for Establishing Character Strings
A best practice has been established for defining the text strings to be used in these GHRSST attributes. While a rigid standard for the text strings is not possible, the following best practice should be applied to the extent possible for GHRSST SST datasets and the ancillary and optional variables:

`<Product String>-<RDAC>-<Processing Level>-<Additional Segregator>-v<Product Version>`

The definitions of the components match the definitions from the file naming convention, found in {numref}`filenaming_components`. The component `<Product Version>` is used to distinguish different versions of the same dataset and should be of the form x.y where x is the major and y is the minor version. For ancillary and optional variables, an attempt should be made to follow these conventions to the extent possible. If there is no appropriate GHRSST RDAC to use in the string, then it is recommended that a commonly used acronym for the centre responsible be used. It is recommended that the `<Additional Segregator>` should be one of ICE, ADI, CLIM, SSI, and WSP, for ancillary sea ice fraction, aerosol depth indicator, climatologies, surface solar irradiance, and wind speed variables, respectively. 

Notethat many SST text strings not meeting this best practice were established under the GDS version 1 and are already in use. 

These codes are used in the GHRSST Central Catalogue as product identifiers.


