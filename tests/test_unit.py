import unittest
from parameterized import parameterized
import math
from test_task import Square, Rectangle, Circle


class TestShapes(unittest.TestCase):
    @parameterized.expand(
        [
            ("square", Square(0, 0, 2), 8, 4),
            ("rectangle", Rectangle(0, 0, 3, 4), 14, 12),
            ("circle", Circle(0, 0, 3), 2 * math.pi * 3, math.pi * 3**2),
        ]
    )
    def test_shapes(self, name, shape, expected_perimeter, expected_area):
        if isinstance(shape, Circle):
            self.assertAlmostEqual(shape.perimeter(), expected_perimeter, places=5)
            self.assertAlmostEqual(shape.area(), expected_area, places=5)
        else:
            self.assertEqual(shape.perimeter(), expected_perimeter)
            self.assertEqual(shape.area(), expected_area)


if __name__ == "__main__":
    unittest.main()
