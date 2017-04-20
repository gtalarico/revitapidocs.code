"""
Create a text annotation element.
Does not include start/commit transaction.

TESTED REVIT API: -

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""


def create_text(view, text, point, align):
    """Creates a Revit Text.
    create_test(view, text_string, point)
    view: view object to insert text
    text: text to be inserted
    point: insertion point - XYZ() instance
    align: 'left', 'right', or 'center'
    """
    baseVec = XYZ.BasisX
    upVec = XYZ.BasisZ
    text_size = 10
    text_length = 0.5
    text = str(text)

    align_options = {'left': TextAlignFlags.TEF_ALIGN_LEFT |
                             TextAlignFlags.TEF_ALIGN_MIDDLE,
                     'right': TextAlignFlags.TEF_ALIGN_RIGHT |
                             TextAlignFlags.TEF_ALIGN_MIDDLE,
                     'center': TextAlignFlags.TEF_ALIGN_CENTER |
                             TextAlignFlags.TEF_ALIGN_MIDDLE,
                     }

    text_element = doc.Create.NewTextNote(view, point, baseVec, upVec,
                                          text_length,
                                          align_options[align],
                                          text)
