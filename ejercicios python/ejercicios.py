
aprendices = []
edades = []
'''
1. Llenar las listas solicitando los datos por teclado
'''
cantidad = int(input("Digite la cantidad de aprendices: "))

for i in range(cantidad):
    nombre = input("Digite el nombre del aprendiz: ")
    edad = int(input("Digite la edad del aprendiz: "))

    aprendices.append(nombre)
    edades.append(edad)

print("\n1. LISTAS LLENAS")
print("Aprendices:", aprendices)
print("Edades:", edades)
'''
2. Imprimir las listas
'''
print("\n2. IMPRIMIR LAS LISTAS")
print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)
'''
3. Mostrar el aprendiz con la mayor edad
'''
print("\n3. APRENDIZ CON MAYOR EDAD")
mayor = max(edades)
posicion = edades.index(mayor)

print("Aprendiz:", aprendices[posicion])
print("Edad:", mayor)
'''
4. Insertar el nombre de la instructora en la posicion 1
'''
print("\n4. INSERTAR LA INSTRUCTORA")
instructora = input("Digite el nombre de la instructora: ")
aprendices.insert(1, instructora)

print("Lista de aprendices:", aprendices)
'''
5. Contar cuantos aprendices tienen 18 años
'''
print("\n5. APRENDICES QUE TIENEN 18 AÑOS")
print("Cantidad:", edades.count(18))
'''
6. Agregar un aprendiz x al final de la lista
'''
print("\n6. AGREGAR APRENDIZ X")
aprendices.append("x")

print("Lista de aprendices:", aprendices)
'''
7. Borrar el nombre de la instructora de la lista
'''
print("\n7. BORRAR EL NOMBRE DE LA INSTRUCTORA")
aprendices.remove(instructora)

print("Lista de aprendices:", aprendices)
'''
8. Indicar un dato a buscar en la lista
'''
print("\n8. BUSCAR UN APRENDIZ")
buscar = input("Digite el nombre que desea buscar: ")

if buscar in aprendices:
    print(buscar, "se encuentra en la lista")
else:
    print(buscar, "no se encuentra en la lista")
'''
9. Mostrar los primeros 10 aprendices
'''
print("\n9. PRIMEROS 10 APRENDICES")
print(aprendices[:10])
'''
10. Mostrar los 10 ultimos aprendices
'''
print("\n10. ULTIMOS 10 APRENDICES")
print(aprendices[-10:])
'''
11. Mostrar del elemento 10 al elemento 20
'''
print("\n11. ELEMENTOS DEL 10 AL 20")
print(aprendices[9:20])
'''
12. Mostrar los elementos cuyo indice sea par
'''
print("\n12. APRENDICES CON INDICE PAR")

for i in range(0, len(aprendices), 2):
    print("Indice:", i, "- Aprendiz:", aprendices[i])
