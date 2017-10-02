"""
Examples of C# code, followed by its Python Equivalent

TESTED REVIT API: -

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

# Blog Post about this same topic
# http://thebar.cc/converting-revit-api-c-code-to-python/

""""
Class XYZ
revitapidocs.com/2016/fcb91231-2665-54b9-11d6-7ebcb7f235e2.htm

public XYZ(double x, double y, double z)

Usage:
>>> XYZ point = new XYZ(0, 0, 0);
"""

from Autodesk.Revit.DB import XYZ

point = XYZ(10, 10, 10)
print(point.X)
# 10

""""
CSharp Class Constructors
revitapidocs.com/2016/fcb91231-2665-54b9-11d6-7ebcb7f235e2.htm

public XYZ(double x, double y, double z)

Usage:
>>> XYZ point = new XYZ(0, 0, 0);
"""

from Autodesk.Revit.DB import XYZ

point = XYZ(10, 10, 10)
print(point.X)
# 10

""""
FilteredElementCollector Class
http://www.revitapidocs.com/2018/263cf06b-98be-6f91-c4da-fb47d01688f3.htm

public FilteredElementCollector(
    Document document
)

Usage:
>>> FilteredElementCollector collector = new FilteredElementCollector(doc);
>>> walls = collector.OfClass(Wall).ToElements()
"""
from Autodesk.Revit.DB import FilteredElementCollector, Wall

collector = FilteredElementCollector(doc)
walls = collector.ToElements()


""""
Line Intersect Method (Users Out/Ref Values)
http://www.revitapidocs.com/2018/51961478-fb36-e00b-2d1b-7db27b0a09e6.htm

public SetComparisonResult Intersect(
    Curve curve,
    out IntersectionResultArray resultArray
)

Usage:
>>> IntersectionResultArray results;
>>> SetComparisonResult result = line1.Intersect( line2, out results );
>>> if( result != SetComparisonResult.Overlap ) {
...     throw new InvalidOperationException("Input lines did not intersect." );
... };
>>> if( results == null || results.Size != 1 ) {
...    throw new InvalidOperationException("Could not extract line intersection point." );
... }
>>> IntersectionResult iResult
    = results.get_Item( 0 );

"""
import clr
from Autodesk.Revit.DB import SetComparisonResult, IntersectionResultArray
from Autodesk.Revit.Exceptions import InvalidOperationException

line1 = Line.CreateBound(XYZ(0,0,0), XYZ(10,0,0))
line2 = Line.CreateBound(XYZ(5,-5,0), XYZ(5,5,0))

results = clr.Reference[IntersectionResultArray]()
result = line1.Intersect(line2, results)

if result != SetComparisonResult.Overlap:
    print('No Intesection')

if results is None or results.Size != 1:
    raise InvalidOperationException("Could not extract line intersection point." )

intersection = results.Item[0]
xyz_point = intersection.XYZPoint
