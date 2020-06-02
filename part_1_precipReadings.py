import arcpy
arcpy.env.overwriteOutput = True

InputPoints = arcpy.GetParameterAsText(0)

Power = arcpy.GetParameterAsText(1)
if not Power:
    Power = "2"

Reclassification = arcpy.GetParameterAsText(2)
Reclassification = "0 30000 1;30000 60000 2;60000 90000 3;90000 120000 4" # provide a default value if unspecified

Clip_Features = arcpy.GetParameterAsText(3)

Output_Feature_Class = arcpy.GetParameterAsText(4)


# Process: IDW
arcpy.gp.Idw_sa(InputPoints, "RASTERVALU", "Idw_shp2", "", Power, "VARIABLE 12", "")

# Process: Reclassify
arcpy.gp.Reclassify_sa("Idw_shp2", "VALUE", Reclassification, "Output_raster_", "DATA")

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion("Output_raster_", "PolygonRe", "SIMPLIFY", "VALUE")

# Process: Clip
arcpy.Clip_analysis("PolygonRe", Clip_Features, Output_Feature_Class, "")