# Para entrar al interprete escribimos "Python" para salir Ctrl+d
print("Hola mundo")

# VAriables

# Dinamicamente tipado
cantidad = 1
print(type(cantidad))
cantidad = "Perro"
print(type(cantidad))

# Fuertemente tipado
numero1 = 10
numero2 = "20" # int(numero2)
print("Numero1: ", type(numero1))
print("Numero2: ", type(numero2))

numero2 = int(numero2)

print(numero1 + numero2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# String, cómo declaro un String
mi_nombre = "Jorge"
mi_nombre = 'Jorge'

mi_nombre = 'Jorge "macho" Porto'
mi_nombre = "Jorge 'macho' Porto"

mi_nombre = '''Jorge camina
por la calle'''

mi_nombre = "Jorge camina \n por la calle"

mi_nombre = '''Jorge camina 
\n por la calle'''

print(mi_nombre)

# Constante
MI_NOMBRE = 1

MI_DNI = 27941513

# Comentario de una sola linea
cantidad = 1 # esto es otro comentario 

''' 
Esto es un comentario de varias lineas
Hola
'''
print(cantidad)


# Operadores
cantidad = 10
print(cantidad)

cantidad += 1 # cantidad = cantidad + 1
cantidad *= 2 # cantidad = cantidad * 2
print(cantidad)

# "H" in "Hola mundo"
# True


# Identidad
numero1 = 3
numero2 = 3

print(id(numero1))
print(type(numero1))
print(numero1)

print(id(numero2))
print(type(numero2))
print(numero2)

numero2 = 4
print(id(numero2))
print(type(numero2))
print(numero2)

numero2 = 3
print(id(numero2))
print(type(numero2))
print(numero2)



numero1 = 4
print(id(numero1))

numero1 = 3
print(id(numero1))

print(numero1 is numero2)

for i in range(2): 
    numero = i
    print(id(numero))
    print(type(numero))
    print(numero)

for i in range(2): 
    numero = i
    print(id(numero))
    print(type(numero))
    print(numero)

mi_lista1 = [1,2,3]
mi_lista2 = [1,2,3]

print(id(mi_lista1))
print(type(mi_lista1))
print(mi_lista1)
print(id(mi_lista2))
print(type(mi_lista2))
print(mi_lista2)

numero = 2

# if numero == 1:
#     print("1")
# elif numero == 2:
#     print("2")
# elif numero == 3:
#     print("3")


# if numero > 3:
#      print("Si 3")
# elif numero > 4:
#     print("si 4")
# else:
#     print("no")


# Ternario
numero = 2
valor =  "Es mayor a 3" if numero > 3 else "No es mayor a 3"


print(valor)




# cadena = "Hola mundo"
# cadena = [1,2,3,4,5]

# suma = 0

# for elemento in cadena:
#     suma += elemento
#     print(suma)

# print("Resultado final:",suma)


#range("valor inicial", "hasta ....hasta -1", "saltos")

# for vuelta in range(5):
#     if vuelta == 8:
#         print("brake")
#         break
#     print("doy vueltas", vuelta)
# else: 
#     print("Terminé")


# mi_lista = [[1,2,3],[4,5,6],[7,8,9]]


# for elemento_lista in mi_lista[0:2]:
#     print(elemento_lista)
#     for sublementos in elemento_lista:
#         print(sublementos)


mi_lista = [1,2,3,4,4,5,6]
elemento = 0 
indice = 0

while elemento != 4:

    elemento = mi_lista[indice] 
    indice += 1    
    
    if elemento == 2:
        continue
    

    print(elemento)


    if indice == len(mi_lista) -1:
        print("No encontre el 4")
        break
else:
    print("Lo encontre")

