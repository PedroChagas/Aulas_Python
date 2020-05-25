from arcpy import *
from arcpy.sa import *

x = arcpy.GetParameterAsText(0)
y = arcpy.GetParameterAsText(1)

diretorio = 'C:\\Python27\\Ferramenta_personalizada\\'

gp.ExtractByMask(x, y, diretorio + "MDE_recortado.tif")
gp.FlowDirection(diretorio + "MDE_recortado.tif", diretorio + "fdr.tif")
gp.FlowAccumulation(diretorio + "fdr.tif", diretorio + "fcc.tif")
