# Operadores logicos

'''
# Operador logico AND
# print(False and False)

# Ejemplo practico con condiciones
variable_1 = 30
variable_2 = 30
variable_3 = 25

condicion_1 = variable_1 == variable_2
print(f"Resultado de la condicion_1 es: {condicion_1}")
condicion_2 = variable_2 >= variable_3
print(f"Resultado de la condicion_2 es: {condicion_2}")
resultado = condicion_1 and condicion_2 and False
print(f"{condicion_1} AND {condicion_2} es: {resultado}")


# Operador logico OR
# print(False or False)

# Ejemplo de OR
variable_1 = 35
variable_2 = 30
variable_3 = 30

condicion_1 = variable_1 <= variable_2
print(f'Condicion 1 es: {condicion_1}')
condicion_2 = variable_2 != variable_3
print(f'Condicion 2 es: {condicion_2}')
resultado = condicion_1 or condicion_2
print(f'{condicion_1} OR {condicion_2} es: {resultado}')


# Operador logico NOT Booleanas
print(not -25)


# Combinacion de operaciones logicas
A = True
B = True
C = False

Compuerta_1 = not(A and B)
Compuerta_2 = not(C)
Resultado = Compuerta_1 or Compuerta_2
print(f"El resultado es: {Resultado}")
'''

# Ejemplo del bar 
# Entrada gratis a mujeres mayores de 18 

edad = 56
genero = "Mujer"

condicion_1 = edad >= 18
print(f"¿Es mayor de edad? {condicion_1}")
condicion_2 = genero == "Mujer"
print(f"¿La persona es mujer? {condicion_2}")
resultado = condicion_1 and condicion_2
print(f"¿La persona es mayor de edad y es mujer?: {resultado}")