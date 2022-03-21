def solution(n):
    answer = []
    # reverse_num=rever.str(n)
    num_list=list(map(int,reversed(str(n))))
    
    return num_list

print(solution(12345))