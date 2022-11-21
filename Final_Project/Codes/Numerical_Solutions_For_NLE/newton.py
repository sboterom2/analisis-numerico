import sympy as sp


x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def Newton(eq,x_0,es,maxIte):
    global x
    eq=function(eq)
    d=sp.diff(eq)
    f_NR=x-(eq/d)
    ea=100 
    x_r=x_0
    inter=0
    while ea>es:
        x_prev=x_r
        x_r=f_NR.evalf(subs={x:x_prev})
        if x_r !=0:
            ea=abs((x_r-x_prev)/x_r)*100
        inter+=1
        
        if inter>=maxIte:
            print("The method does not converge")
            break
    
