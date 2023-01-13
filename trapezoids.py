import sympy
import numpy as np
import matplotlib.pyplot as plt

def integrate_trapezoids(f1, a, b, n):
  """Calcola l'integrale definito di f sull'intervallo [a, b] usando il metodo dei trapezi.

  Args:
  f: La funzione da integrare (una funzione di una sola variabile)
  a: Il limite inferiore dell'intervallo di integrazione
  b: Il limite superiore dell'intervallo di integrazione
  n: Il numero di trapezi da utilizzare

  Returns:
  L'approssimazione dell'integrale definito di f sull'intervallo [a, b]
  """
  a = float(a)
  b = float(b)
  n = int(n)
    # Calcola la larghezza di ogni trapezio
  width = (b - a) / n
    # Calcola l'approssimazione dell'integrale come somma delle aree dei trapezi
  integral = 0
  #x_i=0
  #x_i_destro=0
  for i in range(n):
    # Calcola l'ascissa del vertice sinistro del trapezio i-esimo
    if(i==0 or i==n-1):
        color=True
    else:
        color=False
    x_i = a + float(i * width)  # SINISTRA
    x_i_destro = x_i + width  # DESTRA
        # Calcola l'altezza del trapezio i-esimo
        #y_i = f.subs({x: x_i + 0.5*width}).evalf()
    y_i = f1.subs({x: x_i}).evalf()  # ALTEZZA SINISTRA
    y_i_destro = f1.subs({x: x_i_destro}).evalf()  # ALTEZZA DESTRA
    draw_trapezoid(float(x_i), float(x_i_destro), float(y_i), float(y_i_destro),color)
    area_trapezio = float((width * (y_i + y_i_destro)) / 2)
    # Aggiunge l'area del trapezio i-esimo all'approssimazione dell'integrale
    print(f"Trapezio Numero: {i}, Estremo Sinistro: {x_i}, Estremo Destro: {x_i_destro}, Area : {area_trapezio}")
    integral += area_trapezio
  return integral

def draw_trapezoid(sinistra, destra, altezza_sinistra, altezza_destra,color_check):
  """Disegna un trapezio con gli estremi specificati.

  Args:
      sinistra: l'ascissa del vertice sinistro del trapezio
      destra: l'ascissa del vertice destro del trapezio
  altezza_sinistra: l'altezza del vertice sinistro del trapezio
  altezza_destra: l'altezza del vertice destro del trapezio
  """
  # disegnare le due diagonali del trapezio
  plt.plot([sinistra, destra], [altezza_sinistra, altezza_destra], color='green')
  plt.plot([sinistra, destra], [0, 0], color='green')
  if(color_check):
    plt.plot([sinistra,sinistra],[0,altezza_sinistra],'red')
    plt.plot([destra,destra],[0,altezza_destra],'red')
  else:
    plt.plot([sinistra,sinistra],[0,altezza_sinistra],'yellow')
    plt.plot([destra,destra],[0,altezza_destra],'yellow')
  

def draw_function(f,a,b):
  global x
  # Convert the SymPy expression to a Python function
  y_func = sympy.lambdify(x, f, 'numpy')
  
  # Generate the x values
  x = np.arange(float(a)-float(3),float(b)+float(3), 0.01)
  
  # Evaluate the function at the x values
  y = y_func(x)

  plt.plot(x, y)
  plt.title("Funzione richiesta")
  plt.xlabel("valori di  x")
  plt.ylabel("valori di  y")
  plt.show()

# Input the expression from the user
print("Metodo dei trapezi:")
expr1 = input('Inserisci la funzione da integrare: ')

# Convert the expression to a SymPy expression
x = sympy.Symbol('x')
expr = sympy.sympify(expr1)

print("Funzione inserita: ")
print(expr)
expr_copy=expr
a = input("Inserisci il limite inferiore dell'intervallo di integrazione: ")
b = input("Inserisci il limite superiore dell'intervallo di integrazione: ")
n = input("Inserisci il numero di rettangoli: ")

result = integrate_trapezoids(expr_copy,a,b,n)
print(f"Il risultato dell'integrale è: {result}")
draw_function(expr , a, b)