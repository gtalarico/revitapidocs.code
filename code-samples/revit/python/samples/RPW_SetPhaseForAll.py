"""
Forcefully set the phase for all Selected Objects.
User will be prompted with a simple form to select the desired phase

Requires rpw library: github.com/gtalarico/revitpythonwrapper

TESTED REVIT API: -

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import rpw
from rpw import doc

selection = rpw.Selection()
phases = [p for p in doc.Phases]

phase_options = {p.Name: p for p in phases}

form = rpw.forms.SelectFromList('Set Phase', phase_options.keys(),
                                description='Select a Phase')
form_ok = form.show()
phase = phase_options[form.selected]

with rpw.TransactionGroup('Set Phases'):
    for element in selection:
        element = rpw.Element(element)
        with rpw.Transaction('Set Element Phase'):
            try:
                element.parameters.builtins['PHASE_CREATED'].value = phase.Id
            except rpw.exceptions.RPW_Exception:
                pass
