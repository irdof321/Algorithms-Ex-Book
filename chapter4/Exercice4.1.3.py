import time
import random

def brutForce(array):
    max_sum = - float("inf")
    index = (0, 0)
    for i in range(len(array)):
        for j in range(i, len(array)):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += array[k]
            if current_sum > max_sum:
                max_sum = current_sum
                index = (i, j)
                
    return max_sum, index

def FindMaxSubArray(array):
    if len(array) == 1:
        return array[0], (0, 0)
    else:
        mid = len(array) // 2
        left_sum, left_index = FindMaxSubArray(array[:mid])
        right_sum, right_index = FindMaxSubArray(array[mid:])
        cross_sum, cross_index = FindMaxCrossingSubArray(array)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum, left_index
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum, right_index
        else:
            return cross_sum, cross_index
        
def FindMaxCrossingSubArray(array):
    mid = len(array) // 2
    left_sum = - float("inf")
    sum = 0
    left_index = mid
    right_index = mid + 1
    for i in range(mid, -1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i
    right_sum = - float("inf")
    sum = 0
    for j in range(mid + 1, len(array)):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum
            right_index = j
    return left_sum + right_sum, (left_index, right_index)

def FindMaxSubArrayLinear(array):
    max_sum = - float("inf")
    current_sum = 0
    index = (0, 0)
    for i in range(len(array)):
        current_sum += array[i]
        if current_sum > max_sum:
            max_sum = current_sum
            index = (index[0], i)
        if current_sum < 0:
            current_sum = 0
            index = (i + 1, i + 1)
    return max_sum, index

if __name__ == "__main__":
    # Test time of computation for both methods 

    array = [random.randint(-100, 100) for i in range(1000)]
    
    t0 = time.time()
    brutForce(array)
    t1 = time.time()
    print("Time of computation for brut force method: ", t1 - t0, "The result is: {0}".format(brutForce(array)))
    
    t0 = time.time()
    FindMaxSubArray(array)
    t1 = time.time()
    #need more decimal
    print("Time of computation for divide and conquer method: {0:.5f}" .format(t1 - t0)
          , "The result is: {0}".format(FindMaxSubArray(array)))
    
    t0 = time.time()
    FindMaxSubArrayLinear(array)
    t1 = time.time()
    
    print("Time of computation for linear method: {0:.5f}" .format(t1 - t0), "The result is: {0}".format(FindMaxSubArrayLinear(array)))
    
