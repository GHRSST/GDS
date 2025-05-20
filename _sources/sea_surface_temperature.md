# Sea Surface Temperature

SST is a challenging parameter to define precisely as the upper ocean (~10 m) has a complex and variable vertical temperature structure that is related to ocean turbulence and air-sea fluxes of heat, moisture and momentum. A theoretical framework is therefore required to understand the information content and relationships between measurements of SST made by different satellites and in situ instruments, especially if these are to be merged together. The definitions of SST developed by the GHRSST SST Science Team (agreed at the 2nd and 3rd workshops) achieve the closest possible coincidence between what is defined and what can be measured, taking into account current scientific knowledge and understanding of the near-surface thermal structure of the ocean.

The definitions of SST defined by GHRSST are currently being refined by the Science Team. Once approved, the GHRSST SST definitions will be iterated with the Climate and Forecast (CF) metadata convention definitions of SST to ensure they are in agreement.

The figure below presents a schematic diagram that summarises the definition of SST in the upper 10 m of the ocean and provides a framework to understand the differences between complementary SST measurements. It encapsulates the effects of dominant heat transport processes and time scales of variability associated with distinct vertical and volume regimes of the upper ocean water column (horizontal and temporal variability is implicitly assumed).

```{figure} images/sst-definition.gif
---
name: sst_definition
---
Overview of SST measurement types used within GHRSST
```


CF Definition: 
> sea_surface_temperature is usually abbreviated as "SST". It is the temperature of sea water near the surface (including the part under sea-ice, if any), and not the interface temperature, whose standard name is surface_temperature. For the temperature of sea water at a particular depth or layer, a data variable of sea_water_temperature with a vertical coordinate axis should be used.

```{admonition} Additional details
The interface temperature (SSTint) is a theoretical temperature at the precise air-sea interface. It represents the hypothetical temperature of the topmost layer of the ocean water and could be thought of as an even mix of water and air molecules. SSTint is of no practical use because it cannot be measured using current technology. It is important to note that it is the SSTint that interacts with the atmosphere. Within GHRSST, most variables containing SST are named “sea_surface_temperature” to simplify the development of client applications wishing to read these variables.  The variable attribute “standard_name” indicates the precise form of the SST, using the following definitions. More detail is given in the Level 2P (Section 9), Level 3 (Section 10), and Level 4  (Section 11) specification.
```


**Sea_surface_skin_temperature (GHRSST <SST Type>: SSTskin):**

CF Definition: 
> The surface called "surface" means the lower boundary of the atmosphere. The sea surface skin temperature is the temperature measured by an infrared radiometer typically operating at wavelengths in the range 3.7 - 12 micrometers. It represents the temperature within the conductive diffusion-dominated sub-layer at a depth of approximately 10 - 20 micrometers below the air-sea interface. Measurements of this quantity are subject to a large potential diurnal cycle including cool skin layer effects (especially at night under clear skies and low wind speed conditions) and warm layer effects in the daytime. 

```{admonition} Additional Details:
The sea surface skin temperature (SSTskin) as defined above represents the actual temperature of the water across a very small depth of approximately 20 micrometers. This definition is chosen for consistency with the majority of infrared satellite and ship mounted radiometer measurements. 
```

**Sea_surface_subskin_temperature (GHRSST <SST Type>: SSTsubskin):**

CF Definition: 
> The surface called "surface" means the lower boundary of the atmosphere. The sea surface subskin temperature is the temperature at the base of the conductive laminar sub-layer of the ocean surface, that is, at a depth of approximately 1 - 1.5 millimetres below the air-sea interface. For practical purposes, this quantity can be well approximated to the measurement of surface temperature by a microwave radiometer operating in the 6 - 11 gigahertz frequency range, but the relationship is neither direct nor invariant to changing physical conditions or to the specific geometry of the microwave measurements. Measurements of this quantity are subject to a large potential diurnal cycle due to thermal stratification of the upper ocean layer in low wind speed high solar irradiance conditions. 

```{admonition} Additional Details: 
The sea surface subskin temperature (SSTsubskin) represents the temperature at the base of the thermal skin layer. The difference between SSTint and SSTsubskin is related to the net flux of heat through the thermal skin layer. SSTsubskin is the temperature of a layer approximately 1 mm thick at the ocean surface.
```

**Sea_water_temperature (GHRSST <SST Type>: SSTdepth or SSTz):**

CF Definition:
> The general term, "bulk" sea surface temperature, has the standard name sea_surface_temperature with no associated vertical coordinate axis. The temperature of sea water at a particular depth (other than the foundation level) should be reported using the standard name sea_water_temperature and, wherever possible, supplying a vertical coordinate axis or scalar coordinate variable. 

```{admonition} Additional Details:
Sea water temperature (SSTdepth or SSTz, for example SST1.5m) is the terminology adopted by GHRSST to represent in situ measurements near the surface of the ocean that have traditionally been reported simply as SST or "bulk" SST. For example SST6m would refer to an SST measurement made at a depth of 6 m.  Without a clear statement of the precise depth at which the SST measurement was made, and the circumstances surrounding the measurement, such a sample lacks the information needed for comparison with, or validation of satellite-derived estimates of SST using other data sources. The terminology has been introduced to encourage the reporting of depth (z) along with the temperature. 
```

All measurements of water temperature beneath the SSTsubskin are obtained from a wide variety of sensors such as drifting buoys having single temperature sensors attached to their hull, moored buoys that sometimes include deep thermistor chains at depths ranging from a few meters to a few thousand meters, thermosalinograph (TSG) systems aboard ships recording at a fixed depth while the vessel is underway, Conductivity Temperature and Depth (CTD) systems providing detailed vertical profiles of the thermohaline structure used during hydrographic surveys and to considerable depths of several thousand meters, and various expendable bathythermograph systems (XBT). In all cases, these temperature observations are distinct from those obtained using remote sensing techniques and measurements at a given depth should be referred to as sea_water_temperature qualified by a depth in meters rather than sea surface temperatures. The situation is complicated further when one considers ocean model outputs for which the SST may be the mean SST over a layer of the ocean several tens of meters thick.


**Sea_surface_foundation_temperature (GHRSST <SST Type>: SSTfnd):**

CF Definition: 
> The surface called "surface" means the lower boundary of the atmosphere. The sea surface foundation temperature is the water temperature that is not influenced by a thermally stratified layer of diurnal temperature variability (either by daytime warming or nocturnal cooling). The foundation temperature is named to indicate that it is the temperature from which the growth of the diurnal thermocline develops each day, noting that on some occasions with a deep mixed layer there is no clear foundation temperature in the surface layer. In general, sea surface foundation temperature will be similar to a night-time minimum or pre-dawn value at depths of between approximately 1 and 5 meters. In the absence of any diurnal signal, the foundation temperature is considered equivalent to the quantity with standard name sea_surface_subskin_temperature. The sea surface foundation temperature defines a level in the upper water column that varies in depth, space, and time depending on the local balance between thermal stratification and turbulent energy and is expected to change slowly over the course of a day. If possible, a data variable with the standard name sea_surface_foundation_temperature should be used with a scalar vertical coordinate variable to specify the depth of the foundation level. Sea surface foundation temperature is measured at the base of the diurnal thermocline or as close to the water surface as possible in the absence of thermal stratification. Only in situ contact thermometry is able to measure the sea surface foundation temperature. Analysis procedures must be used to estimate sea surface foundation temperature value from radiometric satellite measurements of the quantities with standard names sea_surface_skin_temperature and sea_surface_subskin_temperature. Sea surface foundation temperature provides a connection with the historical concept of a "bulk" sea surface temperature considered representative of the oceanic mixed layer temperature that is typically represented by any sea temperature measurement within the upper ocean over a depth range of 1 to approximately 20 meters. The general term, "bulk" sea surface temperature, has the standard name sea_surface_temperature with no associated vertical coordinate axis. Sea surface foundation temperature provides a more precise, well-defined quantity than "bulk" sea surface temperature and, consequently, is more representative of the mixed layer temperature. The temperature of sea water at a particular depth (other than the foundation level) should be reported using the standard name sea_water_temperature and, wherever possible, supplying a vertical coordinate axis or scalar coordinate variable.

```{admonition} Additional Details: 
Through the definition of the CF standard names, GHRSST is attempting to discourage the use of the term “bulk SST”, replacing it instead with sea_water_temperature (SSTdepth) and a depth coordinate, or sea_surface_foundation_temperature (SSTfnd) and a depth coordinate if possible, if the observation comes from the base of the diurnal thermocline.
```


**Blended SST (GHRSST <SST Type>: SSTblend):**
In addition to the CF standard names defined above, GHRSST also uses the term “Blended SST” for ambiguous cases when the depth or type of SST is not well known.  This ambiguity in depth may arise in some L4 analysis products that merge multiple types of SST from satellite and in situ observations. Note, however, that many L4 analysis systems do attempt to specifically create a sea surface foundation temperature, SSTfnd.
