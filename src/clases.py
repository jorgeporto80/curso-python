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


# Identidad
numero1 = 3
numero2 = 3

print(id(numero1))
print(id(numero2))

# numero1 = 4
# print(id(numero1))

# numero1 = 3
# print(id(numero1))

print(numero1 is numero2)


