"""
Moves all selected tags to the center of their corresponding rooms

TESTED REVIT API: 2015, 2016, 2017, 2017.1

Author: Gui Talarico | github.com.gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

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
