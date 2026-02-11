# Condicionales
'''
nombre = "Jorge"
edad = 20 

# --------Estructura------ 
# if condicion:
#   ejecucion de codigo

if edad >= 18: 
    print(f"{nombre} es mayor de edad.")


#-----------Estructura 2------------
# if condicion:
#   codigo
# else: 
#   codigo

nombre = "Jorge"
edad = 25

if edad > 18:
    print(f"{nombre} es mayor de edad.")
else:
    print(f"{nombre} es menor de edad.")

'''

# Estructura 3
# if condicion:
#   codigo
# elif condicion:
#   codigo
# else:
#   codigo

nombre = "Jorge"
edad = 99.999

if edad < 0:
    print(f"Usted tecleo mal la edad")
elif edad >= 100:
    print(f"Usted tecleo mal la edad")
elif edad < 18:
    print(f"{nombre} es menor de edad")
else:
    print(f"{nombre} es mayor de edad")