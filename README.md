
# Vectorcalc

A simple package to perform elementary operations in vector calculus.

## Current Features (W.I.P)

 - Numerical line integrals
	 - Vector and scalar numerical line integrals


## Usage Examples
Examples of working with curves in vectorcalc
 1.  Creating a curve
 
 The first step in any operation is creating the curve.
 
    import vectorcalc as vc
    curve = vc.Curve([0, 1], [lambda t: 1, lambda t: t**2])

This creates a curve in R^2 with domain of [0, 1] and parametrization (1, t^2). Nota bene, the parametrization of the curve must be a list with **callable** elements.

2. Scalar Integral

 Suppose we would like to integrate a scalar-valued function over this curve. This could be done as follows:

    integral = vc.scalar_integrate(curve, lambda x, y: x + y, neval = 1000)
Here, we integrate the scalar function x + y over the curve. It should be noted that the lambda function has two parameters. **The number of accepted parameters should match the dimension of the curve.**


## Installation
To install run command:
> pip install vectorcalc
