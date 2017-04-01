"""
Auto Move Tag to Center of Room

TESTED REVIT API:
2015 | 2016

This was written to be used with PyRevit, but can easilly be used as
a standalone script using the IronPythonShell, or
a Dynamo Python component.
"""

__doc__ = "Move Room Tag to the Center of it's corresponding Room"
__author__ = '@gtalarico'
__version__ = '0.0.1'

import clr

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
from Autodesk.Revit.DB.Architecture import Room

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

###########################################################################
# TAG COLLECTOR [IN VIEW BY: doc.ActiveView.Id]
room_tags = FilteredElementCollector(doc, doc.ActiveView.Id).OfCategory(
            BuiltInCategory.OST_RoomTags).WhereElementIsNotElementType().\
            ToElements()
###########################################################################

transaction = Transaction(doc, 'Move Room Tags on Room Points')
transaction.Start()
for room_tag in room_tags:
    room_tag_pt = room_tag.Location.Point
    room = room_tag.Room
    room_pt = room.Location.Point

    translation = room_pt - room_tag_pt
    room_tag.Location.Move(translation)

transaction.Commit()
