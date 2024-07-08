def solution(myString, pat):
    answer = myString.replace('A', 'a').replace('B', 'A').replace('a','B')
    if answer.find(pat) >= 0 :
        return 1
    else : return 0