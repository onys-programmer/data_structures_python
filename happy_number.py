# 과제 4번 코드란
from functools import reduce

# 81이면 [8, 1]을 반환
def get_each_number(n):
    return [int(i) for i in str(n)]

def solution(n):
    arr = []

    # 중복된 값이 나올 때, 혹은 1이 나올 때까지 재귀호출
    def helper(num):
        each_number = get_each_number(num)
        sum = reduce(lambda acc, cur: acc + cur**2, each_number, 0)
        
        if sum == 1:
            return True
        if sum in arr:
            return False
        
        arr.append(sum)

        return helper(sum)

    return helper(n)

# Test code
print(solution(19))  # True
print(solution(61))  # False
