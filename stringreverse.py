import random 
import string


def recursiveReverseString(_string, _low, _high):
    if (_low >= _high):
        return
    
    recursiveReverseString(_string, _low + 1, _high - 1)
    
    _string[_low] , _string[_high] = _string[_high], _string[_low]
    return _string


def mainfunction():
    myString = ''.join(random.choices(string.ascii_uppercase, k = 300)) 
    myStringList = []
    for i in myString:
        myStringList.append(i)
    print(myString)

    myString = recursiveReverseString(myStringList, 0, len(myString)-1)
    print(''.join(myString))


if __name__ == '__main__':
    mainfunction()
