"""
Removes Underlay From Selected Views.

TESTED REVIT API: 2015, 2016

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

# Parts of this script were taken from:
# http://dp-stuff.org/revit-view-underlay-property-python-problem/

__doc__ = 'Removes Underlay parameter from selected views.'
__author__ = 'gtalarico'
__version__ = '0.2.0'

import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.DB import ElementId
from Autodesk.Revit.DB import BuiltInParameter, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

selection = uidoc.Selection
selection_ids = selection.GetElementIds()

if selection_ids.Count > 0:
    t = Transaction(doc, 'Batch Set Underlay to None')
    t.Start()

    for element_id in selection_ids:
        element = doc.GetElement(element_id)
        if element.Category.Id.IntegerValue == int(BuiltInCategory.OST_Views) \
                and (element.CanBePrinted):
            p = element.get_Parameter(BuiltInParameter.VIEW_UNDERLAY_ID)
            if p is not None:
                p.Set(ElementId.InvalidElementId)

    t.Commit()
else:
    TaskDialog.Show('Remove Underlay', 'Select Views to Remove Underlay')


__window__.Close()
