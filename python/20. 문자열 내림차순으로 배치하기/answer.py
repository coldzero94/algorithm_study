# def solution(s):
#     ord_list = []
#     chr_list = []
#     for i in range(len(s)):
#         ord_list.append(ord(s[i]))
  
#     for i in range(len(ord_list)):
#         chr_list.append(chr(sorted(ord_list,reverse=True)[i]))
#     answer = ''.join(chr_list)
    
#     return answer

# print(solution('asdf'))


def solution(s):
    return ''.join(sorted(s, reverse=True))
print(solution('asdfg'))