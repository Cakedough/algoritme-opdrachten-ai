import random
from time import sleep as ts
from bisect import insort_left


def binarySearch(arr, low, high, key): 
    '''
    A binary search function that compares middle of list to key and traverses a subarray to the left or right, depending on comparison
    \nReturns index of key, the first element, or the last element.
    \n!!! - REQUIRES SORTED LIST AS INPUT - !!!
    '''
    print("\n\t|BinarySearch function called with parameters: \n\t|arr:{} \n\t|low: {} -- high: {} -- key: {}".format(arr,low,high,key))
    # if key < array[0] -> return index first element
    if high == -1:
        print("\t|Leftmost traverse out of list. Returning: 0")
        return 0
    # if key > array[-1] -> return index last element
    elif high < low:
        print("\t|Rightmost traverse out of list. Returning last index: {}".format(high))
        return high
          
    # low + (high - low)/2;     
    mid = int((low + high)/2) 
    print("\t|Mid index equals {}".format(mid))
    
    # compare key with value in the middle of (sub)list
    # return if equal
    print("\t|Comparing mid value with key: {} == {}".format(arr[mid], key))
    if key == arr[mid]: 
        print("\t|Number found!!! Returning index: {}".format(mid))
        return mid 
    # check on what side the key is in.
    # left side: recursive call with subarray [low:mid-1]
    # right side: recursive call with subarry [mid+1:high]
    print("\t|Checking if key is in left or right subarray..")
    if key > arr[mid]:
        print("\t|Key is in right subarray")
        return binarySearch(arr, (mid + 1), high, key)
    print("\t|Key is in left subarray")
    return binarySearch(arr, low, (mid -1), key)


def balanceScale(_L, _R):
    '''
    Main function to balance weights. Input must be a sorted array.
    Returns array tuple (_L, _R)
    '''
    print("\nStart of this iteration:")

    sumLeft = sum(_L)
    print("sumleft:", sumLeft)
    sumRight = sum(_R)
    print("sumright", sumRight)
    sumTotal = sumLeft + sumRight
    print("sumTotal", sumTotal)
    target = 0

    # win conditions: 
    # - total weight even -> som(_L) == K/2 (true balance)
    # - total weight uneven -> som(_L) == K/2 +- 2 (optimal balance)
    if (sumTotal) % 2 == 0:
        print("Total is even: ", sumTotal)
        target = sumLeft - sumTotal/2
        if target == 0:
            print("The scale is balanced!")
            print("Returning _L as: ", _L)
            print("Returning _R as: ", _R)
            return _L, _R
    else:
        print("Total is uneven: ", sumTotal)
        # in uneven scenario balance is achieved when one side is
        # (totalweight+1)/2 or (totalweight-1)/2
        # in this case only -1 is used because L>R always, and target
        # is representing the weight that needs to move to R
        target = sumLeft - (sumTotal-1)/2
        if target == 1:
            print("The scale is optimally balanced!")
            print("Returning _L as: ", _L)
            print("Returning _R as: ", _R)
            return _L, _R
    
    print(_L, " -- ", sum(_L), " ---- (>",target,">) ----", sum(_R)," -- ", _R)


    # if smallest element in _L is bigger than the target:
    # look if two weights can be swapped between _L and _R to achieve balance
    # by using a binarysearch per element in _L, with the key being equal to
    # the element - target.
    if _L[0] > target:
        print("First element of L > target: ", _L[0], ">", target)
        print("Iterating list _L...")
        for i in range(0, len(_L)):
            indexR = binarySearch(_R, 0, len(_R)-1, _L[i]-target)
            print("The target: {}".format(target))
            print("The current element: {}".format(_L[i]))
            print("Looking for value: {}".format(_L[i]-target))
            print("The returned value: {}".format(_R[indexR]))
            if _L[i] - target == _R[indexR] == target:
                print("Returned value is the value we are looking for!")
                print("swapping values _L[i] and _R[indexR]...: ", _L[i], "<->", _R[indexR])
                insort_left(_R, _L[i])
                _L.pop(i)
                insort_left(_L, _R[indexR])
                break
            else:
                pass
                print("Returned value is not the value we are looking for...")

        # to prevent infinite loops, return _L and _R after one big loop.
        print("\nThis is where the heuristic part kicks in...")
        print("Returning _L as: ", _L)
        print("Returning _R as: ", _R)
        return _L, _R

    else:
        # the target value is either (1) in the list (2) bigger than any weight in the list
        # look for the closest value in _L to the target and move it to the other side
        print("Searching for (approximation of) target in _L")
        indexL = binarySearch(_L, 0, len(_L)-1, target)
        print("Target = {} -- Approximation = {}".format(target, _L[indexL]))
        print("Moving approximation to other side")
        insort_left(_R, _L[indexL])
        _L.pop(indexL)

    print("\nResult of this iteration:")
    print(_L, " -- ", sum(_L), " ---- ", sumTotal/2," (", sumTotal, ") ", sumTotal/2, " ----", sum(_R)," -- ", _R)

    ts(0.5)
    # call function recursively. This algorithm depends on _L being bigger than _R
    # so if _R is bigger, the arrays are passed mirrored
    if sum(_R) > sum(_L):
        return balanceScale(_R, _L)

    else:
        return balanceScale(_L, _R)


#----------------------------------------------------------------------#


def mainfunction():
    L = []
    R = []

    for i in range(1, 100):
        L.append(random.randint(1,50))

    L.sort()
    L, R = balanceScale(L, R)

if __name__ == '__main__':
    mainfunction()
