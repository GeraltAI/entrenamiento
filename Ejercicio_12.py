#Escribir un programa que almacene las matrices
 
 # las matrices no se ven porque aqui no se pueden poner, xd

#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

A = [[1,2,3],[4,5,6]]
B = [[-1,0],[0,1],[1,1]]

# a grandes rasgos ya esta resulto, solo debo aplicar esto 4 veces cambiando los subindices...debo encontrar una manera de automatizarlo
B1 = [] 
AB00 = []
for i in range(0,3):
    B1.append(B[i][0])
for j in range(0,3):
    AB00.append(A[0][j]*B1[j])
print(sum(AB00))