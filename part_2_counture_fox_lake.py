import arcpy
arcpy.env.overwriteOutput = True

try:
    # Local variables:
    inRaster = arcpy.GetParameterAsText(0)
    outContours = arcpy.GetParameterAsText(1)

    # Local variables:
    inRaster = "D:\\python_project\\ArcGIS_python\\Lesson1\\foxlake"
    outContours = "D:\\python_project\\ArcGIS_python\\Lesson1\\USA.gdb\\foxlake_output"

    # Process: Contour
    arcpy.gp.Contour_sa(inRaster, outContours, "25", "0", "1")

    # Report a success message
    arcpy.AddMessage("All done!")
except:
    # Report an error messages
    arcpy.AddError("Could not complete the buffer")

    # Report any error messages that the Buffer tool might have generated
    arcpy.AddMessage(arcpy.GetMessages())
