import unittest
import vectorcalc as vc

class TestCurveValues(unittest.TestCase):
    def runTest(self):
      curve = vc.Curve([0, 1], [lambda x: 1, lambda x: x])

      #Tests that the domain is set correctly
      self.assertEqual(curve.begin_point, 0, "incorrect beginning point")
      self.assertEqual(curve.end_point, 1, "incorrect end point")

      #Tests that the curve evaluates the paramaterization correctly
      self.assertEqual(curve.dim, 2, 'incorrect dimension')
      self.assertEqual(curve.value(1), [1,1], 'incorrect evaluation')

      #Tests curve addition
      second_curve = vc.Curve([1, 3], [lambda x: 1, lambda x: 2*x - 1])
      curve += second_curve

      self.assertEqual(curve.end_point, 3, 'incorrect endpoint')
      self.assertEqual(curve.value(1), [1, 1], 'incorrect boundary point')
      self.assertEqual(curve.value(3), [1, 5], 'incorrect curve extension')

      curve = vc.Curve([0, 1], [lambda x: 3*x -2, lambda x: 3*x-1 ])
      self.assertEqual(round(vc.scalar_integrate(curve, lambda x, y: 4*x**3, neval = 10000), 2), -21.21, 'incorrect scalar integral')


if __name__ == "__main__":
    unittest.main()
