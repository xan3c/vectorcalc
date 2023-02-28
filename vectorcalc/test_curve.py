import unittest
import curves

class TestCurveValues(unittest.TestCase):
    def runTest(self):
      curve = curves.Curve([0, 1], [lambda x: x, lambda x: x])

      #Tests that the domain is set correctly
      self.assertEqual(curve.begin_point, 0, "incorrect beginning point")
      self.assertEqual(curve.end_point, 1, "incorrect end point")

      #Tests that the curve evaluates the paramaterization correctly




unittest.main()
