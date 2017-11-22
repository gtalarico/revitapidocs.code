"""
Linked DWG PolyLine Redraw and Dimension Example

Redraws polylines in a given layer (LAYER_NAME) in a linked DWG instance
and adds Dimensions to these segments

TESTED REVIT API: 2017

Author: Frederic Beaupere | github.com/hdm-dt-fb

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

from rpw import revit, db, ui, DB

LAYER_NAME = 'A-FLOR-OTLN'  # "ENTER_DWG_LAYER_NAME_HERE"

selection = ui.Selection().get_elements(wrapped=False)
dwg_link_instances = [l for l in selection if isinstance(l, DB.ImportInstance)]

if not dwg_link_instances:
    ui.forms.Alert("please select a linked dwg", exit=True)

active_view = revit.doc.ActiveView
geo_opt = DB.Options()
geo_opt.ComputeReferences = True
geo_opt.IncludeNonVisibleObjects = True
geo_opt.View = active_view

geometry = dwg_link_instances[0].get_Geometry(geo_opt)

with db.Transaction("redraw dim_help layer dwg polylines"):
    for geo_inst in geometry:
        geo_elem = geo_inst.GetInstanceGeometry()
        for polyline in geo_elem:
            element = revit.doc.GetElement(polyline.GraphicsStyleId)
            if not element:
                continue

            is_target_layer = element.GraphicsStyleCategory.Name == LAYER_NAME
            is_polyline = polyline.GetType().Name == "PolyLine"
            if is_polyline and is_target_layer:

                begin = None
                for pts in polyline.GetCoordinates():
                    if not begin:
                        begin = pts
                        continue
                    end = pts
                    line = DB.Line.CreateBound(begin, end)
                    det_line = doc.Create.NewDetailCurve(active_view, line)
                    line_refs = DB.ReferenceArray()
                    geo_curve = det_line.GeometryCurve
                    line_refs.Append(geo_curve.GetEndPointReference(0))
                    line_refs.Append(geo_curve.GetEndPointReference(1))
                    dim = doc.Create.NewDimension(active_view,
                                                  det_line.GeometryCurve,
                                                  line_refs)
                    begin = pts
