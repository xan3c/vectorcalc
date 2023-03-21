import math
import warnings

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
        
        # Some error handling
        if not second_curve.begin_point == self.end_point:
            raise Exception('Domain of second curve does not begin at the end of the first curve.')
        if not second_curve.value(second_curve.begin_point) == self.value(self.end_point):
            raise Exception('Curves must join at endpoints')

        # Updates the curve with its new properties
        self.breaks.update(second_curve.breaks)
        self.end_point = second_curve.end_point

        return self      

def truncate(f, n):
    """Utility function to truncate float (f) to n digits"""
    return math.floor(f * 10 ** n) / 10 ** n

def domain_truncate(point_one: float, point_two: float, trunc: int) -> "two floats":
    """"
    Utility function to truncate two points.
    Used for integration and length calculations to handle irrational curve boundaries

    -----Parameters-----
    point_one : float
    point_two : float
    trunc : int
        The number of digits to truncate each point

    -----Returns-----
    a, b : float, float
        Returns the two truncated points
    """
    a, b = truncate(point_one, trunc), truncate(point_two, trunc)
    truncation_error = []
    if a != 0:
        truncation_error.append(abs(a - point_one) / a)
    if b!= 0:
        truncation_error.append(abs(b - point_two) / b)
    for i in truncation_error:
        if i > 0.01:
            warnings.warn("The relative error of truncating the curve bounds is more than 1%. Consider increasing truncation")

    return a, b

def scalar_integrate(curve : Curve, func, neval=100, trunc=10) -> float:
    """
    Finds a numerical integral of a scalar function over a curve via. midpoint method

    -----Parameters-----
    curve : vectorcalc.Curve
        The curve used in the curve integral

    func : callable
        The scalar function integrated over this curve. func must have as many parameters as the dimension of the curve
        e.g. if the curve lies in R^3, then func must take 3 arguments

    neval : int
        The number of evaluations done. i.e. the size of the partition of the curve.

    trunc : int
        The number of digits to truncate the curve's bounds. This is needed to handle irrational numbers.

    -----Returns-----
    result : float
        The value of the integral

    -----TODO-----
        Implement and return error estimation 
    """

    # Truncates curve boundaries to handle irrational boundaries
    a, b = domain_truncate(curve.begin_point, curve.end_point, trunc)
    
    # Calculates the step_size
    domain_range = b - a
    step_size = domain_range/neval

    # Begins calculation of the integral
    result = 0
    for i in range(neval):
        # Finds length between the two curve points
        distance = math.dist(curve.value(a + (i+1)*step_size), curve.value(a + i*step_size))    
        # Finds the evaluation point: the point that lies in the middle of the two curve points
        eval_point = curve.value(a + step_size/2 + i * step_size)
        # Multiplies the length of the curve with the function evaluated at the evaluation point and adds it to the result
        result += func(*eval_point) * distance 
    return result

def vector_integrate(curve: Curve, func : list, neval=100, trunc=10) -> float:
    """
    Finds a numerical integral of a vector-valued function over a curve via. midpoint method

    -----Parameters-----
    curve : vectorcalc.Curve
        The curve used in the curve integral

    func : list
        The vector-valued function integrated over this curve. There must be as many elements in the list 
        as there are dimensions of the curve. Each element in the list represents a callable function,
        with each function also having as many parameters as the dimension of the curve. 
        e.g. if the curve lies in R^3, then a valid argument is [f, g, h] where each of f, g, and h
        are callable and take three arguments.

    neval : int
        The number of evaluations done. i.e. the size of the partition of the curve.

    trunc : int
        The number of digits to truncate the curve's bounds. This is needed to handle irrational numbers.

    -----Returns-----
    result : float
        The value of the integral

    -----TODO-----
        Implement and return error estimation 
    """

    # Tests that the vector function is in the same space as the curve, so that the dot product is well-defined
    if not curve.dim == len(func):
        raise Exception('Vector-valued function must be in the same space as the curve.')

    # Truncates the boundary points to deal with irrational numbers. 
    a, b = domain_truncate(curve.begin_point, curve.end_point, trunc)

    # Sets up domain of integral and the step size
    domain_range = b - a
    step_size = domain_range/neval

    # Performing the integral
    result = 0
    for i in range(neval):
        # Finds the evaluation point: the point that lies in the middle of two curve points
        eval_point = curve.value(a + step_size / 2 + i * step_size)
        # Evaluates the function at this evaluation point
        func_eval = [i(*eval_point) for i in func]
        # Finds the two curve points (i.e. the bounds where the evaluation point lies in the middle)
        begin_bound = curve.value(a + i*step_size)
        end_bound = curve.value(a + (i+1)*step_size)

        # In each component multiplies the distance between the bound points and the evaluated point
        for j, k, l in zip(func_eval, begin_bound, end_bound):
            result += j * math.sqrt((l-k)**2)

    return result

def curve_length(curve: Curve, neval=100, trunc=10) -> float:
    """
    Returns a numerical estimate of the curve length

     -----Parameters-----
    curve : vectorcalc.Curve
        The curve to estimate the length of

    neval : int
        The number of evaluations done. i.e. the size of the partition of the curve.

    trunc : int
        The number of digits to truncate the curve's bounds. This is needed to handle irrational numbers.

    -----Returns-----
    
    length : float
        The numerically estimated length of the curve
    """

    # Truncates the boundaries to handle irrational numbers
    a, b = domain_truncate(curve.begin_point, curve.end_point, trunc)

    # Integrates the constant function "1" over the curve
    length = scalar_integrate(curve, lambda x: 1, neval = neval, trunc = trunc)

    return length
