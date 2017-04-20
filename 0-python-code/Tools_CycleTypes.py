"""
Cycles through available types in family manager. Must be in Family Document

TESTED REVIT API: 2015, 2016, 2017, 2017.1

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""


from Autodesk.Revit.DB import Transaction
from Autodesk.Revit.UI import TaskDialog

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

if not doc.IsFamilyDocument:
    TaskDialog.Show('Message', 'Must be in Family Document.')

else:
    family_types = [x for x in doc.FamilyManager.Types]
    sorted_type_names = sorted([x.Name for x in family_types])
    current_type = doc.FamilyManager.CurrentType

    # Iterate through sorted list of type names, return name of next in list
    for n, type_name in enumerate(sorted_type_names):
        if type_name == current_type.Name:
            try:
                next_family_type_name = sorted_type_names[n + 1]
            except IndexError:
                # wraps list back to 0 if current is last
                next_family_type_name = sorted_type_names[0]

    for family_type in family_types:
        if family_type.Name == next_family_type_name:
            t = Transaction(doc, 'Cycle Type')
            t.Start()
            doc.FamilyManager.CurrentType = family_type
            t.Commit()
