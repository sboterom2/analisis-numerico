import sympy as sp


x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def Busqueda_Incremental(ecuacion, a, b, deltaX):
    global x
    ecuacion=funcion(ecuacion)

    while(a<b):
        xi = a + deltaX
        fun_a = ecuacion.evalf(subs={x:a})
        
        fun_xi = ecuacion.evalf(subs={x:xi})
        if (fun_a *fun_xi )<0:    
            
            print(a)
            print(xi)
            
        else:
            a=xi
  

  
res = Busqueda_Incremental('sin(x)',-7,7,0.3)



