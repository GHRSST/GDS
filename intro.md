# The Recommended GHRSST Data Specification (GDS) Version {{gds_version}}

A new generation of integrated Sea Surface Temperature (SST) data products is
being provided by the **[Group for High Resolution Sea Surface Temperature 
(GHRSST)](https://doi.org/10.1175/BAMS-88-8-1197)**. 
L2 products are provided by a variety of data providers in a common
format. L3 and L4 products combine, in near-real time, various SST data products
from several different satellite sensors and in situ observations and maintain
fine spatial and temporal resolution needed by SST inputs to a variety of ocean
and atmosphere applications in the operational and scientific communities. Other
GHRSST products provide diagnostic data sets and global multi-product ensemble
analysis products. Retrospective reanalysis products are provided in a non-real
time critical offline manner. All GHRSST products have a standard format,
include uncertainty estimates for each measurement, and are served to the
international user community free of charge through a variety of data transport
mechanisms and access points that are collectively referred to as the **GHRSST
Regional/Global Task Sharing (R/GTS) framework**.

The GHRSST Data Specification (GDS) Version {{gds_version}} is a technical
specification of GHRSST products. The GHRSST services are described in a 
separate [Architecture Document (GSA)](https://10.5281/zenodo.4700398).

The GDS technical documents are supported by a User Manual. GDS {{gds_version}}
represents a consensus opinion of the GHRSST international community on how to
optimally combine satellite and in situ SST data streams within the R/GTS. The
GDS also provides guidance on how data providers might implement SST processing
chains that contribute to the R/GTS.

This document first provides an overview of GHRSST followed by detailed
technical specifications of the adopted file naming specification and supporting
definitions and conventions used throughout GHRSST and the technical
specifications for all GHRSST Level 2P, Level 3, Level 4. 
In addition, the GDS {{gds_version}} Technical Specification provides controlled
code tables and best practices for identifying sources of SST and ancillary data
that are used within GHRSST data files.

The GDS document has been developed for data providers who wish to produce any
level of GHRSST data products and for all users wishing to fully understand
GHRSST product conventions, GHRSST data file contents, GHRSST and Climate
Forecast definitions for SST, and other useful information. For a complete
discussion and access to data products and services, see https://www.ghrsst.org,
which is a central portal for all GHRSST activities.

```{tableofcontents}
```
