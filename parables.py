import sympy
import numpy as np
import matplotlib.pyplot as plt


def integrate_parables(f,a1,b1,n):
  fcopy=f
    #"Calcola l'integrale definito di f sull'intervallo [a, b] usando il metodo delle parabole"
  a1 = float(a1)
  b1 = float(b1)
  n = int(n)
  
  width = (b1 - a1) / n
  a = sympy.Symbol('a')
  b = sympy.Symbol('b')
  c = sympy.Symbol('c')
  x= sympy.Symbol('x')
  xcopy=x
  
  
  integral = 0
  add_factor=0
  for i in range(0,n,2):
    punto_sinistra_x=float(a1+i*width)
    add_factor += 1
    punto_centro_x=float(a1+float(i*width+width))
    add_factor += 1
    punto_destra_x=float(a1+float(i*width+width+width))

    punto_sinistra_y=f.subs({x: punto_sinistra_x}).evalf()
    punto_centro_y=f.subs({x: punto_centro_x}).evalf()
    punto_destra_y=f.subs({x: punto_destra_x}).evalf()

    #trovati i punti sinistra destra e centro
    #necessario trovare parabola passante
    funzione_punto_a=sympy.Eq(y-b*x-c,a*x**2)
    funzione_punto_b=sympy.Eq(y-(a*(x**2))-c,b*x)
    funzione_punto_c=sympy.Eq(y-(a*(x**2))-b*x,c)
    #funzione_punto_a=sympy.sympify("(y-b*x-c)/(x**2)")#(funzione di a)
    #print("funzione_punto_a")
    #print(funzione_punto_a)
    #funzione_punto_b=sympy.sympify("(y-(a*(x**2))-c)/x")#(funzione di b)
    #print("funzione_punto_b")
    #print(funzione_punto_b)
    #funzione_punto_c=sympy.sympify("y-(a*(x**2))-b*x")#(funzione di c)
    #print("funzione_punto_c")
    #print(funzione_punto_c)


    funzione_punto_a=funzione_punto_a.subs({x:punto_sinistra_x}).evalf()
    funzione_punto_a=funzione_punto_a.subs({y:punto_sinistra_y}).evalf()
    #print(funzione_punto_a)

    funzione_punto_b=funzione_punto_b.subs({x:punto_centro_x}).evalf()
    funzione_punto_b=funzione_punto_b.subs({y:punto_centro_y}).evalf()
    #print(funzione_punto_b)

    funzione_punto_c=funzione_punto_c.subs({x:punto_destra_x}).evalf()
    funzione_punto_c=funzione_punto_c.subs({y:punto_destra_y}).evalf()
    #print(funzione_punto_c)

    #funzione_punto_a=funzione_punto_a.subs({b:funzione_punto_b}).evalf()
    sol=sympy.solve((funzione_punto_a,funzione_punto_b,funzione_punto_c),(a,b,c))
    #print("sadssaddsadasd")
    #print(sol)
    funzione_parabola=sympy.sympify(f"{sol[a]}*x**(2)+{sol[b]}*x+{sol[c]}")
    print(funzione_parabola)
    draw_parable(funzione_parabola,float(punto_sinistra_x),float(punto_destra_x),True)

    F=sympy.integrate(funzione_parabola,x)
    integral=integral+F.subs(x,punto_destra_x)-F.subs(x,punto_sinistra_x)


    



    add_factor=0
    f=fcopy
    x=xcopy
  draw_function(expr , a1, b1)
  return integral
def draw_parable(func,EST_sinistro,EST_destro,color_check):
  x='x'
  y_func = sympy.lambdify(x, func, 'numpy')
  x = np.arange(float(EST_sinistro)-0.1,float(EST_destro)+0.1, 0.01)

  # Evaluate the function at the x values
  y = y_func(x)
  plt.plot([EST_sinistro,EST_sinistro],[0,y_func(EST_sinistro)],'yellow')
  plt.plot([EST_destro,EST_destro],[0,y_func(EST_destro)],'yellow')
  plt.plot(x, y,'red')

def draw_function(f,a,b):
  x='x'
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

  
print("Metodo delle parabole:")
expr1 = input('Inserisci la funzione da integrare: ')

# Convert the expression to a SymPy expression
x = sympy.Symbol('x')
y = sympy.Symbol('y')

expr = sympy.sympify(expr1)

print("Funzione inserita: ")
print(expr)
expr_copy=expr
a = input("Inserisci il limite inferiore dell'intervallo di integrazione: ")
b = input("Inserisci il limite superiore dell'intervallo di integrazione: ")
n = input("Inserisci il numero di rettangoli: ")

result = integrate_parables(expr_copy,a,b,n)
print(f"Il risultato dell'integrale è: {result}")

