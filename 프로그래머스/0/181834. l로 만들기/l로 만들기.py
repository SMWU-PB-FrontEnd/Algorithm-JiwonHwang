def solution(s):
    table = s.maketrans('abcdefghijk', 'lllllllllll')
    return s.translate(table)
    
            