def solution(my_string, target):
    a = len(my_string)
    b = len(target)
    for i in range(a) :
        if my_string[i:i+b] == target :
            return 1
    return 0