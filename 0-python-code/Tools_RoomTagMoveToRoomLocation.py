"""
ROOM TAGS MOVE TO ROOM LOCATION

TESTED REVIT API: 2016,2017,2018

Author: min.naung@https://twentytwo.space/contact | https://github.com/mgjean

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""
from Autodesk.Revit.DB import FilteredWorksetCollector, WorksetKind
from Autodesk.Revit.DB import Transaction

# document instance
doc = __revit__.ActiveUIDocument.Document

# collect room tags from active view
tags = FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(SpatialElementTag).ToElements()

trans = Transaction(doc, "Room Tags Relocation")
trans.Start()
# loop tags
for i in tags:
	# get room location 
	room_loc = i.Room.Location.Point
	# location to move (room location - current tag location)
	new_loc = room_loc - i.Location.Point
	# move to new location
	i.Location.Move(new_loc)

print "DONE!"
trans.Commit()