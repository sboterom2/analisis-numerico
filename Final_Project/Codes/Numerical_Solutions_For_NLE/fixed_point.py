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
            e=abs(x_r-x_prev)
    print('The solution is in '+ str(x_r)+', with an eror of '+str(e))
    
    
    
fun = input("Put the Function: ")
x0 = float(input("Put X0: "))
e = float(input("Put tolerancie: "))
PF(fun,x0,e)


