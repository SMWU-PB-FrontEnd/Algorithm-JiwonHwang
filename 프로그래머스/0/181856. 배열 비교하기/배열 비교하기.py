def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    sumA = sum(arr1)
    sumB = sum(arr2)
    
    if a > b : return 1
    elif a < b : return -1
    else :
        if sumA > sumB : return 1
        elif sumA < sumB : return -1
        else : return 0
            