# def prefixFreePhones(numbers):
#     # overall runtime is O(n^2)
#     # for each number in numbers: 
#     for num in numbers: # O(n)
#     # compare it to every other number: 
#         for other_num in numbers:   # O(n)
#             # if one of the numbers if a prefix of the other
#             if num == other_num:
#                 continue
#             if other_num.startswith(num) or num.startswith(other_num): 
#             # return true
#                 return False
#     return True
def prefixFreePhones(numbers):
    # what if we sort numbers first? 
    # numbers is a list of strings, so it's going sort alphabetically
    # ["911", "9112345", "9876543"]
    # overall runtime : O(n log n)
    # sort
    numbers.sort()      # O(n log n)
    # iterate through
    for i in range(len(numbers) - 1):       # O(n)
    # compare each element with the one right after it
        first = numbers[i]
        second = numbers[i+1]
    # if the second element starts with the first, return false
        if second.startswith(first):
            return False
    return True
    # otherwise return True