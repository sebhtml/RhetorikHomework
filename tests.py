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
        self.assertEqual(liquid_calculator.ConvexAreas()([1, 2, 4, 2, 4, 1]), 2)
    
if __name__ == '__main__':
    unittest.main()

