#hago una lista  llamada cajita 
cajita = [1,2,2.5,"obj"]
x = 1
y = 1

#en cualquier otro lenguaje de programacion serian dos cajitas distintas en distintas posiciones de memoria
#que almacenan el valor 1

#pero en Python al estar tan orientado a objetos con el id(1), veo la posicion de memoria
print("Imprimo objeto 1:")
print(id(1))
print()
print("Imprimo variable x")
print(id(x))
print()
print("Imprimo variable y")
print(id(y))
print()
print("Imprimo primer objeto de cajita") 
print(id(cajita[0]))
#a diferencia de otros lenguaje de programacion Python toma 1 como un objeto y vive y toma su existencia en una posicion de memoria
# y la variable es un label, en este caso esta el objeto 1 que vive en la parte de memoria que devuelve el id, pero tiene varias 
# etiquetas
cajita[0]=0
print()
print("Cambie el primer dato de la cajita de 1 a 0, direccion de memoria de cajita")
print(cajita)
print(id(cajita))


