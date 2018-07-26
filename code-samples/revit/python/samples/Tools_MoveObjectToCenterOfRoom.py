"""
Centers an object in the Room in it's in based on the center of the
Room Bounding Box.

TESTED REVIT API: 2015, 2016, 2017, 2017.1

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
from functools import wraps

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import FilteredElementCollector
from Autodesk.Revit.DB import Transaction, XYZ

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document


def get_bbox_center_pt(bbox):
    """ Returns center XYZ of BoundingBox Element"""
    avg_x = (bbox.Min.X + bbox.Max.X) / 2
    avg_y = (bbox.Min.Y + bbox.Max.Y) / 2
    return XYZ(avg_x, avg_y, 0)


def revit_transaction(transaction_name):
    """ Revit Transaction Wrapper"""
    def wrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            try:
                t = Transaction(doc, transaction_name)
                t.Start()
            except InvalidOperationException as errmsg:
                print('Transaciton Error: {}'.format(errmsg))
                return_value = f(*args, **kwargs)
            else:
                return_value = f(*args, **kwargs)
                t.Commit()
            return return_value
        return wrapped_f
    return wrap


@revit_transaction('Move Element')
def move_element(element, target_point):
    """ Move Element """
    translation = target_point - element.Location.Point
    return element.Location.Move(translation)

# Get Latest Phase
for phase in doc.Phases:
    pass # phase will be equal latest phase.
active_view = doc.ActiveView

selection = uidoc.Selection.GetElementIds()

# Moves all Objects to the center of the bounding box of the room
# Multiple objects can be selected. Not fully tested.
if selection.Count > 0:
    for element_id in selection:
        element = doc.GetElement(element_id)
        try:
            room = element.Room[phase]
        except:
            pass  # Object doest not have room. Skip.
        else:
            if room:
                room_bbox = room.get_BoundingBox(active_view)
                room_center = get_bbox_center_pt(room_bbox)
                move_element(element, target_point=room_center)
