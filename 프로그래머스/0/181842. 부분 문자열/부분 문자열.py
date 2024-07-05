def solution(str1, str2):
    a = len(str1)
    b = len(str2)
    for i in range(b) :
        if str2[i:i+a] == str1 :
            return 1
    return 0