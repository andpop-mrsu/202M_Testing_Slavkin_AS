import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleFunction(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")
    
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(4, 5, 6), "nonequilateral")
    
    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 5, 5)
    
    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-3, 4, 5)
    
    def test_invalid_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

if __name__ == "__main__":
    unittest.main()