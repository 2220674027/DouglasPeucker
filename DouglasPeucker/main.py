import sys
import json

from dp import douglas_peucker


def read_txt(filename):

    points = []

    with open(filename, "r") as file:

        for line in file:

            x, y = map(float, line.strip().split())

            points.append((x, y))

    return points


def write_txt(filename, points):

    with open(filename, "w") as file:

        for point in points:

            file.write(
                f"{point[0]} {point[1]}\n"
            )


def read_geojson(filename):

    with open(filename, "r") as file:

        data = json.load(file)

    coords = data["features"][0]["geometry"]["coordinates"]

    points = []

    for c in coords:

        points.append((c[0], c[1]))

    return points, data


def write_geojson(filename, points, data):

    coords = []

    for p in points:

        coords.append([p[0], p[1]])

    data["features"][0]["geometry"]["coordinates"] = coords

    with open(filename, "w") as file:

        json.dump(data, file, indent=4)


def main():

    if len(sys.argv) != 4:

        print(
            "Usage: python main.py input output epsilon"
        )

        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    epsilon = float(sys.argv[3])

    if input_file.endswith(".txt"):

        points = read_txt(input_file)

        simplified = douglas_peucker(
            points,
            epsilon
        )

        write_txt(output_file, simplified)

    elif input_file.endswith(".geojson"):

        points, data = read_geojson(input_file)

        simplified = douglas_peucker(
            points,
            epsilon
        )

        write_geojson(
            output_file,
            simplified,
            data
        )

    else:

        print("Unsupported file format")


if __name__ == "__main__":
    main()