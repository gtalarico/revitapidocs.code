"""
Creates a TaskDialog

TESTED REVIT API: -

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

# Results here: https://imgur.com/4DiPYfe

from Autodesk.Revit.UI import (TaskDialog, TaskDialogCommonButtons,
                               TaskDialogCommandLinkId, TaskDialogResult)

title = 'Task Dialog Title'
dialog = TaskDialog(title)

# Properties
dialog.MainInstruction = 'Text Header'
dialog.MainContent = 'Text Content'
dialog.FooterText = 'Footer Text'
dialog.VerificationText = 'Verification Text'
# dialog.ExpandedContent = expanded_content

# Settings
dialog.TitleAutoPrefix = False
dialog.AllowCancellation = True

# Add Button
dialog.CommonButtons = TaskDialogCommonButtons.Ok | TaskDialogCommonButtons.Yes

# Set Default Button
dialog.DefaultButton = TaskDialogResult.None

# Add Command Link
dialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink1,
                      'Command Button Text',
                      'Command Button Sub Text')
dialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink2,
                      'Command Button Text 2',
                      'Command Button Sub Text 2')

result = dialog.Show()

if result == TaskDialogResult.Ok:
    print('Dialog was OK')
if result == TaskDialogResult.Yes:
    print('Dialog was Yes')
if result == TaskDialogResult.Cancel:
    print('Dialog was Cancelled')
if result == TaskDialogResult.CommandLink1:
    print('Button Was Pressed')
if result == TaskDialogResult.CommandLink2:
    print('Button 2 Was Pressed')
if dialog.WasVerificationChecked():
    print('Verification was Checked')

