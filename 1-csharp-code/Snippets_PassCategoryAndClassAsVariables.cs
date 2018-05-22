/*
Pass Category and Class as Variables
This snippet shows how to programatically extract the BuiltInCategory and Class Type 
information from an element and pass it to a FilteredElementCollector

It is useful when working with generic elements without knowing their category or class ahead of time
or as a demonstration of BuiltInCategory and typeof(System.Type) concepts

TESTED REVIT API: 2017
The snippet can be used as is in a Revit Application Macro for test purposes

Author: Deyan Nenov | github.com/ArchilizerLtd

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
License: http://github.com/gtalarico/revitapidocs/blob/master/LICENSE.md
*/

public void PassCategoryAndClassAsVariables()
{
	UIDocument uidoc = this.ActiveUIDocument;
	Document doc = uidoc.Document;
	
	var element = doc.GetElement(uidoc.Selection.PickObject(ObjectType.Element, "Pick test subject").ElementId);
	var type = element.GetType();	//if a Wall element is picked, this substiutes *typeof(Wall)* 
	var bic = (BuiltInCategory)element.Category.Id.IntegerValue	//if a Wall element is picked, this substitutes *BuiltInCategory.OST_Walls*
	
	FilteredElementCollector collector 
	      = new FilteredElementCollector( doc );
	
	collector.OfCategory(bic);
	collector.OfClass(type);
     
	// Select all elements of the same Category and Class
	uidoc.Selection.SetElementIds( collector.ToElementIds() );
}