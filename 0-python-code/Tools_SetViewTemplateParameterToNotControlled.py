"""
Set view template parameter to not controlled by view template 

Sets a single view template parameter 'keep_non_sheet_view'
to be not controlled by view template, keeping other view
template parameters settings.

TESTED REVIT API: 2017

Author: Frederic Beaupere | github.com/hdm-dt-fb

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import FilteredElementCollector as Fec
from Autodesk.Revit.DB import Transaction
from System.Collections.Generic import List


doc = __revit__.ActiveUIDocument.Document
all_views = Fec(doc).OfClass(View).ToElements()
view_templates = [view for view in all_views if view.IsTemplate]
first_view_template = view_templates[0]
view_template_params = first_view_template.GetTemplateParameterIds()
switch_off_param_name = "keep_non_sheet_view"

# get the id of the parameter we want to switch off
for param_id in view_template_params:
    param = doc.GetElement(param_id)
    if "Name" in dir(param):
        print(param.Name)
        if param.Name == switch_off_param_name:
            switch_off_param_id = param_id
            break

# set the switch off parameter to be non controlled
# while keeping the setting of the other parameters

t = Transaction(doc, "adjust view_templates")
t.Start()

for view_template in view_templates:
    set_param_list = List[ElementId]()
    set_param_list.Add(switch_off_param_id)
    
    non_controlled_param_ids = view_template.GetNonControlledTemplateParameterIds()
    
    for param_id in non_controlled_param_ids:
        set_param_list.Add(param_id)
        
    view_template.SetNonControlledTemplateParameterIds(set_param_list)

t.Commit()
