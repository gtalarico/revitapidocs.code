# Wrap & Unwrap

#### **U**nwrapElement

“All Elements coming out of Dynamo Nodes are actually wrappers around core Revit Elements. Inside of Python, you can operate on these types directly by calling our nodes from inside of Python, which are all located in the Revit.Elements namespace \[.. \].  


If you would prefer to use the RevitAPI directly, you will need to unwrap the Element before operating on it, use our TransactionManager to ensure that you're operating inside of a RevitAPI Transaction, and wrap any Element you wish to return.”  


#### Wrapping

“In order to interoperate with our Revit nodes, any raw Autodesk.Revit.DB.Element being returned from a Python script must be wrapped in a Revit.Elements.Element. This can be done by using the ToDSType\(bool\) extension method. The bool argument determines whether or not the Element is "Revit-owned." This distinction is important: Revit-owned Elements are not controlled by Dynamo, non-Revit-owned Elements are. Basically, if you are creating a new Element in your Python script, then you should not mark the wrapped Element as Revit-owned. If you are selecting an Element from the Document, then you should mark the wrapped Element as Revit-owned.”  
  


```python
clr.AddReference("RevitNodes")
import Revit
# Adds ToDSType(bool) extension method to Wrapped elements
clr.ImportExtensions(Revit.Elements)
# Adds ToProtoType, ToRevitType geometry conversion extension methods
clr.ImportExtensions(Revit.GeometryConversion)
```

> Sources:  
> [https://github.com/gtalarico/au2017](https://github.com/gtalarico/au2017)



