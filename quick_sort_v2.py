def quick(li):
    if len(li) <2:
        return li

    else: 
        pivot = li[-1] 
        less = [ i for i in li[:-1] if i <= pivot ]
        greater = [i for i in li[:-1] if i > pivot]
        return quick(less)+[pivot]+quick(greater)

print(quick([4,3,5,2,1]))