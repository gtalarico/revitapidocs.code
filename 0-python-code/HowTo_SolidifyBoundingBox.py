"""
Solidify Selected Element BoundingBox Example
Creates a Generic Model Direct Shape

TESTED REVIT API: 2017

Author: Frederic Beaupere | github.com/hdm-dt-fb
This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""
import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import Curve, CurveLoop, DirectShape, ElementId, Line, XYZ
from Autodesk.Revit.DB import SolidOptions, GeometryCreationUtilities
from Autodesk.Revit.DB import BuiltInCategory as Bic
from System.Collections.Generic import List
from rpw import db, ui, doc, uidoc

selection = [doc.GetElement(elem_id) for elem_id in uidoc.Selection.GetElementIds()]
first_selected = selection[0]
solid_opt = SolidOptions(ElementId.InvalidElementId, ElementId.InvalidElementId)

bbox = first_selected.get_BoundingBox(None)
bottom_z_offset = 0.1
bbox.Min = XYZ(bbox.Min.X, bbox.Min.Y, bbox.Min.Z - bottom_z_offset)
b1 = XYZ(bbox.Min.X, bbox.Min.Y, bbox.Min.Z)
b2 = XYZ(bbox.Max.X, bbox.Min.Y, bbox.Min.Z)
b3 = XYZ(bbox.Max.X, bbox.Max.Y, bbox.Min.Z)
b4 = XYZ(bbox.Min.X, bbox.Max.Y, bbox.Min.Z)
bbox_height = bbox.Max.Z - bbox.Min.Z

lines = List[Curve]()
lines.Add(Line.CreateBound(b1, b2))
lines.Add(Line.CreateBound(b2, b3))
lines.Add(Line.CreateBound(b3, b4))
lines.Add(Line.CreateBound(b4, b1))
rectangle = [CurveLoop.Create(lines)]

extrusion = GeometryCreationUtilities.CreateExtrusionGeometry(List[CurveLoop](rectangle),
                                                              XYZ.BasisZ,
                                                              bbox_height,
                                                              solid_opt)

category_id = ElementId(Bic.OST_GenericModel)

with db.Transaction("solid_bbox_direct_shape") as tx:
    direct_shape = DirectShape.CreateElement(doc, category_id, "A", "B")
    direct_shape.SetShape([extrusion])
