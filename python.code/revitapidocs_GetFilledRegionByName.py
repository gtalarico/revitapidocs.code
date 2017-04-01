from Autodesk.Revit.DB import Element, FilteredElementCollector
from Autodesk.Revit.DB import FilledRegionType, FilledRegion


def fregion_id_by_name(name=None):
    """Get Id of Filled Region Type by Name.
    Loops through all types, tries to match name.
    If name not supplied, first type is used.
    If name supplied does not match any existing types, last type is used
    """
    f_region_types = FilteredElementCollector(doc).OfClass(FilledRegionType)
    for fregion_type in f_region_types:
        fregion_name = Element.Name.GetValue(fregion_type)
        if not name or name.lower() == fregion_name.lower():
            return fregion_type.Id
    # Loops through all, not found: use last
    else:
        print('Color not specified or not found.')
        return fregion_type.Id