#!/usr/bin/env python3

import unittest.mock
from unittest.mock import call
import draw


class TestDraw(unittest.TestCase):
    def test_parse_command_1(self):
        self.assertEqual([("F", 100), ("T", 90), ("F", 100), ("T", 90), ("F", 100), ("T", 90), ("F", 100)],
                         draw.parse_command("F100;T90;F100;T90;F100;T90;F100"))
        self.assertEqual([("R", 4), ("F", 100), ("T", 90), ("E", 0)],
                         draw.parse_command("R4;F100;T90;E0"))
        self.assertEqual([("R", 5), ("F", 80), ("T", -72), ("E", 0)],
                         draw.parse_command("R5;F80;T-72;E0"))

    def test_parse_command_2(self):
        self.assertEqual([("F", 100), ("T", 90), ("F", 100), ("T", 90), ("F", 100), ("T", 90), ("F", 100)],
                         draw.parse_command("F100T90F100T90F100T90F100"))
        self.assertEqual([("R", 4), ("F", 100), ("T", 90), ("E", 0)],
                         draw.parse_command("R4F100T90E0"))
        self.assertEqual([("R", 5), ("F", 80), ("T", -72), ("E", 0)],
                         draw.parse_command("R5F80T-72E0"))

    @unittest.mock.patch("draw.turtle")
    def test_run_commands(self, mock_turtle: unittest.mock.Mock):
        draw.run_commands([("R", 5), ("F", 80), ("T", -72), ("E", 0)])
        self.assertEqual(mock_turtle.method_calls,
                         [call.forward(80),
                          call.left(-72),
                          call.forward(80),
                          call.left(-72),
                          call.forward(80),
                          call.left(-72),
                          call.forward(80),
                          call.left(-72),
                          call.forward(80),
                          call.left(-72)])


if __name__ == "__main__":
    unittest.main()
