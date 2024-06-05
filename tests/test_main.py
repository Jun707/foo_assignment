import unittest
from .sphere import Sphere

class TestSphere(unittest.TestCase):
    def test_volume(self):
        sphere = Sphere(1)
        self.assertAlmostEqual(sphere.volume(), 4.1887902047863905)
        sphere = Sphere(0)
        self.assertAlmostEqual(sphere.volume(), 0)
        with self.assertRaises(ValueError):
            Sphere(-1)
            
if __name__ == '__main__':
    unittest.main()
