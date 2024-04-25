# Variables

#String
my_string_variable = "My String Variable"
print(my_string_variable)

#Integer
my_int_variable = 5
print(my_int_variable)

#Boolean
my_bool_variable = True
print(my_bool_variable)

#Concatenación de variables
print(my_string_variable, my_int_variable)
print("este es el valor de mi variable", my_int_variable)


#Algunas funciones del sistema

print(len(my_string_variable)) #Mide el largo de la variable

#Variables en una sola línea

name, lastname, email, age = "Oscar", "Pereyra", "oscarpereyra.mhs@gmail.com", 32
print("Tengo:", age,"Mi apellido es:", lastname, "Mi correo es:", email,"Mi nombre es:", name)

#Inputs

name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
print(name)
print(lastname)

#¿Forzando el tipo?
#En Python podes declarar que tipo de variable va a ser, pero la variable siempre puede ser sobreescrita
#Por otro tipo de dato.
address: str = "Mi direccion"
address = 32
print(address)
