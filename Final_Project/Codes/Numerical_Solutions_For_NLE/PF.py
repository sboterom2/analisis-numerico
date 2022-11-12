import sympy as sp
x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def PF(eq,x_0,tol):
    global x
    eq=function(eq)+x 
    e=100
    x_r=x_0 
    iteracion=0 
    while e>tol:
        x_prev=x_r
        x_r=eq.evalf(subs={x:x_prev})
        iteracion+=1
        if x_r !=0:
            e=abs((x_r-x_prev)/x_r)*100
    print(x_r)
    print(e)
    


