# wildfire-exposure-toolbox
Repository for GINA ArcGIS Wildfire Exposure Python Toolbox.

## Accessing the Toolbox

Zipped directories of the toolbox and ancillary files can be downloaded from the [Releases section](https://github.com/gina-alaska/wildfire-exposure-toolbox/tags). To use the toolbox, unzip the toolbox into a location on your ArcPro machine. In ArcPro, naviagate to the Catalog pane and right click Toolboxes. Select 'Add New Toolbox', navigate to and select the WildfireExposure.pyt file. THe Toolbox should now be added to your ArcPro project and can be run from the Catalog pane by clicking the dropdown next to 'WildfireExposure.pyt' and double clicking the 'Wildfire Hazard and Exposure' script tool that appears.

## Overview

This ArcGIS Python Toolbox, developed in collaboration with Dr. Jennifer Schmidt, Institute for Social and Economic Research (ISER) at the University of Alaska Anchorage, is designed to allow users to calculate wildfire hazard fuels and exposure values from gridded vegetation data, as described in:

Schmidt, J.I., Ziel, R.H., Calef, M.P. et al. Spatial distribution of wildfire threat in the far north: exposure assessment in boreal communities. Nat Hazards 120, 4901–4924 (2024). https://doi.org/10.1007/s11069-023-06365-4

Intitial usage of the toolbox has been internal for replicating the exposure assessment, and expanding to additional areas, in a user-friedly and repeatable way. Processing methods include the calculation of hazard fuels layers at 100 and 500 meter distances, exposure layers at 100 and 500 meter distances, and a combined exposure layer that assigns the values from the 100 meter exposure within a 500m buffer distance of a buildings layer, and the 500 meter exposure values outside those areas. Intermediate products are also created and saved, and the tool can use previously generated intermediate products as inputs to limit processing time.

## Toolbox inputs

- **Vegetation Layer**

Gridded vegetation data that will be processed. Toolbox designed using Arctic Boreal Vulnerability Experiment (ABoVE) Landsat-derived Annual Dominant Land Cover Across ABoVE Core Domain, 1984-2014 (Hereafter refered to as ABoVE Landcover), a 30m x 30m categorical landcover classification (Wang et al., 2019). Other categorical vegetation datasets can be used, provided the user customizes the reclassification table to match the dataset.

- **Reclassification Table**

Can be entered manually in tool, or loaded from a table file. This table is used to reclassify categorical vegetation data into hazard fuels data. We developed reclassification tables for 100 meter and 500 meter distances for the ABoVE Landcover data; these are included in the zipped toolbox and can be used as a template for other landcover datasets.

- **Building Footprint Layer**

Building footprints can be input as a vector or raster. If the building footprints are a vector, the tool can buffer these by 500 meters by user choice. This vector data will be rasterized matching the vegetation layer gridded file - a previously created rasterized building footprint dataset can also be used.

- **Clipping Layer**

The outputs can be clipped to match a polygon dataset, such as the outline of a state. All outputs will be clipped to the shape of the polygon clipping layer.

## Methodology

The following image illustrates the processing methods.


![image](https://github.com/user-attachments/assets/35f87d21-13d2-40db-825f-fa5af7b4cf0c)
Figure: Exposure assessment method process fowchart adapted from Beverly et al. (2010, 2021).
 


## Citations

Beverly JL, Bothwell P, Conner JCR, Herd EPK (2010) Assessing the exposure of the built environment to potential ignition sources generated from vegetative fuel. Int J Wildland Fire 19(3):299–313. https://doi.org/10.1071/WF09071

Beverly JL, McLoughlin N, Chapman E (2021) A simple metric of landscape fire exposure. Landsc Ecol. https://doi.org/10.1007/s10980-020-01173-8

Schmidt, J.I., Ziel, R.H., Calef, M.P. et al. Spatial distribution of wildfire threat in the far north: exposure assessment in boreal communities. Nat Hazards 120, 4901–4924 (2024). https://doi.org/10.1007/s11069-023-06365-4

Wang, J.A., D. Sulla-Menashe, C.E. Woodcock, O. Sonnentag, R.F. Keeling, and M.A. Friedl. 2019. ABoVE: Landsat-derived Annual Dominant Land Cover Across ABoVE Core Domain, 1984-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1691
