## Overview

This ArcGIS Python Toolbox, developed in collaboration with Dr. Jennifer Schmidt, Institute for Social and Economic Research (ISER) at the University of Alaska Anchorage, is designed to allow users to calculate wildfire hazard fuels and exposure values from gridded vegetation data, as described in:

Schmidt, J.I., Ziel, R.H., Calef, M.P. et al. Spatial distribution of wildfire threat in the far north: exposure assessment in boreal communities. Nat Hazards 120, 4901–4924 (2024). https://doi.org/10.1007/s11069-023-06365-4

Ziel R., Schmidt J.I., Calef M.P., and Varvek A. 2024. Mapping the Wildfire Threat for Boreal Communities. University of Alaska Anchorage and Fairbanks. https://www.frames.gov/sites/default/files/AFSC/presentations/WildfireExposureTechnicalReport.pdf 

The toolbox was designed for replicating the described exposure assessment, and expanding to additional areas, in a user-friendly and repeatable way. Processing methods include the calculation of hazard fuels layers at 100 and 500 meter distances, exposure layers at 100 and 500 meter distances, and a combined exposure layer that assigns the values from the 100 meter exposure within a 500m buffer distance of a buildings layer, and the 500 meter exposure values outside those areas. Intermediate products are also created and saved, and the tool can use previously generated intermediate products as inputs to limit processing time.

Toolbox development and publication by the Geographic Information Network of Alaska (GINA) at the University of Alaska Fairbanks.

## Accessing Toolbox

Zipped directories of the toolbox and ancillary files can be downloaded from the [Releases section](https://github.com/gina-alaska/wildfire-exposure-toolbox/releases/latest).

## Installing Toolbox

To use the toolbox, unzip the toolbox into a location on your ArcGIS Pro machine. In ArcGIS Pro:

1. Navigate to the Catalog pane -> Project tab
2. Right click Toolboxes. Select 'Add Toolbox', navigate to and select the WildfireExposure.pyt file. The Toolbox should now be added to your ArcGIS Pro project.
3. Run the toolbox from the Catalog pane by clicking the dropdown next to 'WildfireExposure.pyt' and double clicking the 'Wildfire Hazard and Exposure' script tool that appears.

## Changelog

- 10/21/24 - v1.0.2 published, GitHub repository made public

- 10/17/24 - Toolbox and Readme modifications for user clarity, fixed default naming bug, added FNSB building shapefile to sample-data

- 10/15/24 - Readme modifications

- 10/14/24 - v1.0.1 published

## Known Issues

If issues are found, please let the developers know by creating a [GitHub Issue](https://github.com/gina-alaska/wildfire-exposure-toolbox/issues). If possible, copying the toolbox output and error message will help developers replicate issues.

### Current Issues

- [#6: 9/18/24](https://github.com/gina-alaska/wildfire-exposure-toolbox/issues/6) - When saving the Hazard fuels datasets in a geodatabase, they are added to ArcPro with an incorrect, default name. The files are named correctly in the geodatabase. Saving them as a GeoTIFF file seems to avoid this, as well as running the full tool and clipping outputs. This appears to be due to a bug in the arcpy Reclassify tool.

## Toolbox inputs

- **Vegetation Layer**

Gridded vegetation data that will be processed. Toolbox designed using Arctic Boreal Vulnerability Experiment (ABoVE) Landsat-derived Annual Dominant Land Cover Across ABoVE Core Domain, 1984-2014 (Hereafter refered to as ABoVE Landcover), a 30m x 30m categorical landcover classification (Wang et al., 2019). Other categorical vegetation datasets can be used, provided the user customizes the reclassification table to match the dataset.

The tool is built to handle different pixel sizes - however, since the tool generates datasets at 100m and 500m distances, a pixel size smaller than 100 meters would be best for data validity.

- **Reclassification Table**

Can be entered manually in tool, or loaded from a table file. This table is used to reclassify categorical vegetation data into hazard fuels data. We developed reclassification tables for 100 meter and 500 meter distances for the ABoVE Landcover data; these are included in the zipped toolbox and can be used as a template for other landcover datasets.

- **Building Footprint Layer**

Building footprints can be input as a vector or raster. If the building footprints are a vector, the tool can buffer these by 500 meters by user choice. This vector data will be rasterized matching the vegetation layer gridded file - a previously created rasterized building footprint dataset can also be used.

- **Clipping Layer**

The outputs can be clipped to match a polygon dataset, such as the outline of a state. All outputs will be clipped to the shape of the polygon clipping layer.

- **Outputs**

Raster datasets will be created, with the user able to output paths and formats. We recommend saving all raster output as GeoTIFF (.tif) in the dropdown menus in the toolbox for best performance. 

### Sample Data

For testing the toolbox, a set of sample data has been included in [sample-data](sample-data/). The following data has been included:

- **ABoVE_2014_AK_Albers_FNSB.tif**

A subset of the ABoVE Landcover data, clipped to the Fairbanks North Star Borough region

- **ABoVE_remap_100m_Veg_Types.csv** and **ABoVE_remap_500m_Veg_Types.csv**

Reclassification tables for ABoVE Landcover data, based on Beverly et al., 2021 and Schmidt et al., 2024. The format of these tables can be adapted for additional datasets with different hazard fuels classifications.

- **Building_Outlines_2023_Pictography_FNSB.shp**

FNSB building footprint GIS polygon data, accessed from: https://fnsb.gov/1108/FNSB-GIS-Layer-REST-Services

- **Building_Outlines_FNSB_500mBuffer_Raster.tif**

FNSB building footprints, buffered to a 500 meter distance and converted to a GeoTIFF raster dataset.

- **FNSB_Borough.shp**

The boundary of the FNSB Borough as a polygon shapefile. This can be used as the 'Clipping Layer'.


- **Vegetation_ABoVEOnly.lyrx**

An ArcGIS Pro .lyrx file that contains symbology for the ABoVE Landcover.

## Methodology

The following image illustrates the processing methods.


![image](docs/flowdiag.png)
Figure: Exposure assessment method process flowchart adapted from Beverly et al. (2010, 2021).
 


## Citations

Beverly JL, Bothwell P, Conner JCR, Herd EPK (2010) Assessing the exposure of the built environment to potential ignition sources generated from vegetative fuel. Int J Wildland Fire 19(3):299–313. https://doi.org/10.1071/WF09071

Beverly JL, McLoughlin N, Chapman E (2021) A simple metric of landscape fire exposure. Landsc Ecol. https://doi.org/10.1007/s10980-020-01173-8

Schmidt, J.I., Ziel, R.H., Calef, M.P. et al. Spatial distribution of wildfire threat in the far north: exposure assessment in boreal communities. Nat Hazards 120, 4901–4924 (2024). https://doi.org/10.1007/s11069-023-06365-4

Wang, J.A., D. Sulla-Menashe, C.E. Woodcock, O. Sonnentag, R.F. Keeling, and M.A. Friedl. 2019. ABoVE: Landsat-derived Annual Dominant Land Cover Across ABoVE Core Domain, 1984-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1691

Ziel R., Schmidt J.I., Calef M.P., and Varvek A. 2024. Mapping the Wildfire Threat for Boreal Communities. University of Alaska Anchorage and Fairbanks. https://www.frames.gov/sites/default/files/AFSC/presentations/WildfireExposureTechnicalReport.pdf 
