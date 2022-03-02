#!/usr/bin/env python

import math
import unittest
import liquid_calculator

class TestLinearInterpolator(unittest.TestCase):
    def test_case_1(self):
        p0 = (50, 100)
        p1 = (150, 200)
        points = [p0, p1]
        halfedge = liquid_calculator.EdgeSplit(0, 1, 0.5)
        interpolator = liquid_calculator.LinearInterpolator()
        interpolated_point = interpolator(halfedge, points)
        self.assertEqual(interpolated_point, (100, 150))

    def test_case_1(self):
        p0 = (50, 100)
        p1 = (150, 200)
        points = [p0, p1]
        halfedge = liquid_calculator.EdgeSplit(0, 1, 0.20)
        interpolator = liquid_calculator.LinearInterpolator()
        interpolated_point = interpolator(halfedge, points)
        self.assertEqual(interpolated_point, (70, 120))

class TestConvexAreas(unittest.TestCase):
    def test_case_1(self):
        #
        # input = [1, 2, 4, 2, 4, 1]
        # output = 2
        #
        #
        #         *      *   - 4
        #                    |
        #                    - 3
        #                    |
        #      *     *       - 2
        #                    |
        #   *              * - 1
        #                    |
        #                    - 0
        #   |--|--|--|--|--|
        #   0  1  2  3  4  5
        heights = [1, 2, 4, 2, 4, 1]
        self.assertEqual(liquid_calculator.ConvexAreas()(heights), 2)

    def test_case_2(self):
        #
        # input = [5,1,3,4,5]
        # output = 7
        #
        #
        #   *           *    - 5
        #                    |
        #            *       - 4
        #                    |
        #         *          - 3
        #                    |
        #                    - 2
        #                    |
        #      *             - 1
        #                    |
        #                    - 0
        #   |--|--|--|--|--|
        #   0  1  2  3  4  5
        heights = [5, 1, 3, 4, 5]
        self.assertEqual(liquid_calculator.ConvexAreas()(heights), 7)

    def test_case_3(self):
        #
        # input = [4,3,4,3,4]
        # output = 2
        #
        #
        #                    - 5
        #                    |
        #   *     *     *    - 4
        #                    |
        #      *     *       - 3
        #                    |
        #                    - 2
        #                    |
        #                    - 1
        #                    |
        #                    - 0
        #   |--|--|--|--|--|
        #   0  1  2  3  4  5
        heights = [4, 3, 4, 3, 4]
        self.assertEqual(liquid_calculator.ConvexAreas()(heights), 2)

    def test_convex_area_with_linear_algebra_1(self):
        #
        # input = [2,1,4]
        # output = 2
        #
        #
        #                    - 5
        #                    |
        #         *          - 4
        #                    |
        #                    - 3
        #                    |
        #   *                - 2      --------- water level
        #                    |
        #      *             - 1
        #                    |
        #                    - 0
        #   |--|--|--|--|--|
        #   0  1  2  3  4  5

        # the water level will touch the right wall at
        # point = {
        #           x: 1 + (2-1)*(2/(4-1)),
        #           y: 2
        #         }
        #

        p0 = (0,2)
        p1 = (1,1)
        p2 = (2,4)
        points = [p0, p1, p2]
        parameter = (p0[1] - p1[1] + 0.0) / (p2[1] - p1[1] + 0.0)
        halfedge = liquid_calculator.EdgeSplit(1, 2, parameter)
        interpolator = liquid_calculator.LinearInterpolator()
        interpolated_point = interpolator(halfedge, points)

        expected_area = 0
        expected_area += abs((p1[0] - p0[0]) * (p1[1] - p0[1]) / 2)
        expected_area += abs((interpolated_point[0] - p1[0]) * (interpolated_point[1] - p1[1]) / 2)

        heights = [p0[1], p1[1], p2[1]]
        actual_area = liquid_calculator.ConvexAreas()(heights)

        self.assertEqual(math.isclose(actual_area, expected_area, rel_tol=1e-9), True)


if __name__ == '__main__':
    unittest.main()

