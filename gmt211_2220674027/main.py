from dp import *

# GeoJSON Testi
input_file = 'bodrum.geojson'
out_file = 'out.geojson'
epsilon = 0.01

try:
    execute_douglas_peucker(input_file, out_file, epsilon)
except FileNotFoundError:
    pass

# Line.txt Testi (Epsilon = 6)
input_line_file = "Line.txt"
try:
    input_line = convert_coordinates_to_line(input_line_file)
    result_list_6 = douglas_peucker(input_line, epsilon=6)
    for pt in result_list_6:
        print(f"{pt[0]} {pt[1]}")
except FileNotFoundError:
    pass

# Line.txt Testi (Epsilon = 0.1)
try:
    input_line = convert_coordinates_to_line(input_line_file)
    result_list_01 = douglas_peucker(input_line, epsilon=0.1)
    for pt in result_list_01:
        print(f"{pt[0]} {pt[1]}")
except FileNotFoundError:
    pass