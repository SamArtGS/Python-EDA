def insertionSort(n_lista):
    for index in range(1,len(n_lista)):
        #este ciclo for trabaja con los elementos de la lista
        #1 al n  elemento de esta, pero recordemos que
        #el primer elemento de la lista esta representado con la 
        #posicion 0,por ende este ciclo for no toma en cuenta el valor
        #del primer elemento de la lista
        actual = n_lista[index]
        posicion = index
        print("valor a ordenar = {}".format(actual))
        #actual sera cada elemento de la lista apartir del
        #segundo elemento de esta, ya que recordemos que 
        #el primer elemento de la lista no es tomado en cuenta
        #debido a que este se encuentra en la posicion numero 0
        #de la lista , y el ciclo for empieza a trabajar apartir 
        #del posicion numero 1 de la lista.
        
        while posicion>0 and n_lista[posicion-1]>actual:
            n_lista[posicion]=n_lista[posicion-1]
            posicion = posicion-1           
        n_lista[posicion]=actual
        print(n_lista)
        print() 
    return n_lista

lista = [21, 10, 0, 11, 9, 24, 20, 14, 1]
print("lista desordenada {}".format(lista))
insertionSort(lista)
print("lista ordenada {}".format(lista))