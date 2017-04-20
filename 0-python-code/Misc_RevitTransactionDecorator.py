"""
Revit Transaction Decorator function.
This allows you to create functions that make changes to the revit document
without having to repeat the code to start/commit transactions.
Just add the revit_transaction decorator and a transaction will be started before
your function is called, and then commit after the call

TESTED REVIT API: 2015, 2016, 2017, 2017.1

Author: Gui Talarico | github.com/gtalarico

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

from functools import wraps
from Autodesk.Revit.Exceptions import InvalidOperationException

def revit_transaction(transaction_name):
    def wrap(f):
        @wraps(f)
        def wrapped_f(*args):
            try:
                t = Transaction(doc, transaction_name)
                t.Start()
            except InvalidOperationException as errmsg:
                print('Transaciton Error: {}'.format(errmsg))
                return_value = f(*args)
            else:
                return_value = f(*args)
                t.Commit()
            return return_value
        return wrapped_f
    return wrap


#Example
@revit_transaction('Create Text')
def create_text(view, text, point, align):
    baseVec = XYZ.BasisX
    upVec = XYZ.BasisZ
    text_size = 10
    text_length = 0.5
    text = str(text)
    align_options = {'left': TextAlignFlags.TEF_ALIGN_LEFT |
                             TextAlignFlags.TEF_ALIGN_MIDDLE,
                     'right': TextAlignFlags.TEF_ALIGN_RIGHT |
                             TextAlignFlags.TEF_ALIGN_MIDDLE
                     }

    text_element = doc.Create.NewTextNote(view, point, baseVec, upVec, text_length,
                                          align_options[align], text)
