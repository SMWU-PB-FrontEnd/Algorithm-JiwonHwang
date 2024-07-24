def solution(arr, intervals):
    a1 = intervals[0][0]
    a2 = intervals[0][1]
    b1 = intervals[1][0]
    b2 = intervals[1][1]
    
    return arr[a1:a2+1]+arr[b1:b2+1]