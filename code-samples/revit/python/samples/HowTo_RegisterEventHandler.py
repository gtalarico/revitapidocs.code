"""
Register Event Handler

TESTED REVIT API: -

Author: Ehsan Iran Nejad | https://github.com/eirannejad/

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
"""

# https://github.com/eirannejad/pyRevit/issues/201
# Relevant Links:
# http://www.revitapidocs.com/2017.1/fb46d2bd-92bf-1cc5-79ad-f253f3e875d8.htm
# http://www.revitapidocs.com/2017.1/b69e9d33-3c49-e895-3267-7daabab85fdf.htm

from System import EventHandler, Uri
from Autodesk.Revit.UI.Events import ViewActivatedEventArgs, ViewActivatingEventArgs

def event_handler_function(sender, args):
    # do the even stuff here
    pass

# I'm using ViewActivating event here as example.
# The handler function will be executed every time a Revit view is activated:
__revit__.ViewActivating += EventHandler[ViewActivatingEventArgs](event_handler_function)
