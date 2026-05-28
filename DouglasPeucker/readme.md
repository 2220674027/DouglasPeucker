# Douglas Peucker Algorithm

This project implements the Douglas-Peucker line simplification algorithm using pure Python.

## Features

- Recursive Douglas-Peucker implementation
- TXT input support
- GeoJSON input support
- Adjustable epsilon parameter
- No NumPy or SciPy used

## Usage

### TXT Example

python main.py input.txt output.txt 1

### GeoJSON Example

python main.py coastline.geojson output.geojson 0.005