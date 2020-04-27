import overpass
import shapely.geometry as geometry
from shapely.ops import linemerge, unary_union, polygonize

api = overpy.Overpass()

query = """ YOUR QUERY HERE """
response = api.query(query)

lss = [] #convert ways to linstrings

for ii_w,way in enumerate(response.ways):
    ls_coords = []

    for node in way.nodes:
        ls_coords.append((node.lon,node.lat)) # create a list of node coordinates

    lss.append(geometry.LineString(ls_coords)) # create a LineString from coords 


merged = linemerge([*lss]) # merge LineStrings
borders = unary_union(merged) # linestrings to a MultiLineString
polygons = list(polygonize(borders))