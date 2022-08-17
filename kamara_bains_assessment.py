#ALGORITHMS QUESTION 1 
# def isValidSubsequence(array, sequence):
#     s_index = 0
#     for x in array:
#         if s_index == len(sequence):
#             break
#         if s_index == x:
#             s_index += 1
#     return s_index == len(sequence)

#array1 = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence1 = [1, 6, -1, -2]
# print(isValidSubsequence(array1, sequence1))  # FALSE

# array2 = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence2 = [1, 6, -1, 10]
# print(isValidSubsequence(array2, sequence2))  # TRUE

# array3 = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence3 = [25]
# print(isValidSubsequence(array3, sequence3))  # TRUE

# array4 = [4, 8, 23, 12, 17, 9, 20, 22]
# sequence4 = [8, 12, 17, 22]
# print(isValidSubsequence(array4, sequence4))  # TRUE



#ALGORITHMS QUESTION 2 ATTEMPT 1
def findThreeLargestNumbers(array):
#     array.sort()
#     return [array[-3:]]
#ALGORITHMS QUESTION 2 ATTEMPT 2
# def findThreeLargestNumbers(array):
#     array = insertion_sort(array)
#     return array[-3:]

# def insertion_sort(arr):
#     for i in range(len(arr)):
#         cursor = arr[i]
#         pos = i

#         while pos > 0 and arr[pos - 1] > cursor:
#             arr[pos] = arr[pos - 1]
#             pos = pos - 1
#         arr[pos] = cursor

#     return arr

#ALGORITHMS QUESTION 2 ATTEMPT 3

    def findThreeLargestNumbers(array):
        x = 0
        y = 0
        z = 0
        for num in array:
              if num > x:
                  z = y
                  y = x
                  x = num
        return [x,y,z]

print(findThreeLargestNumbers(array1))
array1 = [141, 1, 17, -17, -27, 18, 541, 8, 7, 7]
expectedOutput1 = [18, 141, 541]
print(str(findThreeLargestNumbers(array1)) +
      " <-- --> " + str(expectedOutput1))  # [18, 141, 541]

array2 = [141, 1, 214, -17, -27, 0, 541, 21, 7, 34]
expectedOutput2 = [141, 214, 541]
print(str(findThreeLargestNumbers(array2)) + " <-- --> " +
      str(expectedOutput2))  # [141, 214, 541]

array3 = [139, 15, 19, -25, -10, 18, 341, 8, 1, 7, 1000]
expectedOutput3 = [139, 341,1000]
print(str(findThreeLargestNumbers(array3)) +
      " <-- --> " + str(expectedOutput3))  # [18, 141, 541]