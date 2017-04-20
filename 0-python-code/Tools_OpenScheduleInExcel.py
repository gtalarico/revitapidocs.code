"""
Creates a temporary .txt file of a selected schedule, and open it in Excel

TESTED REVIT API: 2015, 2016, 2017, 2017.1

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

from Autodesk.Revit.DB import ViewSchedule, ViewScheduleExportOptions
from Autodesk.Revit.DB import ExportColumnHeaders, ExportTextQualifier
from Autodesk.Revit.DB import BuiltInCategory, ViewSchedule
from Autodesk.Revit.UI import TaskDialog

import os
import subprocess

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

desktop = os.path.expandvars('%temp%\\')
vseop = ViewScheduleExportOptions()

selected_ids = uidoc.Selection.GetElementIds()

if not selected_ids.Count:
    '''If nothing is selected, use Active View'''
    selected_ids=[ doc.ActiveView.Id ]

for element_id in selected_ids:
    element = doc.GetElement(element_id)
    if not isinstance(element, ViewSchedule):
        print('No schedule in Selection. Skipping...')
        continue

    filename = "".join(x for x in element.ViewName if x not in ['*']) + '.txt'
    element.Export(desktop, filename, vseop)

    print('EXPORTED: {0}\n      TO: {1}\n'.format(element.ViewName, filename))
    EXCEL = r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
    if os.path.exists(EXCEL):
        print('Excel Found. Trying to open...')
        print('Filename is: ', filename)
        try:
            full_filepath = os.path.join(desktop, filename)
            os.system('start excel \"{path}\"'.format(path=full_filepath))
        except:
            print('Sorry, something failed:')
            print('Filepath: {}'.filename)
            print('EXCEL Path: {}'.format(EXCEL))
    else:
        print('Could not find excel. EXCEL: {}'.format(EXCEL))
print('Done')
