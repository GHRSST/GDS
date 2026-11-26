# Uncertainties

## Overview description of the GHRSST uncertainty variables

Explain here:
- the rationale behind the expression of uncertainties in GHRSST products and to what processing level they apply or not
- the minimum requirements
- the optional requirements
- the variable attributes to further refine the uncertainty variable definition
- the requirements to relate uncertainty fields to their parent SST variable (variable attribute uncertainty_variables ... )
- references on how to estimate these uncertainties
- reference to CF Convention


```{table} Summary description of GHRSST uncertainty data records, with their applicability to a specific processing level (M: mandatory, R: recommended, O: optional, N/A: not applicable)
:name: uncertainty_variables

| Variable Name         | Description            | Units  | Science data type | L2P | L3U | L3C | L3S | L4 |
|-----------------------|------------------------|--------|-----|-----|-----|-----|-----|-----|
| [sea_surface_temperature_uncertainty](__sea_surface_temperature_uncertainty) | Total uncertainty – replaces sses_standard_deviation | K | float | M | M | M | M | ? 
| [sea_surface_temperature_uncertainty_independent](__sea_surface_temperature_uncertainty_independent) | Independent or uncorrelated uncertainty e.g. radiometric noise. Can be calculated by propagating NeDTs through retrieval. | K | float | R | R | R | R | ?
| [sea_surface_temperature_uncertainty_correlated](__sea_surface_temperature_uncertainty_correlated) | Locally correlated on synoptic scales e.g. due to atmospheric state | K | float | R | R | R | R | ?
| [sea_surface_temperature_uncertainty_common](__sea_surface_temperature_uncertainty_common) | Large scale correlated e.g. due to systematic calibration effects | K | float | R | R | R | R | ?
| [sea_surface_temperature_uncertainty_correlated_depth_adjustment](__sea_surface_temperature_uncertainty_correlated_depth_adjustment) | Can be used for uncertainty in depth adjustment if product provides separate SSTskin and SSTdepth | K | float | O | O | O | O | ?
| [uncertainty_correlated_depth_and_time_adjustment](__uncertainty_correlated_depth_and_time_adjustment) |  | K | float | O | O | O | O | ?

```

## uncertainty data record format specification

Detailed definition and description of each variable. Example CDL.

(__sea_surface_temperature_uncertainty)=
### sea_surface_temperature_uncertainty

(__sea_surface_temperature_uncertainty_independent)=
### sea_surface_temperature_uncertainty_independent

(__sea_surface_temperature_uncertainty_correlated)=
### sea_surface_temperature_uncertainty_correlated

(__sea_surface_temperature_uncertainty_common)=
### sea_surface_temperature_uncertainty_common

(__sea_surface_temperature_uncertainty_correlated_depth_adjustment)=
### sea_surface_temperature_uncertainty_correlated_depth_adjustment

(__uncertainty_correlated_depth_and_time_adjustment)=
### uncertainty_correlated_depth_and_time_adjustment
