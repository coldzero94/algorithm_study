def solution(s):
    s_list = dict(s)
    print(s_list)
    answer=[]
    blank_num = s_list.count(' ')
    print(blank_num)
    
    for i in range(len(s_list)):
        while s_list[i] == ' ':
            for x in range(len(s_list[i])):
                 if x == 0 or x%2==0:
                    answer.append(s_list[i].upper())
                 elif x%2!=0:
                    answer+=s_list[i]
                 if s_list[x] == ' ':
                     break
        if i == 0 or i%2==0:
            answer.append(s_list[i].upper())
        else:
            answer+=s_list[i]
    answer=''.join(answer)
    return answer

print(solution("try hello world"))