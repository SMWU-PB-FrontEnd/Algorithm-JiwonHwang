def solution(a, b):
    a_fir = str(a)+str(b)
    b_fir = str(b)+str(a)
    if (int(a_fir) >= int(b_fir)) :
        answer = int(a_fir)
    else : answer = int(b_fir)
    return answer