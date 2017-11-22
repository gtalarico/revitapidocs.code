"""
Linked DWG PolyLine Redraw and Dimension Example
Redraws polylines of layer "dim_help" of selected
linked DWG and adds Dimensions to these segments

TESTED REVIT API: 2017

Author: Frederic Beaupere | github.com/hdm-dt-fb

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
clr.AddReference("RevitAPI")
from rpw import doc, uidoc
from rpw.db import Transaction
from Autodesk.Revit.DB import Line, ReferenceArray, Options
from System.Diagnostics import Stopwatch

stopwatch = Stopwatch()
stopwatch.Start()

active_view = doc.ActiveView
selection = [doc.GetElement(elem_id) for elem_id in uidoc.Selection.GetElementIds()]

geo_opt = Options()
geo_opt.ComputeReferences = True
geo_opt.IncludeNonVisibleObjects = True
geo_opt.View = active_view

dim_link = selection[0]

if not dim_link:
    print("please select a linked dwg")

else:
    geometry = dim_link.get_Geometry(geo_opt)
    with Transaction("redraw dim_help layer dwg polylines"):
        for geo_inst in geometry:
            geo_elem = geo_inst.GetInstanceGeometry()
            for polyline in geo_elem:
                layer_name = doc.GetElement(polyline.GraphicsStyleId).GraphicsStyleCategory.Name

                if layer_name == "dim_help":
                    if polyline.GetType().Name == "PolyLine":

                        begin = None
                        for pts in polyline.GetCoordinates():
                            if begin:
                                end = pts
                                line = Line.CreateBound(begin, end)
                                det_line = doc.Create.NewDetailCurve(active_view, line)
                                line_refs = ReferenceArray()
                                line_refs.Append(det_line.GeometryCurve.GetEndPointReference(0))
                                line_refs.Append(det_line.GeometryCurve.GetEndPointReference(1))
                                dim = doc.Create.NewDimension(active_view, det_line.GeometryCurve, line_refs)

                                begin = pts
                            else:
                                begin = pts

print("{} updated in: ".format(__file__))
stopwatch.Stop()
timespan = stopwatch.Elapsed
print(timespan)
