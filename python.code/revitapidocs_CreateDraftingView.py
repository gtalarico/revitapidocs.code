''' Creates a Drafting View'''
from Autodesk.Revit.DB import Transaction, Element
from Autodesk.Revit.DB import FilteredElementCollector

#  Drafting Views
from Autodesk.Revit.DB import ViewFamilyType, ViewDrafting, Element
from Autodesk.Revit.DB import ViewFamily

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

t = Transaction(doc, 'Create Drafting View')
t.Start()

"""Create a Drafting View"""
def get_drafting_type_id():
    """Selects First available ViewType that Matches Drafting Type."""
    viewfamily_types = FilteredElementCollector(doc).OfClass(ViewFamilyType)
    for i in viewfamily_types:
        if i.ViewFamily == ViewFamily.Drafting:
            return i.Id

drafting_type_id = get_drafting_type_id()
drafting_view = ViewDrafting.Create(doc, drafting_type_id)
# drafting_view.Name = 'New View' - Optional View Name - May fail if already exists.

t.Commit()