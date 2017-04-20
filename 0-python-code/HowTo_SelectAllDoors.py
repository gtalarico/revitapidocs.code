"""
Selects All Door Instances that have been Mirrored.

TESTED REVIT API: 2015, 2016, 2017, 2017.1

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
clr.AddReference("System")

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB import BuiltInCategory, ElementId
from System.Collections.Generic import List

collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors)
doors = collector.WhereElementIsNotElementType().ToElements()

mir_doors = []

for door in doors:
    try:
        if door.Mirrored:
            mir_doors.append(door)
    except AttributeError:
        pass  # for Symbols that don't have Mirrored attribute.

TaskDialog.Show("Mirrored Doors", "Mirrored: {} of {} Doors".format(
                len(mir_doors), len(doors)))

selection = uidoc.Selection
collection = List[ElementId]([door.Id for door in mir_doors])
selection.SetElementIds(collection)
