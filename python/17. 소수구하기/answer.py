
import math

def solution(number):
    numbers = [True] * (number + 1)
    answer = 0

    for num in range(2,int(math.sqrt(number))+1):
        if numbers[num] == False:
            continue;

        for i in range(num+num,number+1,num):
            numbers[i] = False

    for i in range(2,number+1):
        if numbers[i] == True:
            answer+=1

    return answer
    # 아래는 틀린 
# def solution(n):
#     answer = 0
#     blank_list = []
#     for i in range(1,n+1):
#         if i==2 or i==3 or i==5 or i==7:
#             blank_list.append(i)
#         elif i%i == 0 and i!=1 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#             blank_list.append(i)
#     answer = len(blank_list)
#     return answer