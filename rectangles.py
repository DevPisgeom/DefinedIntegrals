import sympy
import numpy as np
import matplotlib.pyplot as plt




def integrate_rectangles(f, a, b, n):
  """Calcola l'integrale definito di f sull'intervallo [a, b] usando il metodo dei rettangoli.
  
  Args:
    f: La funzione da integrare (una funzione di una sola variabile)
    a: Il limite inferiore dell'intervallo di integrazione
    b: Il limite superiore dell'intervallo di integrazione
    n: Il numero di rettangoli da utilizzare
  
  Returns:
    L'approssimazione dell'integrale definito di f sull'intervallo [a, b]
  """
  a = float(a)
  b = float(b)
  n = int(n)
  # Calcola la larghezza di ogni rettangolo
  width = (b - a) / n
  
  # Calcola l'approssimazione dell'integrale come somma delle aree dei rettangoli
  integral = 0
  for i in range(n):
    # Calcola l'ascissa del vertice sinistro del rettangolo i-esimo
    if(i==0 or i==n-1):
        color=True
    else:
        color=False
    x_i = a + (i * width) #SINISTRA
    #x_i+width DESTRA
    
    # Calcola l'altezza del rettangolo i-esimo
    y_i = f.subs({x: x_i + 0.5*width}).evalf() #ALTEZZA
    draw_rectangle(float(x_i) , float(x_i+width) , float(y_i), color )
    EST_sinistro=float(x_i)
    EST_destro=float(x_i+width)
    altezza=float(y_i)
    area_rettangolo=float(width * altezza)
    print(f"Rettangolo Numero: {i}, Estremo Sinistro: {EST_sinistro}, Estremo Destro: {EST_destro}, Area : {area_rettangolo}")
    # Aggiunge l'area del rettangolo i-esimo all'approssimazione dell'integrale
    integral += area_rettangolo
  
  return integral
def draw_rectangle(sinistra,destra,altezza,color_check):
    #per disegnare un rettangolo devo fare 3 rette
    #la prima con x=sinistra alta fino altezza
    #la seconda con x=destra alta fino altezza
    #la terza che va da x=sinista y=f(sinistra) a x=destra y=f(destra)

    if(color_check):
      plt.plot([sinistra,sinistra],[0,altezza],'red')
      plt.plot([destra,destra],[0,altezza],'red')
      plt.plot([sinistra,destra],[altezza,altezza],'blue')
    else:
      #plt.plot([sinistra,sinistra],[0,altezza],'yellow')
      plt.plot([destra,destra],[0,altezza],'yellow')
      plt.plot([sinistra,destra],[altezza,altezza],'blue')
    #plt.show()

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
print("Metodo dei rettangoli:")
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

result = integrate_rectangles(expr_copy,a,b,n)
print(f"Il risultato dell'integrale è: {result}")
draw_function(expr , a, b)


