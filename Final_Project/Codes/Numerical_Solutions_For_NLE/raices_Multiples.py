import sympy as sp

x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def Raices_Multiples(eq,x0,tol,it):
    global x
    eq=function(eq)
    derivada1 = sp.diff(eq,x)
    derivada2 = sp.diff(derivada1,x)

    c=0
    e=tol+1
    

    while(c < it and e > tol and ((pow(derivada1.evalf(subs={x:x0}), 2)-(eq.evalf(subs={x:x0})*derivada2.evalf(subs={x:x0})))!=0)):
        c=c+1
        t=x0-((eq.evalf(subs={x:x0})*derivada1.evalf(subs={x:x0}))/(pow(derivada1.evalf(subs={x:x0}),2)-(eq.evalf(subs={x:x0})*derivada2.evalf(subs={x:x0}))))
        e=abs(x0-t)
        x0=t
    print(x0)
    print(e)
   

