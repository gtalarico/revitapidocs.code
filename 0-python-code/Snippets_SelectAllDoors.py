"""
Select all instances of the the door Category, types included.

TESTED REVIT API: 2015, 2016, 2017, 2017.1

Author: Gui Talarico | github.com.gtalarico

This file is part of www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/master/
"""

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB import BuiltInCategory, ElementId
from System.Collections.Generic import List
# Required for collection

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors)
doors = collector.ToElements()

# SELECT MIRRORED DOORS                 | 2015 + 2016 API
selection = uidoc.Selection
collection = List[ElementId]([door.Id for door in doors])
selection.SetElementIds(collection)
