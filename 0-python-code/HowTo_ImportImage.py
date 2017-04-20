"""
Imports an Image

TESTED REVIT API: -

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

# See: http://www.revitapidocs.com/2015/05c3dbe2-fe7e-c293-761d-b11f356a011b.htm

from clr import StrongBox
from Autodesk.Revit.DB import XYZ, ImageImportOptions, BoxPlacement, BuiltInParameter

# Import Options
import_options = ImageImportOptions()
import_options.Placement = BoxPlacement.Center
import_options.RefPoint = XYZ(0,0,0)
import_options.Resolution = 72

# Create New Image in Revit
t = Transaction(doc, 'Crop Image')
t.Start()
new_img_element = StrongBox[Element]()
new_img_path = 'C:\\path\\to\\image.jpg' # Remember to escape backslashes or use raw string
width_in_ft = 2
doc.Import(new_img_path, import_options , doc.ActiveView, new_img_element)
new_img_width = new_img_element.get_Parameter(BuiltInParameter.RASTER_SHEETWIDTH)
new_img_width.Set(width_in_ft)
t.Commit()
