# if condicion:
#   codigo
# elif condicion:
#   codigo
# else:
#   codigo

edad = 31
genero = "Mujer"
nombre = "Mariana"

if (genero == "Mujer" and edad >= 18 and edad <= 100 and edad > 0):
    print(f'{nombre} obtiene la promoción')
elif edad > 100:
    print(f'{nombre} tiene una edad mucho mayor (NO ES POSIBLE)')
elif edad < 0:
    print(f'{nombre} tiene una edad negativa')
elif edad < 18:
    print(f'{nombre} es menor de edad')
else:
    print(f'{nombre} NO es mujer')
