# #DETECT CAPITAL
# class Solution:
#     def detectCapitalUse(self, word):
#         return (
#             word.isupper() or
#             word.islower() or
#             word.istitle()
#         )
# solution = Solution()
# word = input("Enter a word: ")
# result = solution.detectCapitalUse(word)
# print("Capital usage is correct:", result)


# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     count = {}
#     for char in s:
#         count[char] = count.get(char, 0) + 1
#     for char in t:
#         if char not in count:
#             return False
#         count[char] -= 1
#         if count[char] < 0:
#             return False
#     return True
# s = input("Enter first string: ")
# t = input("Enter second string: ")
# print("Is Anagram:", isAnagram(s, t))


# def climb_stairs(n):
#     if n <= 2:
#         return n
    
#     prev1 = 1
#     prev2 = 2
    
#     for i in range(3, n + 1):
#         current = prev1 + prev2
#         prev1 = prev2
#         prev2 = current
    
#     return prev2

# n = int(input("Enter number of steps: "))
# print("Number of ways:", climb_stairs(n))


# def fizz_buzz(n):
#     result = []
    
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
    
#     return result

# n = int(input("Enter a number: "))
# output = fizz_buzz(n)

# for item in output:
#     print(item)
    
    
    
# def majority_element(nums):
#     candidate = None
#     count = 0

#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += 1 if num == candidate else -1

#     return candidate


# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# print("Majority Element:", majority_element(nums))


# def array_sign(nums):
#     sign = 1

#     for num in nums:
#         if num == 0:
#             return 0
#         if num < 0:
#             sign = -sign

#     return sign

# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# print("Sign of the product:", array_sign(nums))


# def length_of_last_word(s):
#     length = 0
#     i = len(s) - 1

#     # Skip trailing spaces
#     while i >= 0 and s[i] == " ":
#         i -= 1

#     # Count characters of last word
#     while i >= 0 and s[i] != " ":
#         length += 1
#         i -= 1

#     return length


# s = input("Enter a sentence: ")
# print("Length of last word:", length_of_last_word(s))


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
nums1 = list(map(int, input("Enter first array elements: ").split()))
nums2 = list(map(int, input("Enter second array elements: ").split()))
result = intersection(nums1, nums2)
print("Intersection:", result)
