# Metodo de Newton Raphson

# %% Reset
from IPython import get_ipython
get_ipython().magic('reset -sf')

# %% Funciones
import Funsiones_Newton_Raphson as f

# %% Entradas
print("\nMetodo de Newton Raphson\n")
Po = float(input("Ingrese el valor de la primera aproximacion(Po)\n"))
TOL = float(input("Ingrese el valor de la tolerancia(TOL)\n"))

if TOL != 0.0:
    tipErr = int(input("Escoja el tipo de error, 1:E_abs, 2:E_rel,3:E_%\n"))
else:
    print("\nTipo de error: porcencual")
    
No = int(input("Ingrese el numero maximo de interaciones(No)\n"))
guardar = input("¿Quiere guardar el resultado? y/n\n")

# %% Declaracion de variables
i = 1
E = 100.0
alfa = 1.0
epsilon = 6.123233995736766e-17
AproxIni = Po

# %% Cosideraciones iniciales
if TOL == 0.0:
    TOL = epsilon
    tipErr = 3

if tipErr < 1.0 or tipErr > 3.0:
    tipErr = 2

#Tipo de error(Mensaje)    
if tipErr == 1:
    Err = "_abs"
elif tipErr == 2:
    Err = "_rel"
elif tipErr == 3:
    Err = "_%"
    
# %% Metodo de Newton Raphson
while E> epsilon and i<=No:
    p = Po - (f.f(Po)/f.g(Po))
    
    if p != 0.0:
        E = f.Errores(tipErr,p,Po)
        
    delta = (p-Po)/2.0 
    alfa = abs(E/alfa)
    
    #Impresión y almacenamiento de resultados
    if abs(p-Po) < TOL:
        print("-------------------------------------------------------------")
        print("Proceso exitoso")
        print("Po =",AproxIni)
        print("p =",p)
        print("f(p) =",f.f(p))
        print("Error"+Err+" =",E)
        print("Alfa =",alfa)
        print("Delta =",delta)
        print("TOL =",TOL)
        print("No =",i)
        print("-------------------------------------------------------------")
        
        #Archivo de texto con los datos
        if guardar == "y":        
            resultado_NewtonRaphson = open("resultado_NewtonRaphson.txt","a")
            resultado_NewtonRaphson.write("Po = "+str(AproxIni)+"\n")
            resultado_NewtonRaphson.write("p = "+str(p)+"\n")
            resultado_NewtonRaphson.write("Error"+Err+" = "+str(E)+"\n")
            resultado_NewtonRaphson.write("Alfa = "+str(alfa)+"\n")
            resultado_NewtonRaphson.write("Delta = "+str(delta)+"\n")
            resultado_NewtonRaphson.write("TOL = "+str(TOL)+"\n")
            resultado_NewtonRaphson.write("No = "+str(i)+"\n")
            resultado_NewtonRaphson.write("-------------------------------------------------------------\n")
            resultado_NewtonRaphson.close()
        break
    
    i += 1
    Po = p
    alfa = E
    
if i > No:
    print("\nEl metodo ha fallado luego de la interación No =", i+1)        