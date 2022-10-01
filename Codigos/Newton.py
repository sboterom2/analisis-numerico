#Newton
import sympy as sp
from math import *
 
def MetodoDeNewton(xi,tolerancia,n):
  x=sp.symbols("x")
  funcion = input("Insertar Funcion")
  derivada_de_f=sp.diff(funcion)
  funcion = sp.lambdify(x,funcion)
  derivada_de_f = sp.lambdify(x, derivada_de_f)
  for k in range(n):
    x1 = xi-funcion/derivada_de_f(xi)
    if (abs(x1-xi)<tolerancia):
      print ("x", k+1, "=", x1, end = " ")
      print("Buena aproximacion de raiz")
      return
      xi = x1
      print("x", k+1, "=", x1)