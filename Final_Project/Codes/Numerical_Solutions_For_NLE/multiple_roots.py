import sympy as sp

x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def multiple_roots(eq,x0,tol,it):
    global x
    eq=function(eq)
    d1 = sp.diff(eq,x)
    d2 = sp.diff(d1,x)

    c=0
    e=tol+1
    

    while(c < it and e > tol and ((pow(d1.evalf(subs={x:x0}), 2)-(eq.evalf(subs={x:x0})*d2.evalf(subs={x:x0})))!=0)):
        c=c+1
        t=x0-((eq.evalf(subs={x:x0})*d1.evalf(subs={x:x0}))/(pow(d1.evalf(subs={x:x0}),2)-(eq.evalf(subs={x:x0})*d2.evalf(subs={x:x0}))))
        e=abs(x0-t)
        x0=t
    print('The solution is'+str(x0)+', with an error of '+str(e))
    
    


fun = input("Ingresa la funcion: ")
x0 = float(input("Ingresa X0: "))
tol = float(input("Ingresa la tolerancia: "))
ite = float(input("Ingresa las iteraciones: "))

multiple_roots(fun,x0,tol,ite)
