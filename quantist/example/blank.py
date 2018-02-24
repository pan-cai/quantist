from sympy import *
x = Symbol('x')
print(diff(sin(x),x))
print(diff(x**2,x))
print(diff(3*x**2+x,x))
print(diff((1/(1+x**2)),x))


