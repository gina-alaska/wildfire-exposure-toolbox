# -*- coding: utf-8 -*-

import arcpy
from arcpy.sa import *
import os

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [WildfireExposure]


class WildfireExposure(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Wildfire Hazard and Exposure"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        # Define the input parameters for the script tool

        hazCheck = arcpy.Parameter(
            name="hazCheck",
            displayName="Reclassify Vegetation to Hazardous Fuels",
            parameterType="Optional",
            direction="Input",
            datatype="GPBoolean")

        whichHaz = arcpy.Parameter(
            name="whicHaz",
            displayName="Select distance",
            parameterType="Optional",
            direction="Input",
            datatype="GPString")
        whichHaz.filter.type = "Value List"
        whichHaz.filter.list = ['100m', '500m', 'Both']
        whichHaz.enabled = False

        input_raster = arcpy.Parameter(
            displayName="Input raster",
            name="input_raster",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Input")
        input_raster.enabled = False
        
        remap_table100 = arcpy.Parameter(
            displayName="100m Reclassification Table",
            name="remap_table100",
            datatype="GPSARemap",
            parameterType="Optional",
            direction="Input")
        remap_table100.enabled = False

        remap_table500 = arcpy.Parameter(
            displayName="500m Reclassification Table",
            name="remap_table500",
            datatype="GPSARemap",
            parameterType="Optional",
            direction="Input")
        remap_table500.enabled = False
        
        hazOutput100 = arcpy.Parameter(
            displayName="Output 100m Hazardous Veg Raster",
            name="hazOutput100",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Output")
        hazOutput100.enabled = False
        hazOutput100.symbology = os.path.join(os.path.dirname(__file__), 'symbology', 'WIldfire_Hazardous_100_Cat_Explained.lyrx')
        
        hazOutput500 = arcpy.Parameter(
            displayName="Output 500m Hazardous Veg Raster",
            name="hazOutput500",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Output")
        hazOutput500.enabled = False
        hazOutput500.symbology = os.path.join(os.path.dirname(__file__), 'symbology', 'WIldfire_Hazardous_500_Cat_Explained.lyrx') 
        
        expCheck = arcpy.Parameter(
            name="expCheck",
            displayName="Process Exposure from Hazardous Fuels",
            parameterType="Optional",
            direction="Input",
            datatype="GPBoolean")

        whichExp = arcpy.Parameter(
            name="whichExp",
            displayName="Select distance",
            parameterType="Optional",
            direction="Input",
            datatype="GPString")
        whichExp.filter.type = "Value List"
        whichExp.filter.list = ['100m', '500m', 'Both']
        whichExp.enabled = False

        input_haz100 = arcpy.Parameter(
            displayName="Input Hazardous Fuels 100m raster",
            name="input_haz100",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Input")
        input_haz100.enabled = False
        
        input_haz500 = arcpy.Parameter(
            displayName="Input Hazardous Fuels 500m raster",
            name="input_haz500",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Input")
        input_haz500.enabled = False

        expOutput100 = arcpy.Parameter(
            displayName="Output 100m Exposure Pct Raster",
            name="expOutput100",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Output")
        expOutput100.enabled = False
        expOutput100.symbology = os.path.join(os.path.dirname(__file__), 
                                    'symbology', 'Wildfire_Exposure_Cat_Explained_v2.lyrx')

        expOutput500 = arcpy.Parameter(
            displayName="Output 500m Exposure Pct Raster",
            name="expOutput500",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Output")
        expOutput500.enabled = False
        expOutput500.symbology = os.path.join(os.path.dirname(__file__), 
                                    'symbology', 'Wildfire_Exposure_Cat_Explained_v2.lyrx')
        
        combiCheck = arcpy.Parameter(
            name="combiCheck",
            displayName="Create combined Exposure Dataset using Buildings Dataset",
            parameterType="Optional",
            direction="Input",
            datatype="GPBoolean")        

        input_exp100 = arcpy.Parameter(
            displayName="Input Exposure Pct 100m raster",
            name="input_exp100",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Input")
        input_exp100.enabled = False
        
        input_exp500 = arcpy.Parameter(
            displayName="Input Exposure Pct 500m raster",
            name="input_exp500",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Input")
        input_exp500.enabled = False

        input_buildings = arcpy.Parameter(
            displayName="Input buildings dataset (vector or raster)",
            name="input_buildings",
            datatype=["GPRasterLayer", "GPFeatureLayer"],
            parameterType="Optional",
            direction="Input")
        input_buildings.enabled = False

        bufferCheck = arcpy.Parameter(
            name="bufferCheck",
            displayName="Building dataset needs buffer (vector only)",
            parameterType="Optional",
            direction="Input",
            datatype="GPBoolean")
        bufferCheck.enabled = False

        combiOutput = arcpy.Parameter(
            displayName="Output Combined Exposure Pct Raster",
            name="expOutputCombi",
            datatype="GPRasterLayer",
            parameterType="Optional",
            direction="Output")
        combiOutput.enabled = False
        combiOutput.symbology = os.path.join(os.path.dirname(__file__), 
                                    'Wildfire_Exposure_Cat_Explained_v2.lyrx')


        clipOutputs = arcpy.Parameter(
            name="clipOutputs",
            displayName="Clip Outputs",
            parameterType="Optional",
            direction="Input",
            datatype="GPBoolean")  

        clipExtent = arcpy.Parameter(
            name="clipExtent",
            displayName="Clipping Layer",
            parameterType="Optional",
            direction="Input",
            datatype="GPFeatureLayer")  

        # Return the parameter definitions
        return [
            hazCheck,
            whichHaz,
            input_raster,
            remap_table100,
            remap_table500,
            hazOutput100,
            hazOutput500,
            expCheck,
            whichExp,
            input_haz100,
            input_haz500,
            expOutput100,
            expOutput500,
            combiCheck,
            input_exp100,
            input_exp500,
            input_buildings,
            bufferCheck,
            combiOutput,
            clipOutputs,
            clipExtent
        ]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        # Enable/disable parameters based on the value of other parameters
        parameters[1].enabled = parameters[0].value
        parameters[2].enabled = parameters[0].value
        if parameters[1].value == '100m':
            parameters[3].enabled = parameters[0].value
            parameters[4].enabled = False
            parameters[5].enabled = parameters[0].value
            parameters[6].enabled = False
        elif parameters[1].value == '500m':
            parameters[3].enabled = False
            parameters[4].enabled = parameters[0].value
            parameters[5].enabled = False
            parameters[6].enabled = parameters[0].value
        elif parameters[1].value == 'Both':
            parameters[3].enabled = parameters[0].value
            parameters[4].enabled = parameters[0].value
            parameters[5].enabled = parameters[0].value
            parameters[6].enabled = parameters[0].value
        else:
            parameters[5].enabled = False
            parameters[6].enabled = False            
        parameters[8].enabled = parameters[7].value
        if parameters[1].enabled and parameters[1].value:
            parameters[8].value = parameters[1].value
        if parameters[8].value == '100m':
            parameters[9].enabled = parameters[7].value and not parameters[0].value
            parameters[10].enabled = False
            parameters[11].enabled = parameters[7].value
            parameters[12].enabled = False
        elif parameters[8].value == '500m':
            parameters[9].enabled = False
            parameters[10].enabled = parameters[7].value and not parameters[0].value
            parameters[11].enabled = False
            parameters[12].enabled = parameters[7].value
        elif parameters[8].value == 'Both':
            parameters[9].enabled = parameters[7].value and not parameters[0].value
            parameters[10].enabled = parameters[7].value and not parameters[0].value
            parameters[11].enabled = parameters[7].value
            parameters[12].enabled = parameters[7].value
        else:
            parameters[9].enabled = False
            parameters[10].enabled = False
            parameters[11].enabled = False
            parameters[12].enabled = False
        if parameters[13].value == True:
            parameters[14].enabled = not parameters[7].value
            parameters[15].enabled = not parameters[7].value
            parameters[16].enabled = True
            parameters[17].enabled = True
            parameters[18].enabled = True
        else:
            parameters[14].enabled = False
            parameters[15].enabled = False
            parameters[16].enabled = False
            parameters[17].enabled = False
            parameters[18].enabled = False
        parameters[20].enabled = parameters[19].value

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # To allow overwriting outputs change overwriteOutput option to True.
        arcpy.env.overwriteOutput = True

        # Check out any necessary licenses.
        arcpy.CheckOutExtension("spatial")

        hazCheck = parameters[0].value
        whichHaz = parameters[1].valueAsText
        input_raster = parameters[2].valueAsText
        remap_table = {
            '100': parameters[3].valueAsText,
            '500': parameters[4].valueAsText
        }
        hazOutput = {
            '100': parameters[5].valueAsText,
            '500': parameters[6].valueAsText
        }
        expCheck = parameters[7].value
        whichExp = parameters[8].valueAsText
        input_haz = {
            '100': parameters[9].valueAsText,
            '500': parameters[10].valueAsText
        }
        expOutput = {
            '100': parameters[11].valueAsText,
            '500': parameters[12].valueAsText
        }
        combiCheck = parameters[13].value
        input_exp = {
            '100': parameters[14].valueAsText,
            '500': parameters[15].valueAsText
        }
        input_buildings = parameters[16].valueAsText
        bufferCheck = parameters[17].value
        combiOutput = parameters[18].valueAsText
        clipOutputs = parameters[19].value
        clipExtent = parameters[20].valueAsText
        if input_raster:
            arcpy.env.outputCoordinateSystem = arcpy.Describe(input_raster).spatialReference
            arcpy.env.cellSize = input_raster
            arcpy.env.snapRaster = input_raster

        # Process: Reclassify (Reclassify) (sa)
        if hazCheck:
            if whichHaz == 'Both':
                dist = ['100', '500']
            else:
                dist = [f'{whichHaz[:-1]}']
            reclassed_rasters = []
            for d in dist:
                arcpy.AddMessage(f'reclassifying with {d} meter remap')
                hazard_raster = arcpy.sa.Reclassify(input_raster, "Value", remap_table[f'{d}'], missing_values="NODATA")
                arcpy.AddMessage(arcpy.GetMessages())
                if hazOutput[f'{d}']:
                    arcpy.AddMessage(f"saving reclassed raster to {hazOutput[f'{d}']}")
                    hazard_raster.save(hazOutput[f'{d}'])
                arcpy.AddMessage("adding reclassed raster to exposure raster input")
                input_haz[f'{d}'] = hazard_raster
        if expCheck:
            if whichExp == 'Both':
                dist = ['100', '500']
            else:
                dist = [f'{whichExp[:-1]}']
            for d in dist:
                if d == '100':
                    nbhd = "Circle 3 CELL"
                    expression = "SetNull(IsNull(y), Int(x / 29))"
                elif d == '500':
                    nbhd = "Circle 16 CELL"
                    expression = "SetNull(IsNull(y), Int(x / 797))"
                arcpy.AddMessage(f'focal statistics with {d} hazardous veg, using hazOutput')
                exposure_raster_sum = arcpy.sa.FocalStatistics(in_raster = input_haz[f'{d}'], neighborhood = nbhd, statistics_type = "SUM", ignore_nodata = "DATA")
                exposure_raster = arcpy.sa.RasterCalculator([exposure_raster_sum, input_haz[f'{d}']], ['x', 'y'], expression)
                arcpy.AddMessage(arcpy.GetMessages())
                if expOutput[f'{d}']:
                    result = arcpy.management.CopyRaster(exposure_raster, expOutput[f'{d}'], '', None, "-128", "NONE", "NONE", "8_BIT_SIGNED", "NONE", "NONE", '', "NONE", "CURRENT_SLICE", "NO_TRANSPOSE")
                    exp_raster_8bit = arcpy.Raster(result.getOutput(0))
                input_exp[f'{d}'] = exp_raster_8bit
        if combiCheck:
            arcpy.env.outputCoordinateSystem = arcpy.Describe(input_exp['500']).spatialReference
            arcpy.env.cellSize = input_exp['500']
            arcpy.env.snapRaster = input_exp['500']
            arcpy.AddMessage(f"combining with {input_buildings} (datatype: {arcpy.Describe(input_buildings).dataType}), using {input_exp['100']} and {input_exp['500']}")
            if arcpy.Describe(input_buildings).dataType == "FeatureLayer" or arcpy.Describe(input_buildings).dataType == "ShapeFile":
                arcpy.AddMessage(f'Converting {input_buildings} to raster')
                if bufferCheck == True:
                    building_name, building_extension = os.path.splitext(input_buildings)
                    building_buffer = building_name + '_buffer' + building_extension
                    arcpy.AddMessage(f'buffering {input_buildings}, creating {building_buffer}')
                    arcpy.analysis.Buffer(input_buildings, building_buffer, "500 Meters")
                    arcpy.AddMessage(arcpy.GetMessages())
                    input_buildings = building_buffer
                building_name, building_extension = os.path.splitext(input_buildings)
                building_raster = os.path.basename(building_name) + '_raster'
                arcpy.conversion.PolygonToRaster(input_buildings, arcpy.Describe(input_buildings).OIDFieldName, building_raster)
                input_buildings = building_raster
                arcpy.AddMessage(f"combining with {input_buildings} (datatype: {arcpy.Describe(input_buildings).dataType}), using {input_exp['100']} and {input_exp['500']}")
            combi = Con(IsNull(input_buildings), input_exp['500'], Con(arcpy.Raster(input_exp['500']) > arcpy.Raster(input_exp['100']), input_exp['500'],
                        input_exp['100']))
            '''
            combi = Con(IsNull(input_buildings), input_exp['500'],
                        Con(input_exp['500'] > input_exp['100'], input_exp['500'],
                        input_exp['100']))
            '''
            arcpy.AddMessage(arcpy.GetMessages())

            combi.save(combiOutput)
        if clipOutputs:
            for o in [hazOutput['100'], hazOutput['500'], expOutput['100'], expOutput['500'], combiOutput]:
                if o:
                    arcpy.AddMessage(f"clipping {o} output rasters to {clipExtent}")
                    out_raster = arcpy.sa.ExtractByMask(o, clipExtent); out_raster.save(o)
                    arcpy.AddMessage(arcpy.GetMessages())
        return

