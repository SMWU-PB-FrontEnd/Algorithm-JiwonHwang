def solution(myString, pat):
    answer = myString.replace('A', 'a').replace('B', 'A').replace('a','B')
    return int(pat in answer)