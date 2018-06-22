def quicksort(lista):
    quicksort_aux(lista,0,len(lista)-1)
    #Utiliza a la funcion quickort_aux
    #INICIO =primer elemento de la lista
    #FINAL =penultimo elemento de la lista
    #RANGO DE LISTA=primer elemento de la lista
    #a penultimo elemento de la lista.

def quicksort_aux(lista,inicio, fin):
    if inicio < fin: 
        
        pivote = particion(lista,inicio,fin)
        #utiliza a la funcion partition
        quicksort_aux(lista, inicio, pivote-1)
        
        quicksort_aux(lista, pivote+1, fin)
        

def particion(lista, inicio, fin):
    #Se asigna como pivote en número de la primera localidad
    pivote = lista[inicio]
    #recordemos que... inicio=0 por lo tanto:
    #lista[inicio]=lista[0]=primer elemento de la lista
    #PRIMER PIVOTE=PRIMER ELEMENTO DE LA LISTA
    print("Valor del pivote {}".format(pivote))
    #Se crean dos marcadores 
    izquierda = inicio+1
    derecha = fin
    print("Índice izquierdo {}".format(izquierda))
    print("Índice derecho {}".format(derecha))

    
    bandera = False
    while not bandera:
    #mientras no sea falso que:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda + 1
        while lista[derecha] >= pivote and derecha >=izquierda:
            derecha = derecha -1
        if derecha < izquierda:
            bandera= True
        else:
            temp=lista[izquierda]
            lista[izquierda]=lista[derecha]
            lista[derecha]=temp
            
    print(lista)


    temp=lista[inicio]
    lista[inicio]=lista[derecha]
    lista[derecha]=temp
    return derecha

lista = [21, 10, 0, 11, 9, 24, 20, 14, 1]
lista1=[99,100]
lista2=[100,101,99]
lista3=[102,100,99,101]
lista4=[100,102,99,101,103]
lista5=[103,101,99,102,100,104]
print("lista desordenada {}".format(lista5))
quicksort(lista5)
print("lista ordenada {}".format(lista5))