def MaxMax (L):
    if len(L)==1:
      return (-1, L[0])
    elif len(L) == 2:
        if L[0] <= L[1]:
           return (L[0], L[1])
        else:
           return (L [1],L [0])
    else: 
        mid = len(L)/2
        (max1L, max2L) = MaxMax(L[:int(mid)])
        (max1R, max2R) = MaxMax(L[int (mid):])
        if max2L >= max2R:
            max2=max2L
            max1=max2R 
            if max1L>max1:
               max1=max1L
        else:
            max2 = max2R 
            max1 = max2L
            if max1R>max1:
               max1=max1R
    return (max1, max2)
def main():
	lista = [3,10,32,100,4,76,45,32,17,12,1]
	print("Los valores son: ",MaxMax(lista))
main()