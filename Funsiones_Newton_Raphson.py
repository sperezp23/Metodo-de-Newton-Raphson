# Funsiones Newton Raphson

# %% Librerías
import math

# %% Funciones a evaluar

#f(x)
def f(p):
    f = math.exp(-p)-math.sin(p)
    return f
#f'(x)
def g(p):
    g = -math.exp(-p)-math.cos(p)
    return g

# %% Errores
def Errores(tipErr,p,z):
    if tipErr == 1:
        E = abs(p-z)
    elif tipErr == 2:
        E = abs((p-z)/(p))
    elif tipErr == 3:
        E = abs((p-z)/(p))*100.0
    return E