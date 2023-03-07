class Curve():
    """
    Defines a curve that goes from R to R^M 

    -----Attributes-----
    begin_point : 
    end_point : 
    curve_dim : 
    """
    def __init__(self, domain_interval:list, curve_func:list) -> None:
        """Init a curve with a domain interval and a parametrization of the curve for this domain"""
        
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
        domain = min(i for i in list(self.breaks) if i >= point) # Finds the first point of the domain interval in which the point lies

        return self.breaks[domain]          # Returns the curve_func value at that point.

    def _evaluate(self, point:float, curve_func) -> list:
        """Non-public utility function to find the value of the curve at a point"""
        value = [func(point) for func in curve_func]
        return value

    def value(self, point:float) -> list:
        """Public function to find the value of the curve at a point"""

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

        self.breaks.update(second_curve.breaks)
        self.end_point = second_curve.end_point

        return self      

def scalar_integrate(curve : Curve, func, num : int) -> int:
    pass

def vector_integrate(curve: Curve, func, num: int) -> int:
    pass

def curve_length(curve: Curve, num:int) -> int:
    pass

def curve_derivative(curve: Curve, num:int) -> list: #is it a list?
    pass





