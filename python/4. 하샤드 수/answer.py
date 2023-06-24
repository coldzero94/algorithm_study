def solution(x):
    test_x = str(x)
    sum_number = 0

    for i in range(len(test_x)):
        sum_number += int(test_x[i])

    if x%sum_number == 0:
        return True
        
    else:
        return False