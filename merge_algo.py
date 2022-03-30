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


#when you compare the last first two elements from the both halfs, you are sure
#there are no elements behiend this element is less than the first element
#you are comparing with. [123] and [456]
# 4 is the lowest element in it's array and 1 is the lowest in it's array. 

# in merge sort we are comparing first number with half of the array because we sorted 
# the all the element both halfs, so if the first element in first half is greater than 
# the whole second half, we will but the first half with out comparing. 
# and the main key that we compare the element with the second half only  not with the 
# whole array which keeps us half of time in comparing.