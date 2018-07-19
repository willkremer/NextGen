# def make_double(a):
#     dbl = a * 2
#     return dbl
# def make_half(a):
#     h = a/2
#     return h
# def make_plural(word):
#     return word + 's'
# def get_power(base, exp):
#     return pow(base, exp)
#
# print(get_power(8,2))
#
# print(make_plural('hat'))
# b = make_double
# print(b)
# b = make_half(5)
# print(b)
#
# def find_max(num1, num2, num3):
#     return max((num1, num2, num3))
# print(find_max(1, 2, 3))
#
# def sum(nums):
#     total = 0
#     for n in nums:
#         total += n
#     return total
# print(sum((8, 2, 3, 0, 7)))
#
# def multiply(nums):
#     total = 1
#     for n in nums:
#         total *= n
#     return total
# print(multiply((8, 2, 3, -1, 7)))
#
#
# def string_reverse(str1):
#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("put in a number : "))
# print(factorial(n))
#
# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)
#
# def count_upper_lower(word):
#     count_uppers = 0
#     count_lowers = 0
#     for w in word:
#         if w == w.lower():
#             count_lowers += 1
#         else:
#             count_uppers +=1
#         return (count_uppers, count_lowers)
# t = count_upper_lower("Katie")
# print("the upper count is", t[0], ", the lower count is", t[1])


def get_weight(weight, planet='earth'):
    if planet == 'earth':
        return weight
    elif planet == 'mercury':
        return weight * .38
    elif planet == 'venus':
        return weight * .91
    elif planet == 'mars':
        return weight * .38
    elif planet == 'jupiter':
        return weight * 2.34
    elif planet == 'saturn':
        return weight * 1.06
    elif planet == 'uranus':
        return weight * .92
    elif planet == 'neptune':
        return weight * 1.19

print(get_weight(130), "weight")
print(get_weight(130, planet='mercury'), "weight")