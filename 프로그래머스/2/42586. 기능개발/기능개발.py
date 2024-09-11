import math 

def solution(progresses, speeds):
    days = []
    for i, x in enumerate(progresses) :
        days.append(math.ceil((100-x)/speeds[i]))
    count = 0
    answer = []
    k = days[0]
    for i in range(len(days)) :
        if k < days[i] :
            answer.append(count)
            count = 0
            k = days[i]
        count += 1
    answer.append(count)
    return answer
