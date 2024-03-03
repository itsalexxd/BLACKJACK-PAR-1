# print ("Hola")
# print ("Prueba")

# a = 1
# b = 5.2

# print (a + b)

# type(a)
# print (type(b))

# c = int (input ("Introduce un numero: "))
# d = int (input ("Introduce otro numero: "))

# resta = c - d

# print (resta)

# #comentario en python


# #programa en python que sume 2 numeros
# # input -> por defecto devuelve un string
# # como hacer un cast int (input)


# # solicita la edad de una persona hasta que sea mayor de edad

# edad = int (input ("Inserte la edad: "))

# while(edad < 18):
#     print ("Menor de edad")
#     edad = int (input ("Inserte la edad: "))
    
# print ("Mayor de edad")

# print ("La edad insertada es de: " + str(edad))

# # version con if

# edad2 = int (input ("Inserte la edad: "))

# if edad2 >= 18:
#     print ("Mayor de edad")
# else:
#     print ("Menor de edad")



# quiero saber cuantos numeros menores de edad se han introducido
# edad = int (input ("Inserte la edad: "))
# menoresEdad = 0
# listaMenores = []


# while(edad < 18):
#     if edad < 18:
#         menoresEdad += 1
#         listaMenores.append(edad)
#     edad = int (input ("Inserte la edad: "))
    

# print ("La cantidad de menores de edad es de: " + str(menoresEdad))
# print (listaMenores)

# for i in listaMenores:
#     print (i, end=" ") 
    
    
# calcular el factorial de un numero que se le pasa como argumento a la funcion fact()

# num = int(input ("Inserte el numero para calcular el factorial: "))

# def fact(num):    
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i  
#     return factorial

# print ("El factorial es: ")
# print (fact(num))

# if num > 18:
#     print ()



cadena = input ("String:")

print (cadena)
print (type(cadena))