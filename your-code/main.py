#1. Importa el paquete NUMPY bajo el nombre np.
import numpy as np

#2. Imprime la versión de NUMPY y la configuración.
print(f"numpy version: {np.__version__}")

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?
print("Crear array \"a\"")
a = np.random.rand(2,3,5)
# a = np.random.random((2,3,5))
# a = np.random.randn(2,3,5)

#4. Imprime a.
print(f"a:\n {a}")
print("-------------------------------")
#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"
print("Crear array \"b\"")
b = np.ones((5,2,3))

#6. Imprime b.
print(f"b:\n {b}")
print("-------------------------------")
#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?
a_size = a.size
b_size = b.size
print(f"tamaño de a: {a_size}")
print(f"tamaño de b: {b_size}")
print(f"¿a y b tienen el mismo tamaño?: {"Si" if a_size == b_size else "No"}")
print("-------------------------------")

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?
a_shape = a.shape
b_shape = b.shape
print(f"forma de a: {a_shape}")
print(f"forma de b: {b_shape}")
print(f"¿a y b tienen la misma forma?: {"Si" if a_shape == b_shape else "No"}")
print("-------------------------------")

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".
print("Crear array \"c\" transponiendo \"b\"")
c = np.transpose(b, (1,2,0))
print(f"c:\n {c}")
c_shape = c.shape
print(f"forma de c: {c_shape}")
print("-------------------------------")

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?
print("Sumar \"a\" y \"c\" para crear \"d\"")
d = a + c
print(f"d:\n {d}")
print("-------------------------------")


#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.
print("Comparar \"a\" y \"d\"")
print(f"a:\n {a}")
print(f"d:\n {d}")
print("""
La diferencia entre a y d es que d es el resultado de sumar a y c, donde c es b transpuesto.
Por lo tanto, cada valor en d es la suma de un valor en a y un valor en c. Como c es un array de unos,
cada valor en d es el valor correspondiente en a más 1.
Para comprar dichas arrays, no podemos usar "array_equal" porque son arrays de floats y los valores
pueden no ser exactamente iguales. Por lo tanto, usamos "allclose" para comparar si los valores son
cercanos dentro de una tolerancia.
""")
print(f"\"d\" - \"a\":\n {d - a}")
print(f"\"c\":\n {c}")
print(f"Es \"d\" - \"a\" igual a \"c\"?: {"Si" if np.allclose(d - a, c) else "No"}")
print("-------------------------------")


#12. Multiplica a y c. Asigna el resultado a e.
print("Multiplicar \"a\" y \"c\" para crear \"e\"")
e = a * c
print(f"e:\n {e}")
print("-------------------------------")

#13. ¿Es e igual a a? ¿Por qué sí o por qué no?
print("Comparar \"a\" y \"e\"")
print(f"a:\n {a}")
print(f"e:\n {e}")
print("""
La diferencia entre a y e es que e es el resultado de multiplicar a y c, donde c es b transpuesto.
Por lo tanto, cada valor en e es el producto de un valor en a y un valor en c. Como c es un array de unos,
cada valor en e es el valor correspondiente en a.
Al haber multiplicado por 1 cada valor en a, e es igual a a. No tenemos que preocuparnos por la precisión
de los valores porque la multiplicación de floats es exacta (almenos multiplicando por 1).
""")
print(f"Es \"a\" igual a \"e\"?: {"Si" if np.array_equal(a, e) else "No"}")
print("-------------------------------")

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"
print("Identificar valores máximos, mínimos y medios en \"d\"")
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print(f"d:\n {d}")
print(f"máximo de \"d\": {d_max}")
print(f"mínimo de \"d\": {d_min}")
print(f"media de \"d\": {d_mean}")
print("-------------------------------")

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.
print("Crear array \"f\"")
f = np.empty((2,3,5))
print(f"f:\n {f}")
print("-------------------------------")

"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""
print(f"Rellenar valores en \"f\" usando \"d\"")
# for i in range(d.shape[0]):
#     for j in range(d.shape[1]):
#         for k in range(d.shape[2]):
#             if d[i,j,k] > d_min and d[i,j,k] < d_mean:
#                 f[i,j,k] = 25
#             elif d[i,j,k] > d_mean and d[i,j,k] < d_max:
#                 f[i,j,k] = 75
#             elif d[i,j,k] == d_mean:
#                 f[i,j,k] = 50
#             elif d[i,j,k] == d_min:
#                 f[i,j,k] = 0
#             elif d[i,j,k] == d_max:
#                 f[i,j,k] = 100
f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100
print(f"f:\n {f}")


"""
#17. Imprime d y f. ¿Tienes el f esperado?
Por ejemplo, si tu d es:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Tu f debería ser:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print("Comparar \"d\" y \"f\"")
print(f"d:\n {d}")
print(f"f:\n {f}")
print("--------------------------------")

"""
#18. Pregunta de bonificación: en lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena
("A", "B", "C", "D" y "E") para etiquetar los elementos del array? Esperas el resultado sea:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
De nuevo, no necesitas Numpy en esta pregunta. (lo uso para no mutar el array f)
"""
print(f"Rellenar valores string en \"g\" usando \"d\"")
g = np.empty((2,3,5), dtype=str)
g[(d > d_min) & (d < d_mean)] = "B"
g[(d > d_mean) & (d < d_max)] = "D"
g[d == d_mean] = "C"
g[d == d_min] = "A"
g[d == d_max] = "E"
# for i in range(d.shape[0]):
#     for j in range(d.shape[1]):
#         for k in range(d.shape[2]):
#             if d[i,j,k] > d_min and d[i,j,k] < d_mean:
#                 g[i,j,k] = "B"
#             elif d[i,j,k] > d_mean and d[i,j,k] < d_max:
#                 g[i,j,k] = "D"
#             elif d[i,j,k] == d_mean:
#                 g[i,j,k] = "C"
#             elif d[i,j,k] == d_min:
#                 g[i,j,k] = "A"
#             elif d[i,j,k] == d_max:
#                 g[i,j,k] = "E"

print(f"g:\n {g}")
print("-------------------------------")

