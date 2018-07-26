"""
Selects unbound rooms in model

TESTED REVIT API: 2015, 2016, 2017

Author: Jared Friedman | github.com/jbf1212

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""
from Autodesk.Revit.DB import Transaction, Element
from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.UI import TaskDialog
from System.Collections.Generic import List

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

# GET ALL ROOMS IN MODEL
rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms)
ub_rooms = []

for r in rooms:
    if r.Area > 0:
        pass
    else:
        ub_rooms.append(r)

# SELECT UNBOUND ROOMS
collection = List[ElementId]([r.Id for r in ub_rooms])
selection = uidoc.Selection
selection.SetElementIds(collection)

TaskDialog.Show('Unbound Rooms', "{} unbound rooms selected". format(len(ub_rooms)))
