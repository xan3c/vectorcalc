import unittest
import vectorcalc as vc

class TestCurveValues(unittest.TestCase):
    def runTest(self):
      curve = vc.Curve([0, 1], [lambda x: 1, lambda x: x])

      # Tests that the domain is set correctly
      self.assertEqual(curve.begin_point, 0, "incorrect beginning point")
      self.assertEqual(curve.end_point, 1, "incorrect end point")

      # Tests that the curve evaluates the paramaterization correctly
      self.assertEqual(curve.dim, 2, 'incorrect dimension')
      self.assertEqual(curve.value(1), [1,1], 'incorrect evaluation')

      # Tests curve addition
      second_curve = vc.Curve([1, 3], [lambda x: 1, lambda x: 2*x - 1])
      curve += second_curve

      # Tests curve addition applied correctly
      self.assertEqual(curve.end_point, 3, 'incorrect endpoint')
      self.assertEqual(curve.value(1), [1, 1], 'incorrect boundary point')
      self.assertEqual(curve.value(3), [1, 5], 'incorrect curve extension')


class TestCurveFuncs(unittest.TestCase):
    def runTest(self):
        # Tests a known scalar integral to 3 decimal places
        # See Paul's Online Notes - Line Integrals - Part I Example 3 for analytic solution
        # https://tutorial.math.lamar.edu/Classes/CalcIII/LineIntegralsPtI.aspx 
        curve = vc.Curve([0, 1], [lambda x: 3*x -2, lambda x: 3*x-1 ])
        self.assertEqual(round(vc.scalar_integrate(curve, lambda x, y: 4*x**3, neval = 1000), 3), -21.213, 'incorrect scalar integral')

        # Tests a known vector function integral to 3 decimal places
        # See Paul's Online Notes - Line Integrals Of Vector Fields Example 1 for analytic solution
        # https://tutorial.math.lamar.edu/Classes/CalcIII/LineIntegralsVectorFields.aspx
        curve = vc.Curve([0, 1], [lambda x: x, lambda x: x**2, lambda x: x**3])
        self.assertEqual(round(vc.vector_integrate(curve, [lambda x, y, z : 8*x**2*y*z, lambda x, y, z : 5*z, lambda x, y, z : -4*x*y]), 3), 1.000, 'incorrect vector integral')

        # Tests curve_length() of a curve with known length to 3 decimal places
        curve = vc.Curve([])

if __name__ == "__main__":
    unittest.main()
