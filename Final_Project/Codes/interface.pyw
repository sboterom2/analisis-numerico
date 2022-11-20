from tkinter import *
import threading
import os
import webbrowser
import tkinter as tk

root = tk.Tk()

root.title("Numerical Methods Calculator") 
root.geometry("800x600")
root key = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

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
# Interpolation

"""
Interface
"""

# Numerical non-linear equations
# Systems of linear equations
# Interpolation

root.mainloop()
