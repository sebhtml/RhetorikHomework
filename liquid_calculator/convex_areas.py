
from .heights_to_points import HeightsToPoints
from .polygon import Polygon
from .linear_interpolator import EdgeSplit
from .linear_interpolator import LinearInterpolator

def get_lake_area(points, lake_first_point, lake_last_point):
    first_y = points[lake_first_point][1]
    last_y = points[lake_last_point][1]
    if first_y == last_y:
        polygon_points = []
        for i in range(lake_first_point, lake_last_point + 1):
            polygon_points.append(points[i])
        return -Polygon(polygon_points).area()
    elif first_y < last_y:
        polygon_points = []
        for i in range(lake_first_point, lake_last_point):
            polygon_points.append(points[i])
        previous_to_last_y = points[lake_last_point - 1][1]
        parameter = (first_y -previous_to_last_y + 0.0) / (last_y - previous_to_last_y)
        halfedge = EdgeSplit(lake_last_point - 1, lake_last_point, parameter)
        interpolated_point = LinearInterpolator()(halfedge, points)
        polygon_points.append(interpolated_point)
        return -Polygon(polygon_points).area()

    raise Exception("Not implemented yet.")

class ConvexAreas:
    pass

    def __call__(self, heights):
        points = HeightsToPoints()(heights)
        sum = 0

        lake_first_point = None
        lake_last_point = None
        current_point = 0

        while current_point != len(points):
            if lake_first_point == None:
                lake_first_point = current_point
                lake_last_point = current_point
            else:
                first_y = points[lake_first_point][1]
                current_y = points[current_point][1]
                if current_y < first_y:
                    # extend the lake
                    lake_last_point = current_point
                else:
                    lake_last_point = current_point
                    if (lake_last_point - lake_first_point) > 1:
                        # close the lake
                        sum += get_lake_area(points, lake_first_point, lake_last_point)
                    # Reset lake
                    lake_first_point = current_point
                    lake_last_point = current_point
                current_point += 1
        return sum
