def solution(num_list):
    mul = 1
    add = 0
    for i in num_list :
        mul *= i
        add += i
    if mul < add**2 :
        return 1
    return 0