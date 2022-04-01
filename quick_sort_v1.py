def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = len(arr)//2
        start = 0
        left = []
        right=[]
        while(start < len(arr)):
            if start == pivot:
                pass
            elif arr[start] >arr[pivot]:
                right.append(arr[start])
            else:
                left.append(arr[start])
            start +=1

        return quick_sort(left)+[arr[pivot]]+quick_sort(right)


arr= [33,22,44,11,55,99,9]
print(quick_sort(arr))