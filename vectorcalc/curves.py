class Curve():
    """
    Defines a curve that goes from R to R^M 

    -----Attributes-----
    begin_point : 
    end_point : 
    curve_dim : 
    """
    def __init__(self, domain_interval:list, curve_func:list) -> None:
        """Inits Curve with a domain interval and a parametrization of the curve"""
        
        #Some error handling
        if not len(domain_interval) == 2:
            raise Exception('Domain interval can only consist of two points')
        for param in curve_func:
            if not callable(param) or type(param) != int or type(param) != float:
                raise Exception('Parametrization of curve must be callable or a constant number')

        #Defining variables in class-scope
        self.begin_point = domain_interval[0]
        self.end_point = domain_interval[1]
        self.curve_dim = len(curve_func)     #The dimension of the vector space of the curve

        return None

    def _curve_func():
        pass

    def dimension(self) -> int:
        """Returns the dimension of the curve."""
        return self.curve_dim

    def _evaluate(self, point:float, curve_func) -> list:
        """Non-public utility function to find the value of the curve_func at a point"""
        value = [func(point) for func in curve_func]
        return value
    
    def __add__(self, second_curve):
        """Overloads the addition operator to add curves together"""
        pass

    def curve_value(self, point:float) -> list:
        """Public function to find the value of the curve at a point"""

        if point < self.begin_point or point > self.end_point:
            raise Exception('Point is outside domain of curve')

        #TODO implement test for two curves



        


        

        #Which curve_func is used on the interval?
        #Within the domain?
        pass

    def __getitem__(self, key):
        #return self.curve_func[key] ?
        pass

def scalar_integrate(curve : Curve, func, num : int) -> int:
    pass

def vector_integrate(curve: Curve, func, num: int) -> int:
    pass

def curve_length(curve: Curve, num:int) -> int:
    pass

def curve_derivative(curve: Curve, num:int) -> list: #is it a list?
    pass





