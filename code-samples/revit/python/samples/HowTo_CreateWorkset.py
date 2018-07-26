"""
Create a Workset
Creates a Workset - Revit 2017+

TESTED REVIT API: 2017

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import Workset, Transaction
doc = __revit__.ActiveUIDocument.Document

workset_name = 'Point Clouds'
t = Transaction(doc)
t.Start('Create Workset')
Workset.Create(doc, workset_name)
t.Commit()
