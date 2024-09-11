def solution(num_list):
    answer = 0
    for x in num_list :
        if 2 <= x < 4 :
            answer += 1
        elif 4 <= x < 8 :
            answer += 2
        elif 8 <= x < 16 :
            answer += 3
        elif 16 <= x :
            answer += 4
    return answer