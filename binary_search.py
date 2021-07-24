def binary_search(data, target):
    if len(data) == 0:
        return False
    if len(data) == 1:
        return True if target == data[0] else False
    
    medium = len(data) // 2
    if target == data[medium]:
        return True
    else:
        if target > data[medium]:
            return binary_search(data[medium+1:], target)
        else:
            return binary_search(data[:medium], target)
    

# 과제1번 코드란
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 20

def searchMatrix(matrix, target):
    for ele in matrix:
        if binary_search(ele, target) == True:
            return True

    return False

print(searchMatrix(matrix, target))
