def solution(my_string, overwrite_string, s):
    s = int(s)
    answer = my_string[0:s]+overwrite_string+my_string[s+len(overwrite_string):len(my_string)]
    return answer