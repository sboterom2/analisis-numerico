#busquedas incrementales
def fx(x):
    y=(x**3)+2
    return y
def busquedas(x0,dx,ite):
    b=x0+dx
    cont=1
    while(fx(x0)*fx(b)>0 and cont< ite):
        x0=b
        b=x0+dx
        cont=cont + 1
    if fx(x0)*fx(b)<0:     
         print('raiz entre ' + str(x0) + ' y ' + str(b))
    else:
        print('er seba e gay')
    
    
busquedas(-2, 0.5, 10)