import math
import json

def perpendicular_distance(point, line_start, line_end):
    x0, y0 = point
    x1, y1 = line_start
    x2, y2 = line_end
    
    if x1 == x2 and y1 == y2:
        return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    
    numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    
    return numerator / denominator

def douglas_peucker(point_list, epsilon):
    if len(point_list) <= 2:
        return point_list
    
    start_point = point_list[0]
    end_point = point_list[-1]
    
    max_dist = 0.0
    index_of_max_dist = 0
    
    for i in range(1, len(point_list) - 1):
        dist = perpendicular_distance(point_list[i], start_point, end_point)
        if dist > max_dist:
            max_dist = dist
            index_of_max_dist = i
            
    if max_dist > epsilon:
        left_results = douglas_peucker(point_list[:index_of_max_dist + 1], epsilon)
        right_results = douglas_peucker(point_list[index_of_max_dist:], epsilon)
        return left_results[:-1] + right_results
    else:
        return [start_point, end_point]

def convert_coordinates_to_line(file_path):
    points = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                points.append([float(parts[0]), float(parts[1])])
    return points

def execute_douglas_peucker(input_file, out_file, epsilon):
    with open(input_file, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
        
    if geojson_data.get("type") == "FeatureCollection":
        for feature in geojson_data.get("features", []):
            geom = feature.get("geometry", {})
            if geom.get("type") == "LineString":
                geom["coordinates"] = douglas_peucker(geom["coordinates"], epsilon)
            elif geom.get("type") == "MultiLineString":
                new_coords = []
                for line in geom["coordinates"]:
                    new_coords.append(douglas_peucker(line, epsilon))
                geom["coordinates"] = new_coords
    elif geojson_data.get("type") == "LineString":
        geojson_data["coordinates"] = douglas_peucker(geojson_data["coordinates"], epsilon)
        
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(geojson_data, f, indent=4)