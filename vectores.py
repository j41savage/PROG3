#JAIME ENRIQUE CARREAZO GUARDO

#1.Declarar una lista vacía
lst= list()

#2.Declarar una lista con más de 5 elementos
list1 = ["Jaime","Enrique","Maria", "Camila"]

#3.Encuentre la longitud de su lista
print(len(list1))

#4.Obtener el primer elemento, el elemento central y el último elemento de la lista
Proplayers =["m1ndfreak","something","forsaken","d4v41","Monyet"]

first_proplayer = Proplayers[0]
print(first_proplayer)
mid_proplayer = Proplayers[2]
print(mid_proplayer)
last_proplayer = Proplayers[4]
print(last_proplayer)

#5.Declara una lista llamada tipos_datos_mezclados, pon tu(nombre, edad, altura, estado civil, dirección)
tipos_datos_mezclados =["Jaime","19","1.75","Soltero","Av.pedro romero,Barrio libano#48c43"]

#6.Declare una variable de lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM","Amazon","Oracle"]

#7.Añadir una empresa de TI a it_companies utilizando los metodos de insercion.
it_companies.append("Sony")
print(it_companies)

#8.Comprobar si una determinada empresa existe en la lista it_companies.
if it_companies.index("Google"):
    print("La empresa si existe")
    
#9.Ordena la lista con el método sort()
it_companies.sort()
print(it_companies)

#10.Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()
print(it_companies)
    
#11.Elimine la primera empresa informática de la lista.
it_companies.pop
it_companies.pop(0)
print(it_companies)

#12.Eliminar todas las empresas de TI de la lista
it_companies.clear
it_companies.clear()
print(it_companies)
