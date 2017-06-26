"""
Function for rotating an element based on rotation of another element.

TESTED REVIT API: 2016, 2017

Author: Jared Friedman | github.com/jbf1212

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

# Works for point-based elements
# Assumes rotations in XY plane
# Function should be called within a Transaction

def rotate_to_ref(ref_element, transform_element):
    """Match rotation between a reference element and an element to rotate"""
    try:
        o_angle = ref_element.Location.Rotation
        l_loc = ref_element.Location.Point
    except Exception as errmsg:
        logger.debug('Could not get element Rotation or Point')
        logger.debug('Error: {}'.format(errmsg))

    rot_ang = o_angle - transform_element.Location.Rotation
    rot_axis = DB.Line.CreateBound(l_loc, DB.XYZ(l_loc.X, l_loc.Y, l_loc.Z+1.0))
    transform_element.Location.Rotate(rot_axis, rot_ang)
