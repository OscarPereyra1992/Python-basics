### Strings ###

my_string = "My string"
my_other_string = "My other string"

print(len(my_string))#Muestra la cantidad de caracteres de un string
print(len(my_string)+len(my_other_string)) #Suma la cantidad de caracteres de dos o mas strings

print(my_string + " " + my_other_string) #Concatena dos strings


my_new_line= "Este es un string\ncon salto de línea" #string con salto de línea
print(my_new_line)


my_tab_line= "\tEste es un string con tabulación" #string con tabulación
print(my_tab_line)

my_scape_line= "\tEste es un string\nescapado" #string con tabulación y salto de línea
print(my_scape_line)

##Formateo

name, surname, age= "Oscar", "Pereyra", 31


print("Mi nombre es {} {} y my edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y my edad es %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #Con la f adelante le das formato

#Desempaquetado de carácteres
language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones del sistema

print(len(my_string)) #Mide el largo de la variable
print(my_string.upper()) #Convierte a mayúsculas
print(my_string.lower()) #Convierte a minúsculas
print(my_string.capitalize()) #Convierte la primera letra a mayúscula
print(my_string.count("s")) #Cuenta cuantas veces aparece una letra en un string
print(my_string.isnumeric()) #Revisa si dentro del string hay números
print("1".isnumeric()) #Revisa si dentro del string hay números
