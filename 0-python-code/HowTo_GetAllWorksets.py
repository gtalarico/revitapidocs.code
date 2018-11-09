"""
GET ALL WORKSETS FROM THE CURRENT DOCUMENT

TESTED REVIT API: 2016,2017,2018

Author: min.naung@https://twentytwo.space/contact | https://github.com/mgjean

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""
from Autodesk.Revit.DB import FilteredWorksetCollector, WorksetKind

# document instance
doc = __revit__.ActiveUIDocument.Document

# collect user created worksets
worksets = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset).ToWorksets()

# loop worksets
for workset in worksets:
	# print name, workset
	print workset.Name,workset
