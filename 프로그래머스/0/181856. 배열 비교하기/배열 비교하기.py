def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    sumA = 0
    sumB = 0
    
    if a > b : return 1
    elif a < b : return -1
    else :
        for i in range(a) :
            sumA += arr1[i]
            sumB += arr2[i]
        if sumA > sumB : return 1
        elif sumA < sumB : return -1
        else : return 0
            