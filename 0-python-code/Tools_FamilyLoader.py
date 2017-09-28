"""
Family Loader

- loads familiy into project with a path and file name.
- implements IFamilyLoadOptions to silence OverwriteParamaterValue dialogue box.

Requires rpw library: github.com/gtalarico/revitpythonwrapper

Author: Grant Foster | github.com/grantdfoster
"""
import os
import clr
import Autodesk.Revit.DB
from Autodesk.Revit.DB import IFamilyLoadOptions, FamilySource, Transaction

doc = __revit__.ActiveUIDocument.Document


class FamilyLoadOptions(IFamilyLoadOptions):
    'A Class implementation for loading families'

    def OnFamilyFound(self, familyInUse, overwriteParameterValues):
        'Defines behavior when a family is found in the model.'
        overwriteParameterValues = True
        return True

    def OnSharedFamilyFound(self, sharedFamily, familyInUse, source, overwriteParameterValues):
        'Defines behavior when a shared family is found in the model.'
        source = FamilySource.Project
        # source = FamilySource.Family
        overwriteParameterValues = True
        return True


def load_family(folder_path='Insert Path Here', file_name='Insert File Name Here'):
    'Loads a family into the Revit project with path and file name.'
    family_path = os.path.join(folder_path, file_name)
    if os.path.exists(family_path) is False:
        return 'Path does not exist.'

    family_loaded = clr.Reference[Autodesk.Revit.DB.Family]()
    t = Transaction(doc)
    t.Start('Load Family')

    loaded = doc.LoadFamily(family_path, FamilyLoadOptions(), family_loaded)
    if loaded:
        family = family_loaded.Value
        symbols = []

        for family_symbol_id in family.GetFamilySymbolIds():
            family_symbol = doc.GetElement(family_symbol_id)
            symbols.append(family_symbol)

        for s in symbols:
            try:
                s.Activate()
            except:
                pass

        t.Commit()
        return symbols

    else:
        t.Commit()
        return 'Family already exists in project.'
