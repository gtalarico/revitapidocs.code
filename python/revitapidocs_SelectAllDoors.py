"""
SelectDoors
Selects All Door Instances 
TESTED REVIT API: 2015 | 2016
Gui Talarico
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

