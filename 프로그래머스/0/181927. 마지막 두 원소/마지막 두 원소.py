def solution(num_list):
    l = len(num_list)
    m = num_list[l-1]
    n = num_list[l-2]
    if m > n :
        num_list.append(m-n)
    else :
        num_list.append(m*2)
    return num_list