"""
Sets Color Mode of all Point Cloud Instances in View to Normal.

TESTED REVIT API: 2017

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit import DB

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

pts = DB.FilteredElementCollector(doc).OfClass(DB.PointCloudInstance).WhereElementIsNotElementType().ToElements()
pt_cloud_settings = DB.PointClouds.PointCloudOverrideSettings()
pt_cloud_settings.ColorMode = DB.PointCloudColorMode.Normals
for pt in pts:
    view = uidoc.ActiveView
    pt_overrides = view.GetPointCloudOverrides()
    t = DB.Transaction(doc)
    t.Start('Set Pt Cloud Color Mode')
    pt_overrides.SetPointCloudOverrideSettings(pt.Id, pt_cloud_settings)
    t.Commit()
