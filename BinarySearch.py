def it_binarySearch(mylist,target):
    first = 0
    last = len(mylist)-1
    while first <= last:
    	midpoint = int((first+last)/2)
    	if mylist[midpoint] == target:
    	   return midpoint
    	else:
    		if target < mylist[midpoint]: 
    	    	 last = midpoint-1
    		else:
    			first = midpoint+1
    return None
test_list = [0,3,4,7,9,11,34,46,57,65]
print(it_binarySearch(test_list,4))
print(it_binarySearch(test_list,30))
print(it_binarySearch(test_list,57))
print(it_binarySearch(test_list,46))
print(it_binarySearch(test_list,11))
print(it_binarySearch(test_list,34))
print(it_binarySearch(test_list,20))
print(it_binarySearch(test_list,25))
print(it_binarySearch(test_list,66))
print(it_binarySearch(test_list,5))