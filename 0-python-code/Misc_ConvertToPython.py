"""
Example of a XYZ Constructor using Python. For more information see:
revitapidocs.com/2016/fcb91231-2665-54b9-11d6-7ebcb7f235e2.htm

TESTED REVIT API: -

Author: Gui Talarico | github.com.gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""


""""
CSharp Class Constructors

public XYZ(double x, double y, double z)

Usage:
XYZ point = new XYZ(0, 0, 0);
"""

# Python Equivalent
from Autodesk.Revit.DB import XYZ

point = XYZ(10, 10, 10)
#############################
>>> print(point.X)
# >>> 10
