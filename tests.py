#!/usr/bin/env python

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

if __name__ == '__main__':
    unittest.main()

