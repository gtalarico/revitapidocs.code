from Autodesk.Revit.DB import Phase, FilteredElementCollector

def get_phase_by_name(phase_name):
	phase_collector = FilteredElementCollector(doc).OfClass(Phase)
	for phase in phase_collector:
 		if phase.Name.Equals(phase_name):
  			return phase
  			
phase = get_phase_by_name('01 - Existing')
print phase.Name
print phase.Id
