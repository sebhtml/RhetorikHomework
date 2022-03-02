

class EdgeSplit:
    def __init__(self, from_index, to_index, parameter):
        self.from_index = from_index
        self.to_index = to_index
        self.parameter = parameter

def interpolate(from_value, to_value, parameter):
    return from_value + (to_value - from_value) * parameter

class LinearInterpolator:
    def __call__(self, halfedge, points):
        x1 = points[halfedge.from_index][0]
        y1 = points[halfedge.from_index][1]
        x2 = points[halfedge.to_index][0]
        y2 = points[halfedge.to_index][1]
        interpolated_x = interpolate(x1, x2, halfedge.parameter)
        interpolated_y = interpolate(y1, y2, halfedge.parameter)
        return (interpolated_x, interpolated_y)


