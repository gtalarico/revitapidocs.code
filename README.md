# Revit API Docs - Code Samples

Code Sample Repository for [RevitAPIdocs.com](http://www.revitapidocs.com)

This repository allows the Revit API Community to contribute to the Code Samples section of Revit API Docs.

## How does this work?

The [Code Samples](http://www.revitapidocs.com/code) page uses the Github API to read this repository and inject the text into the browser. Note that for performance reasons, the code is Cached and will only be refreshed every 6 hours.

## Contriutions

### Who can contribute?

Anyone writes Revit API code and would like to share them with the community.

### What languages are accepted?

Python, CSharp

#### One off contributions
1. [Fork this repository](https://github.com/gtalarico/revitapidocs/fork)
2. Add / Modify the scripts on your fork
3. Create a [Pull Request](https://github.com/gtalarico/revitapidocs/compare)

    (More info on how to Create a Pull Request from your for [here](https://help.github.com/articles/creating-a-pull-request-from-a-fork/))

#### Regular contributions

1. Create an Issue Requesting to be added as a Contributor in the [Issues Page](https://github.com/gtalarico/revitapidocs/issues)
2. Once you have been added as a contributor, you will be able to Push directly to the repository.

### Notes:

1. Scripts should be placed in the appropriate folder, and have the expected extension for that language.
2. The filename should be {Category}_{Name}.{ext}, for example: `Snippets_CreateDraftingView.py`
3. The categories are only loosely defined, but I would be happy to revise them as the code base grows.
4. Scripts must include the license and other information described below.

## License and Credits

All contributions added to this repository will be shared using the MIT License.
Authors can include their own credits, but they must also keep the following
notes at the beginning of every file in the repository:

### Credits

All scripts should include the follwing at the beginning of the file:

    {Description}
    
    Tested Revit API: {comma separated years}

    Author: {Name| {email, and or github page of Author} - optional

    This file is part of www.revitapidocs.com
    For more information visit http://github.com/gtalarico/revitapidocs
    License: http://github.com/gtalarico/revitapidocs/master/

#### Examples

    Filename: CreateDraftingView.py
    
    Creates a drafting view
    TESTED REVIT API: 2015
    
    Author: Gui Talarico | github.com.gtalarico
    
    This file is part of www.revitapidocs.com
    For more information visit http://github.com/gtalarico/revitapidocs
    License: http://github.com/gtalarico/revitapidocs/master/

