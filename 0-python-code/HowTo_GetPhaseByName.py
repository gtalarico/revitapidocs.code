"""
Retrieves a phase by its Name

TESTED REVIT API: -

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""


from Autodesk.Revit.DB import Phase, FilteredElementCollector

def get_phase_by_name(phase_name):
	phase_collector = FilteredElementCollector(doc).OfClass(Phase)
	for phase in phase_collector:
 		if phase.Name.Equals(phase_name):
  			return phase

phase = get_phase_by_name('01 - Existing')
print phase.Name
print phase.Id
