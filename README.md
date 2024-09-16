# wildfire-exposure-toolbox
Repository for GINA ArcGIS Wildfire Exposure Python Toolbox.

## Releases

Zipped directories of the toolbox and ancillary files can be downloaded from the [Releases section](https://github.com/gina-alaska/wildfire-exposure-toolbox/tags).

## Overview

This ArcGIS Python Toolbox, developed in collaboration with Dr. Jennifer Schmidt, Institute for Social and Economic Research (ISER) at the University of Alaska Anchorage, is designed to allow users to calculate wildfire hazard fuels and exposure values from gridded vegetation data, as described in:

Schmidt, J.I., Ziel, R.H., Calef, M.P. et al. Spatial distribution of wildfire threat in the far north: exposure assessment in boreal communities. Nat Hazards 120, 4901–4924 (2024). https://doi.org/10.1007/s11069-023-06365-4

Intitial usage of the toolbox has been internal for replicating the exposure assessment, and expanding to additional areas, in a user-friedly and repeatable way. Processing methods include the calculation of hazard fuels layers at 100 and 500 meter distances, exposure layers at 100 and 500 meter distances, and a combined exposure layer that assigns the values from the 100 meter exposure within a 500m buffer distance of a buildings layer, and the 500 meter exposure values outside those areas. Intermediate products are also created and saved, and the tool can use previously generated intermediate products as inputs to limit processing time.

## Toolbox inputs



The following image illustrates the processing methods.


![image](https://github.com/user-attachments/assets/35f87d21-13d2-40db-825f-fa5af7b4cf0c)
Figure: Exposure assessment method process fowchart adapted from Beverly et al. (2010, 2021).
 


## Citations

Beverly JL, Bothwell P, Conner JCR, Herd EPK (2010) Assessing the exposure of the built environment to potential ignition sources generated from vegetative fuel. Int J Wildland Fire 19(3):299–313. https://doi.org/10.1071/WF09071

Beverly JL, McLoughlin N, Chapman E (2021) A simple metric of landscape fire exposure. Landsc Ecol. https://doi.org/10.1007/s10980-020-01173-8
