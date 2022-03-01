#!/usr/bin/env python

import unittest
import liquid_calculator

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


if __name__ == '__main__':
    unittest.main()

