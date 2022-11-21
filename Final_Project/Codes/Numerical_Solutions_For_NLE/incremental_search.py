import sympy as sp


x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def Incremental_Search(eq, a, b, deltaX):
    global x
    eq=funcion(ecuacion)

    while(a<b):
        xi = a + deltaX
        fun_a = eq.evalf(subs={x:a})
        
        fun_xi = eq.evalf(subs={x:xi})
        if (fun_a *fun_xi )<0:    
            
            print(a)
            print(xi)
            
        else:
            a=xi
  

  
res = Incremental_Search('sin(x)',-7,7,0.3)



