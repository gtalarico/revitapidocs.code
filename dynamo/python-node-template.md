# Python Node Template

## **Starter Code Template**

The code below is provided by default every time a Python Node is created \*. It does not have to be used as is, but we will go through it as line-by-line as an example as some of the concepts are commonly used and helpful to understand.

\* Dynamo releases after Aug. 2017  allows the user to configure the default template - see [Github PR](https://github.com/DynamoDS/Dynamo/pull/8122).

```python
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

#Assign your output to the OUT variable.
OUT = 0
```

The first line `import clr`  imports the Common Language Runtime module `clr`. This module is needed to interact with libraries that are written in .NET languages.

{% hint style="info" %}
**`AddReference()`** automatically resolves the extension, hence why .dll can be omitted.   
The actual dll assembly typically  can be found here: `C:\Program Files\Dynamo\Dynamo Core\1.X`
{% endhint %}

'The second line, uses the `clr.AddReference()` method to load a reference to .NET dll assembly `ProtoGeometry`.

Once an assembly reference is loaded, their corresponding namespaces become available to be imported. The table below lists commonly used assemblies and the corresponding namespaces they enable.

| **Assembly** | **Namespace Loaded** | **Usage example** |
| --- | --- | --- | --- | --- | --- | --- |
| ProtoGeometry | Autodesk.DesignScript | from Autodesk.DesignScript.Geometry import Vector |
| RevitAPI | Autodesk.Revit.DB | from Autodesk.Revit.DB import Wall |
| RevitAPIUI | Autodesk.Revit.UI | from Autodesk.Revit.UI import TaskDialog |
| RevitServices | RevitServices | from RevitServices.Persistence import DocumentManager |
| RevitNodes | Revit | from Revit import Elements |
| DSCoreNodes | DSCore | from DSCore import Color |

In other words, once we add a reference to the `Protogeometry.dll,`the corresponding Namespace becomes available: `Autodesk.DesignScript`

And finally, the last few lines:

```python
#The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN
#Assign your output to the OUT variable.
OUT = 0
```

`dataEnteringNode` creates a variable and assigns the value of `IN`. This line is not needed and and it only needs to be used if you want to refer to the `IN` variable using the name `dataEnteringNode`.

`OUT = 0` is only a placeholder, to indicate to uses that the `OUT` variable should receive a value.  


{% hint style="info" %}
 **Design Script** is a Geometry library created by Autodesk it is the main Geometry engine used by Dynamo to create and operate on Geometry. Many, if not all of the classes available in DesignScript have a Dynamo Node counterpart \(ir. Vector.Length is available as Node as well as in Python\)
{% endhint %}

### **Note on '\*' Imports**

It’s worth mentioning that although the template uses the syntax from Namespace import \* , this is generally considered bad practice by the Python Community. The asterisk at the end tells Python to load all classes and methods inside the module. Depending on the namespace, you could be loading hundreds or even thousands of identifiers into the context of your script. This practice also has the following disadvantages:

1. Loading all modules can cause a namespace conflict. For example, if another module also contains a class with the same name, the first one loaded will be overwritten.
2. As objects loaded are used throughout our code, it’s hard for other programmers to tell from which one of the Assemblies/Namespaces the object came from.

A better solution is to either load only the class you need, or to reference them using the parent module. For example, if you want to use the Circle and Vector classes, you could use:

```python
from Autodesk.DesignScript.Geometry import Circle, Vector
# or alternatively
from Autodesk.DesignScript import Geometry
# The classes would then be accessed using: Geometry.Circle and Geometry.Vector
```

This approach makes it more explicit what is being used, and also avoid name clashes with other modules.

## **Customized Starter Code Template**

The default template provided rarely provides everything we need. Over time, most users will develop their own “boilerplate” code with everything they typically use.  


The code below is an example of what is commonly used as boilerplate.

We will touch on some of these imports and why they are needed later in this document.  
****

```python
import clr
# Import RevitAPI Classes
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
# As explained in the previous section, replace * with the class you need separated by comma.

clr.AddReference("RevitNodes")
import Revit
# Adds ToDSType (bool) extension method to Wrapped elements
clr.ImportExtensions(Revit.Elements)
# Adds ToProtoType, ToRevitType geometry conversion extension methods to objects
clr.ImportExtensions(Revit.GeometryConversion)

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
from RevitServices.Transactions import TransactionManager
from RevitServices.Persistence import DocumentManager# Create variable for Revit Document
doc = DocumentManager.Instance.CurrentDBDocument

# Start Transaction
TransactionManager.Instance.EnsureInTransaction(doc)
# Code that modifies Revit Database goes Here
# End Transaction
TransactionManager.Instance.TransactionTaskDone()

OUT = None
```

> Sources:   
> [https://github.com/gtalarico/au2017](https://github.com/gtalarico/au2017)



