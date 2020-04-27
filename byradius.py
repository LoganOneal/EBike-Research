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


import overpy
api = overpy.Overpass()

radius = 1000.0
lat =  50.75
lon = 6.05

result = api.query("node(around:"+str(radius)+","+str(lat)+","+str(lon)+");out;")

print(len(result.nodes))
#print(result.nodes[0].tags)

for node in result.nodes:
    print(node)