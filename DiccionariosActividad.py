#1.Crea un diccionario vacío llamado perro
Perro ={}
#2.Añade nombre, color, raza, patas y edad al diccionario perro.
Perro['nombre'] = 'tyson'
Perro['color'] = 'blanco'
Perro['raza'] = 'bulldog'
Perro['patas'] = '4'
Perro['edad'] = '6'
print(Perro);
#3.Crea un diccionario de estudiante y añade nombre, apellido, sexo, edad, estado civil, habilidades, país, ciudad y dirección como claves del diccionario
estudiante ={'nombre':'jaime','apellido':'carreazo','sexo':'masculino', 'edad':'19','estado civil':'casado','habilidades':['pyton','java'],'país':'colombia','ciudad':'cartagena', 'direccion':'av pedro romero,barrio libano'}
print(estudiante);
#4.Obtén la longitud del diccionario del alumno
print(len(estudiante))
#5.Obtenga el valor de las habilidades y compruebe el tipo de datos, debe ser una lista
habi=[estudiante['habilidades']]
print(habi)
print(type(habi))
#6.Modifique los valores de las aptitudes añadiendo una o dos aptitudes
habi.insert(6,'c++')
habi.insert(6,'php')
print(habi);
#7.Obtener las claves del diccionario como una lista
claves=estudiante.keys()
print(claves)
#8.Obtener los valores del diccionario como una lista
valores=estudiante.values()
print(valores)
#9.Cambie el diccionario a una lista de tuplas utilizando el método items()
est=estudiante.items()
print(est)
#10.Eliminar uno de los elementos del diccionario
estudiante.pop('apellido')
#11.
print(estudiante.clear())
