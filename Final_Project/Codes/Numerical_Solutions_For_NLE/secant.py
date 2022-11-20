import sympy as sp


x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def secante(fx,a,b,tol,it):
    global x
    fx=function(fx)
    e=tol+1
    xi=a
    x0=b
    c=0
   
    while (e>tol and c<it and (fx.evalf(subs={x:x0})-fx.evalf(subs={x:xi}))!=0):
        c=c+1
        x2=x0-((fx.evalf(subs={x:x0})*(x0-xi))/(fx.evalf(subs={x:x0})-fx.evalf(subs={x:xi})))
        e=abs(xi-x0)
        x0=xi
        xi=x2
    print(xi)
    print(e)
            
    



res=secante('x**3+x**2+2*x+1',-1,0,0.001,100)


