from tkinter import *
import threading
import os
import webbrowser
import tkinter as tk

root = tk.Tk()

root.title("Numerical Methods Calculator") 
root.geometry("800x600")
root_key = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

"""
Extract path from every Method
"""

# Numerical non-linear equations

def binc():
    os.system('start cmd /K python ./Numerical_Solutions_For_NLE/incremental_search.py')

def bisec():
    os.system('start cmd /K python ./Numerical_Solutions_For_NLE/bisection.py')

def rfalse():
    os.system('start cmd /K python ./Numerical_Solutions_For_NLE/false_rule.py')

def fpoint():
    os.system('start cmd /K python ./Numerical_Solutions_For_NLE/.fixed_point.py')

def newton():
    os.system('start cmd /K python ./Numerical_Solutions_For_NLE/newton.py')

def sec():
    os.system('start cmd /K python ./Numerical_Solutions_For_NLE/secant.py')

def rmul():
    os.system('start cmd /K python ./Numerical_Solutions_For_NLE/multiple_roots.py')
    
# Systems of linear equations

def cholesky():
    os.system('start cmd /K python ./Solutions_For_Systems_Of_LE/cholesky.py')

def crout():
    os.system('start cmd /K python ./Solutions_For_Systems_Of_LE/crout.py')

def doolittle():
    os.system('start cmd /K python ./Solutions_For_Systems_Of_LE/doolittle.py')

def gseidel():
    os.system('start cmd /K python ./Solutions_For_Systems_Of_LE/gauss_seidel.py')

def gauss():
    os.system('start cmd /K python ./Solutions_For_Systems_Of_LE/gauss.py')

def jacobi():
    os.system('start cmd /K python ./Solutions_For_Systems_Of_LE/jacobi.py')

def lu():
    os.system('start cmd /K python ./Solutions_For_Systems_Of_LE/lu.py')
    
# Interpolation

def difdiv():
    os.system('start cmd /K python ./Interpolation/divided_differences.py')

def inter():
    os.system('start cmd /K python ./Interpolation/interpolation.py')

def lagrange():
    os.system('start cmd /K python ./Interpolation/lagrange.py')

def spline1():
    os.system('start cmd /K python ./Interpolation/splines_g1.py')

def spline2():
    os.system('start cmd /K python ./Interpolation/splines_g2.py')

def vander():
    os.system('start cmd /K python ./Interpolation/vandermonde.py')



def action(x):
    return x

"""
Interface
"""


# Numerical non-linear equations

text = Label(root,text="Numerical Non-linear Equations",font=("Orbitron",10))
text.place(x=30, y=10)


Binc = tk.Button(root, text="Incremental Search",command=binc)
Binc.place(x=50, y=50)

Bisec = tk.Button(root, text="Bisection",command=bisec)
Bisec.place(x=50, y=100)

Rfalse = tk.Button(root, text="False Rule",command=rfalse)
Rfalse.place(x=50, y=150)

Fpoint = tk.Button(root, text="Fixed Point",command=fpoint)
Fpoint.place(x=50, y=200)

Newton = tk.Button(root, text="Newton",command=newton)
Newton.place(x=50, y=250)

Sec = tk.Button(root, text="Secant",command=sec)
Sec.place(x=50, y=300)

Rmul = tk.Button(root, text="Multiple Roots",command=rmul)
Rmul.place(x=50, y=350)


# Systems of linear equations

text = Label(root,text="Systems of Linear Equations",font=("Orbitron",10))
text.place(x=300, y=10)

Gauss = tk.Button(root, text="Gauss",command=gauss)
Gauss.place(x=320, y=50)

Lu = tk.Button(root, text="LU Factorization",command=lu)
Lu.place(x=320, y=100)

Doolitle = tk.Button(root, text="Doolitle",command=doolittle)
Doolitle.place(x=320, y=150)

Crout = tk.Button(root, text="Crount",command=crout)
Crout.place(x=320, y=200)

Cholesky = tk.Button(root, text="Cholesky",command=cholesky)
Cholesky.place(x=320, y=250)

Jacobi = tk.Button(root, text="Jacobi",command=jacobi)
Jacobi.place(x=320, y=300)

Gseidel = tk.Button(root, text="Gauss - Seidel",command=gseidel)
Gseidel.place(x=320, y=350)

# Interpolation

text = Label(root,text="Interpolation",font=("Orbitron",10))
text.place(x=550, y=10)

Vmonde = tk.Button(root, text="Vandermonde",command=vander)
Vmonde.place(x=560, y=50)

Ddiv = tk.Button(root, text="Divided Difference",command=difdiv)
Ddiv.place(x=560, y=100)

Lagrange = tk.Button(root, text="Lagrange",command=lagrange)
Lagrange.place(x=560, y=150)

Spline1 = tk.Button(root, text="Splines G1",command=spline1)
Spline1.place(x=560, y=200)

Spline2 = tk.Button(root, text="Splines G2",command=spline2)
Spline2.place(x=560, y=250)

Interpolacion = tk.Button(root, text="Interpolation",command=inter)
Interpolacion.place(x=560, y=300)

root.mainloop()
