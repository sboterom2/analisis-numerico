import sympy as sp
import numpy as np

x=sp.symbols('x')

def function(func):
    global x
    return sp.sympify(func)

def Regla_falsa(eq,a,b,tol):
    global x
    eq=function(eq)
    length = abs(b-a)
    fa = eq.evalf(subs={x:a})
    fb = eq.evalf(subs={x:b})
    while not(length<=tol):
        c = b - fb*(a-b)/(fa-fb)
        fc = eq.evalf(subs={x:c})
        r = np.sign(fa)*np.sign(fc)
        
        if r>0:
            length = abs(c-a)
            a = c
            fa = fc
        else:
            length = abs(b-c)
            b = c
            fb = fc
    print(c)
    print(fa)


    


Regla_falsa('x**3+x**2+2*x+1',-1,0,0.01)


