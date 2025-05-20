# Overview of GHRSST and the GDS-{{gds_version}}

**GHRSST** [^footnote0] is an international consortium representing commercial 
enterprises, academic institutions, research organizations, and operational 
agencies that collaborate to provide accurate, high resolution, and consistently 
formatted SST observations and analyses from space-based platforms.

This section briefly provides information on the importance of SST, an 
overview and history of GHRSST, and context for understanding the
**GDS-{{gds_version}}**.

## The Importance of SST
Sea Surface Temperature at the ocean-atmosphere interface is a fundamental 
variable for understanding, monitoring, and predicting fluxes of heat, momentum,
and gas at a variety of scales that determine complex interactions between 
atmosphere and ocean. The ocean stores heat from the sun and redistributes it 
from the tropical regions to higher latitudes and to the less dense atmosphere 
regulating global weather and climate. Through the hydrological cycle the 
coupled system controls terrestrial life by redistributing fresh water over the 
land surface. From large ocean gyres and atmospheric circulation cells that fuel
atmospheric depression systems, storms and hurricanes with their attendant wind 
waves and storm surges, to local scale phenomena such as the generation of sea 
breezes and convection clouds, SST at the ocean-atmosphere interface has a 
significant societal impact. Accurate knowledge of global SST distribution and 
temporal variation at finer spatial resolution is needed as a key input to 
numerical weather prediction (NWP) and numerical ocean prediction (NOP) systems
to constrain the modelled upper-ocean circulation and thermal structure at 
daily, seasonal, decadal, and climatic time scales, for the exchange of energy 
between the ocean and atmosphere in coupled ocean-atmosphere models, and as
boundary conditions for ocean forecasting models. Such models are widely used 
operationally for various applications including maritime safety, military 
operations, ecosystem assessments, fisheries support, and tourism.

In addition, well-defined and quantified error estimates of SST are also 
required for climate time series that can be analysed to reveal the role of the 
ocean in short and long term climate variability. A 30 year record of satellite 
SST observations is available now, that grows on a daily basis. SST climate data
records that are used to provide the GCOS SST Essential Climate Variable (ECV)
[^footnote1], [^footnote2], [^footnote3] are essential to monitoring and 
understanding climate variability, climate-ecosystem interactions such as coral reef health and 
sustainable fisheries management, and critical issues like sea level rise and 
changing sea ice patterns.

## GHRSST History

In 1998, SST data production was considered a mature component of the observing
system with demonstrated capability and data products. However, SST product
availability was limited to a few data sets that were large, scientific in 
format and difficult to exchange in a near real time manner. Product accuracy 
was considered insufficient for the emerging NWP and NOP systems. 
Uncertainty estimates for SST products were unavailable with SST products
complicating their application by the NWP and NOP data assimilation community.
At the same time the number of applications requiring an accurate high 
resolution SST data stream was growing.

Considering these issues, the Global Ocean Data Assimilation Experiment (GODAE) 
[[^footnote4]] defined the minimum data specification required for use in operational 
ocean models, stating that SST observations with global coverage, a spatial 
resolution of 10 km and an accuracy of <0.4 K need to be updated every six 
hours [[^footnote4]].

Despite the network of SST observations from ships and buoys, the only way to 
achieve these demanding specifications was to make full use of space-based 
observations. An integrated and international approach was sought to improve 
satellite SST measurements, based on four principles:
- Respond to user SST requirements through a consensus approach,
- Organize activities according to principles of shared responsibility and 
  subsidiarity, handling matters with the lowest, smallest, or least centralized
  competent group possible,
- Develop complementarities between independent measurements from earth 
  observation satellites and in situ sensors,
- Maximize synergy benefits of an integrated SST measurement system and 
  end-to-end user service.

These foundations enabled the international ocean remote sensing community, 
marine meteorologists, Space Agencies, and ocean modellers to combine their 
energies to meet the GODAE requirements by establishing the GODAE High 
Resolution Sea Surface Temperature Pilot Project (GHRSST-PP). 
GHRSST-PP established four main tasks relevant to the development of the SST 
observing system:
- Improve SST data assembly/delivery,
- Test available SST data sources,
- Perform inter-comparison of SST products,
- Develop applications and data assimilation of SST to demonstrate the 
  benefit of the improved observing system.

GHRSST-PP successfully demonstrated that the requirements of GODAE could be met 
when significant amounts of GHRSST-PP data became available in 2006 and was 
instrumental in defining the shape and form of the modern-era SST measurement 
system and user service over the last 10 years [^footnote0].

At the end of the GODAE period in 2009, the GHRSST-PP evolved into the 
Group for High Resolution SST (GHRSST). GHRSST built on the successes of the 
pilot project phase and continued a series of international workshops that were 
held during 2000-2009. These workshops established a set of user requirements 
for all GHRSST activities in five areas:
- Scientific development and applications,
- Operational agency requirements,
- SST product specifications,
- Programmatic organization of an international SST service,
- Developing scientific techniques to improve products and exploit the observing
  system.

These requirements were critical to establishing the GHRSST framework and work plan and
formed an essential part of the GHRSST evolution. By establishing and documenting clear
requirements in a consultative manner at the start of the project and through all stages of its
development, GHRSST was able to develop confidently and purposefully to address the needs
of the international SST user community.

## GHRSST Organization
Over the last two decades, GHRSST established and now continues to provide an
internationally distributed suite of user focused services in a sustained 
Regional/Global Task Sharing (R/GTS) framework [AD-11] that addresses 
international organizational challenges and recognizes the implementing 
institutional capacities, capabilities, and funding prospects. 
Long term stewardship, user support and help services, and standards-based data
management and interoperability have been developed and are operated within the R/GTS
on a daily basis.
The first GHRSST Level 2P datasets were made available in 2006. Since then the GHRSST R/G
TS framework did not change up to 2019. Datasets produced from the collection of
international 14 Regional Data Assembly Centres (RDACs) were ingested by a Global Data
Assembly Centre (GDAC), such as the US GDAC located at the NASA Jet Propulsion Laboratory,
Physical Oceanography Active Archive Data Center PO.DAAC). These data were made
available for public distribution via a number of access protocols, tools and services, and also
staged for ingestion. Final archiving and further distribution services were performed by the
Long-term Stewardship and Reanalysis Facility (LTSRF) located at the NOAA National Center
for Environmental Information (NCEI). This initial GHRSST R/G TS Framework is presented in
Figure 6-1.

Although this initial paradigm has functioned well, it has deviated from its initial design with
the growing number of producers and datasets. As seen in the dashed box in Figure, a new
GDAC was set-up in Europe, delivering products not available at the US GDAC, while other
producers (e.g. CMEMS, Copernicus/EUMETSAT, and JAXA) are also now delivering products
through their own services without any push to a GDAC. It was recognized by the GHRSST
data management experts, through discussions from 2017 to 2019, and confirmed at the
annual GHRSST science team meetings, that a more defined sharing of data management
resources would be beneficial to the future growth of GHRSST and encourage more
participation by other potential data producers. The specification of the GHRSST data
management paradigm for the next years is the focus of the next sections.
It can be summarised by a more distributed system where no entity, but the GHRSST Project
Office, plays a central role anymore, as shown on Figure 6-2.
In the new R/G TS framework, there are now only two types of entities: data producers (GDP
or GHRSST Data Producers) and distributing centres (DAC or Data Assembly Centre). The two
roles can be combined by a single institution (for example, EUMETSAT which produces and
delivers Sentinel-3 A & B products). The GHRSST Project Office (GHRSST-PO) provides and
maintains on its portal a central catalogue of all GHRSST datasets providing collection
(dataset) level metadata, and federated search and discovery services. Each DAC must
implement a minimum set of services for granule data access, search and discovery,
production/distribution metrics and long-term archiving.


Figure 6-2: Revised architecture proposal. Multiple interfaces are now available to data producers. Each data
node implements interface, distribution, archiving and metadata services for the datasets they are
responsible for. Data and metadata from data producers (GDPs) flow first to a DAC (like PO.DAAC, before as
the US GDAC). There is no more GDAC with the commitment to host all GHRSST datasets, it is now a shared
task between DACs and some datasets can be distributed by several DACs. The GHRSST-PO portal allows the
user to discover and search all GHRSST products and granules without prior knowledge of who is the producer
or distributor.

Each component of the R/GTS is independently managed and operated by different
institutions and agencies. The R/GTS itself is coordinated by the international GHRSST Science
Team, which receives guidance and advice from the GHRSST Advisory Council. A GHRSST
Project Office coordinates the overall framework.

## Overview of the GDS-2.1
The GHRSST R/GTS was made possible through the establishment of a rigorous GHRSST
Technical Data Specification (GDS), which instructed international satellite data providers on
how to process satellite data streams, defined the format and content of the data and
metadata, and documented the basic approaches to providing uncertainty estimates and
auxiliary data sets. The GHRSST-PP established the first GDS (v1.6) [RD-1], which formed the
basis of all GHRSST data production from 2005 through today. Since 2010 the Version 2 of the
GDS has been used in operations, with minor updates occurring from time to time.
All GHRSST products entering the R/GTS must strictly follow the common GDS when
generating L2P, L3, L4, and GMPE data. As a result, users with common tools to read data
from one RDAC can securely use data from any of the others as well as the GDAC and LTSRF
without a need to re-code. Table 6-1 provides a summary of GDS-2.1 data products and their
basic characteristics.
The remainder of this document provides the detailed specifications for GHRSST L2P, L3, L4,
and GMPE products, their file naming convention, metadata requirements, and all necessary
tables, conventions, and best practices for creating and using GHRSST data.


| SST Product         | L2 Pre-Processed {numref}`l2p`                                                                                                                                                                                                                                                                                                                            | L3 Uncollated  [Section 1010]                                                                         | L3 Collated[Section 10]                                                                             | L3 Super-collated[Section 10]                                                              | Analyzed SST[Section 11]                                                                                                                                            |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Acronym             | L2P                                                                                                                                                                                                                                                                                                                                                       | L3U                                                                                                   | L3C                                                                                                 | L3S                                                                                        | L4                                                                                                                                                                  |
| Description         | Geophysical variables derived from Level 1 source data at the same resolution and location as the Level 1 data, typically in a satellite projection with geographic information. These data form the fundamental basis for higher-level GHRSST products and require ancillary data and uncertainty estimates. No adjustments to input SST have been made. | L2 data granules remapped to a space grid without combining any observations from overlapping orbits. | SST measurements combined from a single instrument into a space-time grid.                          | Multiple passes/scenes of data can be combined. Adjustments may be made to input SST data. | SST measurements combined from multiple instruments into a space-time grid. Multiple passes/scenes of data are combined. Adjustments may be made to input SST data. | Data sets created from the analysis of lower level data that results in gridded, gap-free products. SST data generated from multiple sources of satellite data using optimal interpolation are an example of L4 GHRSST products |
| Grid specification  | Native to SST data format                                                                                                                                                                                                                                                                                                                                 | Defined by data provider                                                                              | Defined by data provider                                                                            | Defined by data provider                                                                   | Defined by data provider                                                                                                                                            |
| Temporal resolution | Native to SST data stream                                                                                                                                                                                                                                                                                                                                 | Native to data stream                                                                                 | Defined by data provider                                                                            | Defined by data provider                                                                   | Defined by data provider                                                                                                                                            |
| Delivery timescale  | As available, Ideally within 3 hours from acquisition at satellite                                                                                                                                                                                                                                                                                        | As available, Ideally within 3 hours from acquisition at satellite                                    | As available, Ideally within 3 hours from acquisition at satellite                                  | As available, Ideally within 3 hours from acquisition at satellite                         | Analyzed product processing window as defined by data provider.                                                                                                     |
| Target accuracy     | Native to data stream                                                                                                                                                                                                                                                                                                                                     | Native to data stream                                                                                 | <0.4 K                                                                                              | <0.4 K                                                                                     | < 0.4 K absolute, 0.1 K relative                                                                                                                                    |
| Error statistics    | Native to data stream if available, sensor specific error statistics otherwise                                                                                                                                                                                                                                                                            | Native to data stream if available, sensor specific error statistics otherwise                        | Derived from input data for each output grid point.                                                 | Derived from input data for each output grid point.                                        | Analysis error defined by data provider for each output grid point (no input data statistics are retained)                                                          |
| Coverage            | Native to data stream                                                                                                                                                                                                                                                                                                                                     | Native to data stream                                                                                 | Defined by data provider                                                                            | Defined by data provider                                                                   | Defined by data provider                                                                                                                                            |

L3 GHRSST products do not use analysis or interpolation procedures to fill gaps 
where no observations are available


[^footnote0]: Donlon, C. J., I. Robinson, K. S Casey, J. Vazquez-Cuervo, E Armstrong, O. Arino, C.
Gentemann, D. May, P. LeBorgne, J. Piollé, I. Barton, H Beggs, D. J. S. Poulter, C. J.
Merchant, A. Bingham, S. Heinz, A Harris, G. Wick, B. Emery, P. Minnett, R. Evans, D.
Llewellyn-Jones, C. Mutlow, R. Reynolds, H. Kawamura and N. Rayner, 2007. The
Global Ocean Data Assimilation Experiment (GODAE) high Resolution Sea Surface
Temperature Pilot Project (GHRSST-PP). Bull. Am. Meteorol. Soc., Vol. 88, No. 8, pp.
1197-1213, https://doi.org/10.1175/BAMS-88-8-1197

[^footnote1]: Global Climate Observing system, 2004. Implementation plan for the 
Global observing system for climate in support of the UNFCCC, GCOS – 92, WMO/TD No. 1219, available
from World Meteorological Organization.

[^footnote2]: The Second Report on the Adequacy of the Global Observing Systems for Climate in
Support of the UNFCCC, GCOS – 82, April 2003 (WMO/TD No. 1143), Available online
at http://www.wmo.int/pages/prog/gcos/index.php

[^footnote3]: Satellite Observation of the Climate System: The Committee on 
Earth Observation Satellites (CEOS) Response to the Global Climate Observing 
System (GCOS) Implementation Plan, Available online at
http://www.ceos.org/pages/CEOSResponse_1010A.pdf

[^footnote4]: Donlon, C. J., P. Minnett, C. Gentemann, T. J. Nightingale, 
I. J. Barton, B. Ward and, J. Murray, 2002. Towards Improved Validation of 
Satellite Sea Surface Skin Temperature Measurements for Climate Research, 
J. Climate, Vol. 15, No. 4, pp. 353-369.
