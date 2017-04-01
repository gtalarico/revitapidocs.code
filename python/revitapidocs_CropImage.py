"""
Crop Image
Crops an Image to a Filled Region Boundary
TESTED REVIT API: 2015

Copyright (c) 2014-2016 Gui Talarico
github.com/gtalarico

This script is part of PyRevitPlus: Extensions for PyRevit
github.com/gtalarico/pyrevitplus
"""
__author__ = '@gtalarico'

import sys
import os
import logging
from functools import wraps
from collections import namedtuple
from random import randint

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import XYZ, BoundingBoxXYZ
from Autodesk.Revit.DB import ImageView, ImageType, ImageImportOptions, BoxPlacement
from Autodesk.Revit.DB import Element, ElementId, BuiltInParameter
from Autodesk.Revit.DB import Transaction, FilledRegion

import clr
from clr import StrongBox
clr.AddReference('System')
clr.AddReference('System.IO')
clr.AddReference('System.Drawing')
from System import IO
from System.Drawing.Graphics import DrawImage
from System.Drawing.Imaging import ImageFormat
from System.Drawing import (GraphicsUnit, Graphics,
                            Image, Rectangle, Bitmap,
                            Point, Size)


doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

def get_selected_elements():
    """ Returns actual Elements that are currently selected. """
    selection = uidoc.Selection
    selection_ids = selection.GetElementIds()
    selection_size = selection_ids.Count
    if not selection_ids:
        TaskDialog.Show('MakePlans', 'No Elements Selected.')
        __window__.Close()
        sys.exit(0)
    elements = []
    for element_id in selection_ids:
        elements.append(doc.GetElement(element_id))
    return elements


def get_bbox_center_pt(bbox):
    """ Returns center XYZ of BoundingBox Element"""
    avg_x = (bbox.Min.X + bbox.Max.X) / 2
    avg_y = (bbox.Min.Y + bbox.Max.Y) / 2
    return XYZ(avg_x, avg_y, 0)


def create_img_copy(img_path):
    """ Creates a Copy of an image in the same folder"""
    split_path = img_path.split('.')
    extension = split_path.pop(-1)
    full_path = ''.join(split_path) # Rejoins in case there are other dots
    seq_start = 1
    while True:
        new_img_path = '{}_cropped_{}.{}'.format(full_path, seq_start, extension)
        try:
            IO.File.Copy(img_path, new_img_path)
            return new_img_path
        except IO.IOException as errmsg:
            seq_start +=1
        except Exception as errmsg:
            print('Unknown Error: {}'.format(new_img_path))
            print(errmsg)
            raise

def crop_image(img_path, rectangle_crop):
    source_bmp = Bitmap(img_path)
    new_img_path = create_img_copy(img_path)

    # Without this, images that are not 96 dpi get cropped out of scale
    source_bmp.SetResolution(96,96)
    # An empty bitmap which will hold the cropped image
    bmp = Bitmap(rectangle_crop.Width, rectangle_crop.Height)
    graphic = Graphics.FromImage(bmp)
    # Draw the given area (rectangle_crop) of the source_bmp image at location 0,0 on the empty bitmap (bmp)
    graphic.DrawImage(source_bmp, 0, 0, rectangle_crop, GraphicsUnit.Pixel)
    cropped_img = bmp
    cropped_img.Save(new_img_path)
    return new_img_path


#__window__.Close()
img_element, fregion = None, None
elements = get_selected_elements()

for element in elements:
    if isinstance(element, FilledRegion):
        fregion = element
        fregion_bbox = fregion.get_BoundingBox(doc.ActiveView)
        continue

    for valid_type_id in element.GetValidTypes():
        valid_type = doc.GetElement(valid_type_id)

        if isinstance(valid_type, ImageType):
            img_element = element
            img_type = valid_type

            # Type BIP Definitions
            bip_filename = BuiltInParameter.RASTER_SYMBOL_FILENAME
            bip_height_px = BuiltInParameter.RASTER_SYMBOL_PIXELHEIGHT
            bip_width_px = BuiltInParameter.RASTER_SYMBOL_PIXELWIDTH
            bip_resolution = BuiltInParameter.RASTER_SYMBOL_RESOLUTION

            # Type Parameters
            img_path = img_type.get_Parameter(bip_filename).AsString()
            img_width_px = img_type.get_Parameter(bip_width_px).AsInteger()
            img_height_px = img_type.get_Parameter(bip_height_px).AsInteger()
            img_resolution = img_type.get_Parameter(bip_resolution).AsInteger()

            # Instance BIP Definitions
            bip_scale = BuiltInParameter.RASTER_VERTICAL_SCALE
            bip_width_ft = BuiltInParameter.RASTER_SHEETWIDTH # Width
            bip_height_ft = BuiltInParameter.RASTER_SHEETHEIGHT # Height

            # Instance Parameters
            img_scale = img_element.get_Parameter(bip_scale).AsDouble()
            img_width = img_element.get_Parameter(bip_width_ft).AsDouble()
            img_height = img_element.get_Parameter(bip_height_ft).AsDouble()
            img_bbox = img_element.get_BoundingBox(doc.ActiveView)
            # img_bbox = BoundingBoxElement(img_element)

            break

if not img_element or not fregion:
    print('Need a filled region and image selected.')
else:
    __window__.Close()

    # Absolute Height/Width of Crop Box
    cropbox_height_ft = fregion_bbox.Max.Y - fregion_bbox.Min.Y
    cropbox_width_ft = fregion_bbox.Max.X - fregion_bbox.Min.X

    # Relative Coordinate of Crop Box to Corner of Image
    lw_left_crop_pt = fregion_bbox.Min - img_bbox.Min
    up_left_crop_pt = lw_left_crop_pt + XYZ(0, cropbox_height_ft, 0)

    # Relative Origin for Cropping
    crop_pt_x_ft = up_left_crop_pt.X
    crop_pt_y_ft = img_height - up_left_crop_pt.Y

    # Multiplier to convert from Ft Coordinate to Pixel
    x_ft_to_px_scale = img_width_px / img_width
    y_ft_to_px_scale = img_height_px / img_height

    # Convert ft space to pixel space
    crop_pt_x_px = crop_pt_x_ft * x_ft_to_px_scale
    crop_pt_y_px = crop_pt_y_ft * y_ft_to_px_scale
    cropbox_width_px = cropbox_width_ft * x_ft_to_px_scale
    cropbox_height_px = cropbox_height_ft * y_ft_to_px_scale

    rectangle_crop = Rectangle(crop_pt_x_px, crop_pt_y_px,
                               cropbox_width_px, cropbox_height_px)
    new_img_path = crop_image(img_path, rectangle_crop)

    # New Image Options
    import_options = ImageImportOptions()
    import_options.Placement = BoxPlacement.Center
    import_options.RefPoint = get_bbox_center_pt(fregion_bbox)
    import_options.Resolution = img_resolution

    # Create New Image in Revit
    t = Transaction(doc, 'Crop Image')
    t.Start()
    new_img_element = StrongBox[Element]()
    doc.Import(new_img_path, import_options , doc.ActiveView, new_img_element)
    new_img_width = new_img_element.get_Parameter(bip_width_ft)
    new_img_width.Set(cropbox_width_ft)
    doc.Delete(img_element.Id)
    doc.Delete(fregion.Id)
    t.Commit()

    # DEBUG
    # if True:
    if True:
        __window__.Close()
    else:
        print('Img Width: {} ft'.format(img_width))
        print('Img Height: {} ft'.format(img_height))
        print('Img Pxl Width: {} px'.format(img_width_px))
        print('Img Pxl Height: {} px'.format(img_height_px))
        print('Img Resolution: {} DPI'.format(img_resolution))
        print('='*50)
        print('Crop Width FT: {} ft'.format(cropbox_width_ft))
        print('Crop Height FT: {} ft'.format(cropbox_height_ft))
        print('Crop Width PIXEL: {} px'.format(cropbox_width_px))
        print('Crop Height PIXEL: {} px'.format(cropbox_height_px))
        print('Upper_left Crop Pt: XYZ [{},{}]'.format(up_left_crop_pt.X, up_left_crop_pt.Y))
        print('Lower Left Crop Pt: XYZ [{},{}]'.format(lw_left_crop_pt.X, lw_left_crop_pt.Y))
        print('='*50)
        print('SCALE FT-PX X: {}'.format(x_ft_to_px_scale))
        print('SCALE FT-PX Y: {}'.format(y_ft_to_px_scale))
        print('IMG SCALE: {}'.format(img_scale))
        # DEFAULT IMG_SCALE IS 96
        print('='*50)
        print('SCALED: Crop Width: {}'.format(cropbox_width_ft * x_ft_to_px_scale))
        print('SCALED: Crop Height: {}'.format(cropbox_height_ft * y_ft_to_px_scale))
        print('SCALED: Upper_left Crop Pt: [{},{}]'.format((up_left_crop_pt * x_ft_to_px_scale).X, (up_left_crop_pt * x_ft_to_px_scale).Y))
        print('SCALED: Lower Crop Pt: [{},{}]'.format((lw_left_crop_pt * x_ft_to_px_scale).X, (lw_left_crop_pt * x_ft_to_px_scale).Y))