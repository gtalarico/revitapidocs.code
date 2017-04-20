"""
Inserts a DWG Link into the Active View.
The same code can be used for other link types

TESTED REVIT API: 2017

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

# See: http://www.revitapidocs.com/2017/f3112a35-91c2-7783-f346-8f21d7cb99b5.htm

import clr
from Autodesk.Revit.DB import DWGImportOptions, ImportPlacement, ElementId, Transaction

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

options = DWGImportOptions()
options.Placement = ImportPlacement.Origin # Insert Options
link = clr.Reference[ElementId]()
t = Transaction(doc)
t.Start('Load Link')
doc.Link(r"C:\Some\Path\YourDrawing.dwg", options, uidoc.ActiveView, link)
t.Commit()
# link is not <Autodesk.Revit.DB.ImportInstance>
