# Overpass API

## Links
Python Overpass API Docs - https://python-overpy.readthedocs.io/en/latest/introduction.html#usage
Overpass API Docs - https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example

Forum Post Regarding Extracting Land Use - https://forum.openstreetmap.org/viewtopic.php?id=24738

## Relevant Query Methods
"""
Relative to other elements (around)
Information
- When possible, consider using the bounding box query filter instead of the around query filter. 
- The bounding box query filter performs faster.
- The around filter selects all elements within a certain radius 
around the elements in the input set. If you provide coordinates, then these coordinates are used instead of the input set. The input set can be changed with an adapted prefix notation. As for all filters, the result set is specified by the whole statement, not the individual filter.

A radius of 0 can be used for a way intersection test on outer/inner points.

Syntax: It consists of an opening parenthesis. Then follows the keyword around. 
Then follows optionally an input set declaration. Then follows a single floating 
point number that denotes the radius in meters. The filter either ends with a closing 
parenthesis or is followed by two comma separated floating point numbers indicating latitude
 and longitude and then finally a closing parenthesis.
"""

"""
By polygon (poly)
The polygon filter selects all elements of the chosen type inside the given polygon.

It has no input set. As for all filters, the result set is specified by the whole statement, not the individual filter.

It consists of an opening parenthesis. Then follows the keyword poly. Then follows a string
containing an even number of floating point numbers, divided only by whitespace.
Each pair of floating point numbers 
represents a coordinate, in order latitude, then longitude. The filter ends with a closing parenthesis:
"""