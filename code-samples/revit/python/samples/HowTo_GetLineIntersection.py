"""
Get Line Intersection
Get's intersection of 2 lines

TESTED REVIT API: 2017

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
from Autodesk.Revit.DB import Line, XYZ
from Autodesk.Revit.DB import SetComparisonResult, IntersectionResultArray

def get_intersection(line1, line2):
	results = clr.Reference[IntersectionResultArray]()
    # See ironpython.net/documentation/dotnet for clr.Reference

	result = line1.Intersect(line2, results)
    # http://www.revitapidocs.com/2018/51961478-fb36-e00b-2d1b-7db27b0a09e6.htm

	if result != SetComparisonResult.Overlap:
		print('No Intesection')

	intersection = results.Item[0]
	return intersection.XYZPoint


line1 = Line.CreateBound(XYZ(0,0,0), XYZ(10,0,0))
line2 = Line.CreateBound(XYZ(5,-5,0), XYZ(5,5,0))
point = get_intersection(line1, line2)
print(point)
# <Autodesk.Revit.DB.XYZ object at 0x00000000000001BA [(5.000000000, 0.000000000, 0.000000000)]>

"""
From this discussion:
https://forum.dynamobim.com/t/translating-to-python/13481

C# Equivalent

private XYZ GetIntersection(
  Line line1,
  Line line2 )
{
  IntersectionResultArray results;

  SetComparisonResult result
    = line1.Intersect( line2, out results );

  if( result != SetComparisonResult.Overlap )
    throw new InvalidOperationException(
      "Input lines did not intersect." );

  if( results == null || results.Size != 1 )
    throw new InvalidOperationException(
      "Could not extract line intersection point." );

  IntersectionResult iResult
    = results.get_Item( 0 );

  return iResult.XYZPoint;
}
"""
