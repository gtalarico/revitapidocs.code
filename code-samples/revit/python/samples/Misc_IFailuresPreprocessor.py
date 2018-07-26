"""
IFailuresPreprocessor Example
Places an unenclosed room in a project and removes the warning
from transaction via the IFailuresPreprocessor

TESTED REVIT API: 2015

Author: Frederic Beaupere | github.com/hdm-dt-fb

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

import clr
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import Transaction, IFailuresPreprocessor, BuiltInFailures, UV
from System.Collections.Generic import List

doc = __revit__.ActiveUIDocument.Document
active_view = doc.ActiveView
active_lvl = active_view.GenLevel


class RoomWarningSwallower(IFailuresPreprocessor):
    def PreprocessFailures(self, failuresAccessor):
        fail_list = List[FailureMessageAccessor]()
        fail_acc_list = failuresAccessor.GetFailureMessages().GetEnumerator()
        for failure in fail_acc_list:
            failure_id = failure.GetFailureDefinitionId()
            failure_severity = failure.GetSeverity()
            failure_type = BuiltInFailures.RoomFailures.RoomNotEnclosed
            if failure_id == failure_type:
                print("{0} with id: {1} of type: RoomNotEnclosed removed!".format(failure_severity, failure_id.Guid))
                failuresAccessor.DeleteWarning(failure)
        return FailureProcessingResult.Continue


# "Start" the transaction
tx = Transaction(doc, "place unenclosed room")
tx.Start()

options = tx.GetFailureHandlingOptions()
options.SetFailuresPreprocessor(RoomWarningSwallower())
tx.SetFailureHandlingOptions(options)

room = doc.Create.NewRoom(active_lvl, UV(0,0))

# "End" the transaction
tx.Commit()
