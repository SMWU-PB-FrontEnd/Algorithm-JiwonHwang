def solution(arr):
    for i, x in enumerate(arr) :
        if x >= 50 and x % 2 == 0 :
            arr[i] = x/2
        elif x < 50 and x % 2 == 1 :
            arr[i] = x*2
    return arr