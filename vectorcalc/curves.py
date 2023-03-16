import math

class Curve():
    """
    Defines a curve that goes from R to R^M 

    ...

    -----Attributes-----
    begin_point : float
        the beginning point of the curve's domain (inclusive)
    end_point : float
        the end point of the curve's domain (inclusive)
    dim : int
        the dimension of the space in which the curve lies (i.e. R^N)

    -----Methods-----
    value : float
        the value of the curve at a point in its domain

    """
    def __init__(self, domain_interval:list, curve_func:list) -> None:
        """
        Constructs a curve with a domain interval and a parametrization of the curve for this domain
        
        -----Parameters-----
        domain_interval : list 
            a list representing the domain of the curve. The domain should lie in the reals, i.e. [a, b] for a, b in R.
        curve_func : list
            a list with each element of the list being a callable function of one variable. the dimension of the curve is the length of the list
        """
        
        # Some error handling to ensure the proper inputs
        if not len(domain_interval) == 2:
            raise Exception('Domain interval can only consist of two points')
        if not domain_interval[1] >= domain_interval[0]:
            raise Exception('End point of domain must be larger than begin point')
        for param in curve_func:
            if not callable(param):
                raise Exception('Parametrization of curve must be callable')

        #Defining instance variables

        # A dictionary to store where all the breaks in the domain are at.
        # This will be useful when we add curves together, so we know when our curve_func parametrization changes
        self.breaks = {}                 
        self.breaks[domain_interval[0]] = curve_func         #The start of the domain maps to curve_func
        self.breaks[domain_interval[1]] = curve_func     

        # The domain of the curve
        self.begin_point = list(self.breaks)[0]
        self.end_point =  list(self.breaks)[-1]
        self.dim = len(curve_func)     # The dimension of the vector space of the curve

        return None

    def _curve_func(self, point:float):
        """Non-public utlity function to find which curve parameterization to use at a point. Important for when two curves have been added together."""
        domain = min(i for i in list(self.breaks) if i >= point) # Finds the first point of the domain interval in which the point lies

        return self.breaks[domain]          # Returns the curve_func value at that point.

    def _evaluate(self, point:float, curve_func) -> list:
        """Non-public utility function to find the value of the curve at a point"""
        value = [func(point) for func in curve_func]
        return value

    def value(self, point:float) -> list:
        """Public function to find the value of the curve at a point"""

        #Ensuring point is within the curve's domain
        if point < self.begin_point or point > self.end_point:
            raise Exception('Point is outside domain of curve')

        return self._evaluate(point, self._curve_func(point))

    def __add__(self, second_curve):
        """Overloads the addition operator to add curves together"""
        
        #Some error handling
        if not second_curve.begin_point == self.end_point:
            raise Exception('Domain of second curve does not begin at the end of the first curve.')
        if not second_curve.value(second_curve.begin_point) == self.value(self.end_point):
            raise Exception('Curves must join at endpoints')

        #updates the curve with its new properties
        self.breaks.update(second_curve.breaks)
        self.end_point = second_curve.end_point

        return self      

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def scalar_integrate(curve : Curve, func, neval=100, trunc=10) -> float:
    """Finds a numerical integral of a scalar function over a curve via midpoint method"""
    a, b = truncate(curve.begin_point, trunc), truncate(curve.end_point, trunc)
    domain_range = b - a
    step_size = domain_range/neval

    result = 0
    for i in range(neval):
        distance = math.dist(curve.value(a + (i+1)*step_size), curve.value(a + i*step_size))
        eval_point = curve.value(a + step_size/2 + i * step_size)
        result += func(*eval_point) * distance
    return result

def integrate(curve: Curve, func, neval=100, trunc=10) -> float:
    """integrates vector and scalar functions over a curve"""
    a, b = truncate(curve.begin_point, trunc), truncate(curve.end_point, trunc)
    domain_range = b - a
    step_size = domain_range/neval

    result = 0
    pass


def curve_length(curve: Curve, neval=100, trunc=10) -> float:
    """returns a numerical estimate of the curve length"""
    a, b = truncate(curve.begin_point, trunc), truncate(curve.end_point, trunc)
    domain_range = b - a
    step_size = domain_range/neval
    length = 0
    for i in range(neval):
        length += math.dist(curve.value(a + (i+1)*step_size), curve.value(a + i*step_size))

    return length
