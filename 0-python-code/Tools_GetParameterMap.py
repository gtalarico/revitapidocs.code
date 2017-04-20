"""
Prints a Parameter map of the first element in selection.
Where applicable it prints Instance and type parameter map.
Returns a parameter dict.

TESTED REVIT API: 2015, 2016

Author: Frederic Beaupere | hdm-dt-fb

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
clr.AddReference("RevitAPI")

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

selection = [doc.GetElement(elId) for elId in uidoc.Selection.GetElementIds()]


def print_param_mapping(param_dict):
    """
    Prints a key value pairs of the parameter dict
    Args:
        param_dict: 
    Returns:
    """
    for key in param_dict:
        print(35 * "-")
        print(key)
        print(param_dict[key])


def get_parameter_map(element):
    """
    Retrieve an overview of parameters of the provided element.
    Prints out the gathered parameter information
    Args:
        element: Element that holds the parameters.
    Returns:
        Returns two dictionaries: Instance dict, Type dict.
        If no type is available second dict is None
    """

    print("\nINSTANCE PARAMETERS" + 50 * "_")
    inst_map = collect_params(element)
    print_param_mapping(inst_map)

    type_map = None
    if "Symbol" in dir(element):
        print("\nTYPE PARAMETERS" + 50 * "_")
        elem_symbol = element.Symbol
        type_map = collect_params(elem_symbol)
        print_param_mapping(type_map)

    return inst_map, type_map


def collect_params(param_element):
    """
    Collects parameters of the provided element.
    Args:
        param_element: Element that holds the parameters.
    Returns:
        Returns a dictionary, with parameters.
    """

    parameters = param_element.Parameters
    param_dict = defaultdict(list)

    for param in parameters:
        param_dict[param.Definition.Name].append(param.StorageType.ToString().split(".")[-1])
        param_dict[param.Definition.Name].append(param.HasValue)

        param_value = None
        if param.HasValue:
            if param.StorageType.ToString() == "ElementId":
                param_value = param.AsElementId().IntegerValue
            elif param.StorageType.ToString() == "Integer":
                param_value = param.AsInteger()
            elif param.StorageType.ToString() == "Double":
                param_value = param.AsDouble()
            elif param.StorageType.ToString() == "String":
                param_value = param.AsString()
        param_dict[param.Definition.Name].append(str(param_value))

    return param_dict

if selection.Count > 0:
    get_parameter_map(selection[0])
else:
    print("please select an element.")
