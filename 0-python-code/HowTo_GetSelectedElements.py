"""
Get's selected elements

TESTED REVIT API: -

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

uidoc = __revit__.ActiveUIDocument

def get_selected_elements():
    """Return Selected Elements as a list[]. Returns empty list if no elements are selected.
    Usage:
    - Select 1 or more elements
    > selected_elements = get_selected_elements()
    > [<Autodesk.Revit.DB.FamilyInstance object at 0x0000000000000034 [Autodesk.Revit.DB.FamilyInstance]>]
    """
    selection = uidoc.Selection
    selection_ids = selection.GetElementIds()
    elements = []
    for element_id in selection_ids:
        elements.append(doc.GetElement(element_id))
    return elements
