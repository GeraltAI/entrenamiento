#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

vec1 = [1,2,3]
vec2 = [-1,0,2]
producto = []
for i in range(0,3):
    producto.append(vec1[i]*vec2[i]) # seguro hay una manera mas inteligente de hacerlo    
print(sum(producto))

# sí funciona. Pero esto es mas inteligente:

a = (1, 2, 3) #convenia guardarlo en una tupla!
b = (-1, 0, 2)
product = 0   # genera un contador
for i in range(len(a)):
    product += a[i]*b[i] # a ese contador le va sumando cada iteracion multiplicativa