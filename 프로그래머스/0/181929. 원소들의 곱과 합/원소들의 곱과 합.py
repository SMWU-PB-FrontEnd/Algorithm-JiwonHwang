def solution(num_list):
    mul = 1
    add = 0
    for i in range(len(num_list)) :
        mul *= num_list[i]
        add += num_list[i]
    if mul > add**2 :
        return 0
    else :
        return 1