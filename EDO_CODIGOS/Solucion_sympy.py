# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 13:45:14 2025

@author: gijug
"""

import sympy as sp

def resolver_ecuacion():
    x = sp.Symbol("x")
    y = sp.Function("y")
    edo = sp.Eq(15*y(x) + 3*y(x).diff(x), 6*x*y(x)**2)
    
    print("Ecuación diferencial:")
    sp.pprint(edo)

    # Solución general
    sol_general = sp.dsolve(edo, y(x))
    print("\nSolución general:")
    sp.pprint(sol_general)

    # Solucion particular
    condicion_inicial = {y(0): 2}
    sol_particular = sp.dsolve(edo, y(x), ics=condicion_inicial)
    print("\nSolución particular con y(0)=2:")
    sp.pprint(sol_particular)


if __name__ == "__main__":
    resolver_ecuacion()