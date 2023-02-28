class Curve():
    """
    Defines a curve that goes from R to R^M 
    """
    def __init__(self, domain_interval:list, curve_func:list) -> None:
        """Inits Curve with a domain interval and a parametrization of the curve"""
        
        #Some error handling
        if not len(domain_interval) == 2:
            raise Exception('Domain interval can only consist of two points')
        for param in curve_func:
            if not callable(param):
                raise Exception('Parametrization of curve must be callable')

        #Defining variables in class-scope
        self.begin_point = domain_interval[0]
        self.end_point = domain_interval[1]
        self.curve_dimensions = len(curve_func)     #The dimension of the vector space of the line

        return None
    
    def __add__(self, second_curve: Curve):
        """Overloads the addition operator to add curves together"""
        pass





