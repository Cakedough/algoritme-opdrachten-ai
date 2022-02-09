import math


def mergeSort(arr):
    if len(arr) >1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves
 
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
 
        i = j = k = 0
         
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1
         
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1
         
        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1
    return arr

def worstCaseArrayOfSize(n):
    if n == 1:
        return [1]
    else:
        top = worstCaseArrayOfSize(int(math.floor(float(n) / 2)))
        bottom = worstCaseArrayOfSize(int(math.ceil(float(n) / 2)))
        result = list(map(lambda x: x * 2, top)) + list(map(lambda x: x * 2 - 1, bottom))
        return result

def mainfunction():
    mylist = worstCaseArrayOfSize(300)
    print(mylist)
    mylist = mergeSort(mylist)
    print(mylist)

if __name__=='__main__':
    mainfunction()