def solution(s):
    p = s.count('p')
    p2 = s.count('P')
    y = s.count('y')
    y2 = s.count('Y')
    if (p+p2) == (y+y2):
        return True
    if (p+p2) != (y+y2):
        return False

# from collections import Counter
# def numPY(s):
#     # 함수를 완성하세요
#     c = Counter(s.lower())
#     return c['y'] == c['p'] 