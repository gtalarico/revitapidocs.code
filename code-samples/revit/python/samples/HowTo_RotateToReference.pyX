#TODO: Needs usage example including creation of `transform_element`

"""
Function for rotating an element based on rotation of another element.

TESTED REVIT API: 2016, 2017

Author: Jared Friedman | github.com/jbf1212

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""
from Autodesk.Revit.DB import Line, XYZ

# Works for point-based elements
# Assumes rotations in XY plane
# Function should be called within a Transaction

def rotate_to_ref(ref_element, transform_element):
    """Match rotation between a reference element and an element to rotate"""
    try:
        orientation_angle = ref_element.Location.Rotation
        ref_location = ref_element.Location.Point
    except Exception as errmsg:
        print('Could not get element Rotation or Point')
        print('Error: {}'.format(errmsg))

    rot_ang = orientation_angle - transform_element.Location.Rotation
    rot_axis = Line.CreateBound(ref_location, XYZ(ref_location.X, ref_location.Y, ref_location.Z+1.0))
    transform_element.Location.Rotate(rot_axis, rot_ang)
