#Metodo de Punto Fijo
import numpy as np 
def g(p): 
  return 0.5*pow(10.0-p*p*p, 0.5) 

def punto_fijo(p0,NO,TOL):
    i=0
    while i <= NO:
       p=g(p0)
       if np.abs(p0-p)<TOL:
          break
       print(i, "numero de iteracion", " ", p)
       i+=1
       p0=p
 
    if(i==NO+1):
      print("El metodo fallo")
    else:
      print("El metodo convergio")