import math


def perpendicular_distance(point, start, end):

    x0, y0 = point
    x1, y1 = start
    x2, y2 = end

    if x1 == x2 and y1 == y2:

        return math.sqrt(
            (x0 - x1) ** 2 +
            (y0 - y1) ** 2
        )

    numerator = abs(
        (y2 - y1) * x0
        - (x2 - x1) * y0
        + x2 * y1
        - y2 * x1
    )

    denominator = math.sqrt(
        (y2 - y1) ** 2 +
        (x2 - x1) ** 2
    )

    return numerator / denominator


def douglas_peucker(points, epsilon):

    if len(points) < 3:
        return points

    max_distance = 0
    index = 0

    start = points[0]
    end = points[-1]

    for i in range(1, len(points) - 1):

        distance = perpendicular_distance(
            points[i],
            start,
            end
        )

        if distance > max_distance:
            max_distance = distance
            index = i

    if max_distance > epsilon:

        left = douglas_peucker(
            points[:index + 1],
            epsilon
        )

        right = douglas_peucker(
            points[index:],
            epsilon
        )

        return left[:-1] + right

    else:

        return [start, end]