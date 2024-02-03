from unittest import TestCase, skip
from triangle.triangle import Triangle, TriangleType


class TriangleTestCase(TestCase):
    def test_triangle_ok(self):
        triangle = Triangle([3, 4, 5])
        self.assertEqual(TriangleType.RIGHT, triangle.get_type())

    def test_triangle_acute(self):
        triangle = Triangle([3, 4, 4])
        self.assertEqual(TriangleType.ACUTE, triangle.get_type())

    def test_triangle_obtuse(self):
        triangle = Triangle([3, 4, 6])
        self.assertEqual(TriangleType.OBTUSE, triangle.get_type())

    @skip
    def test_line_triangle(self):
        with self.assertRaises(ValueError) as exception:
            triangle = Triangle([3, 4, 7])
        