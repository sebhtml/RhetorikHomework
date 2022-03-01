
class HeightsToPoints:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def __call__(self, heights):
        """
        Convert a list of heights to a list of points.
        :param     list<int>                heights    list of heights
        :return    list<tuple<int,int>>                list of points
        """
        x = 0
        points = []
        for height in heights:
            point = (x, height)
            x += 1
            points.append(point)

        return points
