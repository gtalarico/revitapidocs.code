"""
Change Workset Settings
Set workset to be hidden by default in all views

TESTED REVIT API: 2017

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
clr.AddReference("RevitAPI")

from Autodesk.Revit.DB import Transaction, WorksetKind, FilteredWorksetCollector
from Autodesk.Revit.DB import WorksetDefaultVisibilitySettings

doc = __revit__.ActiveUIDocument.Document

# collect all worksets
worksets = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset)

# iterate over  worksets
for workset in worksets:
    # Find workset you want to target by name
    if workset.Name == 'Replace this with Name of Workset to Target':
        t = Transaction(doc)
        t.Start('Hide Workset in all Views')

        defaultVisibility = WorksetDefaultVisibilitySettings.GetWorksetDefaultVisibilitySettings(doc)
        defaultVisibility.SetWorksetVisibility(workset.Id, False)

        t.Commit()
