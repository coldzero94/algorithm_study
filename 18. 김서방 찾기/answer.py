def solution(seoul):
    answer1 = '김서방은'
    answer2 = '에 있다'
    find_kim = 'Kim'
    last_name = [i for i in range(len(seoul)) if find_kim in seoul[i]]
    return answer1+" "+str(last_name[0])+answer2