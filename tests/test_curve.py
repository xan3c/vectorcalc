import unittest
import vectorcalc as vc
import math

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
      second_curve = vc.Curve([1, 3], [lambda x: 1, lambda x: 2 * x - 1])
      curve += second_curve

      # Tests curve addition applied correctly
      self.assertEqual(curve.end_point, 3, 'incorrect endpoint')
      self.assertEqual(curve.value(1), [1, 1], 'incorrect boundary point')
      self.assertEqual(curve.value(3), [1, 5], 'incorrect curve extension')


class TestCurveFuncs(unittest.TestCase):
    def runTest(self):
        # Tests a known scalar integral to 3 decimal places
        # See Paul's Online Notes - Line Integrals - Part I Example 3 for
        # analytic solution
        # https://tutorial.math.lamar.edu/Classes/CalcIII/LineIntegralsPtI.aspx
        curve = vc.Curve([0, 1], [lambda x: 3 * x - 2, lambda x: 3 * x - 1])
        integral = vc.scalar_integrate(curve, lambda x, y: 4 * x ** 3, neval = 1000)
        analytic_value = -15 * math.sqrt(2)
        decimal_place = 3
        self.assertAlmostEqual(integral, analytic_value, decimal_place, 'incorrect scalar integral')

        # Tests a known vector function integral to 3 decimal places
        # See Paul's Online Notes - Line Integrals Of Vector Fields Example 1
        # for analytic solution
        # https://tutorial.math.lamar.edu/Classes/CalcIII/LineIntegralsVectorFields.aspx
        curve = vc.Curve([0, 1], [lambda x: x, lambda x: x ** 2, lambda x: x ** 3])
        integral = vc.vector_integrate(curve, [lambda x, y, z : 8 * x ** 2 * y * z, lambda x, y, z : 5 * z, lambda x, y, z : -4 * x * y])
        analytic_value = 1.000
        decimal_place = 3
        self.assertAlmostEqual(integral, analytic_value, decimal_place, msg='incorrect vector integral')

        # Tests curve_length() of a curve with known length to 3 decimal places
        # Namely, the curve is a graph of a line and we find the arc length of
        # this graph
        # See Paul's Online Notes - Section 8.1 : Arc Length Example 2 for
        # analytic solution
        # https://tutorial.math.lamar.edu/classes/calcii/arclength.aspx
        curve = vc.Curve([1, 4], [lambda x: x, lambda x: 2 / 3 * (x - 1) ** (3 / 2)])
        length = vc.curve_length(curve, neval=1000)
        analytic_value = 14 / 3
        decimal_place = 3
        self.assertAlmostEqual(length, analytic_value, decimal_place, 'incorrect length')

        # Tests vector_integrate_square() to a known analytic value within 3
        # decimal places
        func = [lambda x, y: -y * x ** 2, lambda x, y: x * y ** 2]
        analytic_value = 224 / 3
        integral = vc.vector_integrate_square(func, [2, 2], [4, 4])
        self.assertAlmostEqual(integral, analytic_value, decimal_place, 'incorrect square integral')

if __name__ == "__main__":
    unittest.main()