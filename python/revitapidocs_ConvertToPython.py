""""
XYZ Class Constructor
revitapidocs.com/2016/fcb91231-2665-54b9-11d6-7ebcb7f235e2.htm

C# Constructor Documentation

public XYZ(double x, double y, double z)

Usage:
XYZ point = new XYZ(0, 0, 0);
"""

from Autodesk.Revit.DB import XYZ
point = XYZ(10, 10, 10)
#############################
>>> print(point.X)
10