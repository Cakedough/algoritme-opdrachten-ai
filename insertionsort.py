def insertionSortRecursive(arr,n): 
    if n<=1: 
        return
    insertionSortRecursive(arr,n-1) 
    last = arr[n-1] 
    j = n-2
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
  
    arr[j+1]=last 
    return arr


def mainfunction():
    mylist = []
    for i in reversed(range(1,900)):
        mylist.append(i)
    print(mylist)

    mylist = insertionSortRecursive(mylist, len(mylist))
    print(mylist)


if __name__ == '__main__':
    mainfunction()



