def solution(n):
    num_list = str(int(n))
    sort_list = sorted(num_list,reverse=True)
    aanswer = ''.join(map(str,sort_list))
    answer = int(aanswer)
    return answer

print(solution(23421))