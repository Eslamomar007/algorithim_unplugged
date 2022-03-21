#merge algorithim code to sort a list in time complixity (nlogn)

def merge_sort(arr):
    if len(arr)<2:
        return 

    else :
        #spliting the array to two parts 
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        #recursive code
        merge_sort(left)
        merge_sort(right)

        # sorting code and merging 
        i=j=k =0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k] =right[j]
                j+=1
            k+=1

        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        
        while j< len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    
# sample code to test the algorithm 
arr = [44,22,55,11,565,5]
print(merge_sort(arr))
print(arr)