#This function removes all values from list a that are present in list b
def array_diff(a, b):
    if len(b) and len(a) > 0:
        for x in b:
            while True:
                try:
                    a.remove(x)
                except:
                    break
    print(a)
    return(a)
#The following examples will output the intended result
array_diff([1,2], [1])                                      
array_diff([1,2,2], [1])
array_diff([1,2,2], [2])
array_diff([1,2,2], [])
array_diff([], [1,2])
array_diff([-7, -4, -9, -8, 11, 15, -18, -1, -11, 1, 8],[])
array_diff([],[-5, 8, 10, 4, -11, 17, -4, 14, -13, -20, -7, -20, -8, 4])
