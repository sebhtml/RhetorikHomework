
import functools

class Polygon:
    def __init__(self, points):
        self.points = points

    def area(self):
        simplices = []
        i = 0
        while i != len(self.points):
            next_i = (i + 1) % len(self.points)
            simplex = (i, next_i)
            simplices.append(simplex)
            i += 1

        def simplex_area(simplex):
            first_point = self.points[simplex[0]]
            last_point = self.points[simplex[1]]
            return ((last_point[1] + first_point[1]) * (last_point[0] - first_point[0])) / 2

        simplex_areas = map(simplex_area, simplices)
        return functools.reduce(lambda area1, area2: area1 + area2, simplex_areas, 0)
