"""
By polygon (poly)
The polygon filter selects all elements of the chosen type inside the given polygon.

It has no input set. As for all filters, the result set is specified by the whole statement, not the individual filter.

It consists of an opening parenthesis. Then follows the keyword poly. Then follows a string
containing an even number of floating point numbers, divided only by whitespace.
Each pair of floating point numbers 
represents a coordinate, in order latitude, then longitude. The filter ends with a closing parenthesis:
"""


import overpy
api = overpy.Overpass()
result = api.query("""node(around:1000.0,50.75,6.05);out;""")
print(len(result.nodes))
print(result.nodes[0])