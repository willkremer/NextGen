import random
main_course = ['steak', 'salmon', 'rice']
main_course.insert(0, 'stew')
main_course.insert(4, 'burger')
main_course.insert(5, 'tilapia')
main_course.insert(6, 'gulash')
print(main_course)
sides = ['carrots', 'fries', 'salad']
style = ['seared', 'boiled', 'baked', 'fried']
print("Tonight I will serve", random.choice(style), random.choice(main_course), 'with', random.choice(sides))

# problem = input('enter a problem, example 1 + 2')
# plist = problem.split()
# print(plist)
# a = int(plist[0])
# b = int(plist[2])
# operator = plist[1]
# if operator == '+':
#     print(a + b)
# elif operator == '-':
#     print(a - b)
# elif operator == '*':
#     print(a * b)
# elif operator == '/':
#     print(a / b)
# else:
#     print('operator unknown')

#set 2
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1, 2, 3]))

def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1, 2, 3]))

list = [random.randint(0, 100) for x in range(20)]
print(list)
min = list[0]
for x in list:
    if x < min:
        min = x
print("the smallest num is", min)

list = ['plug', 'phone', 'bottle', 'water', 'computer', 'key', 'bob']
total = 0
for w in list:
    if len(w) >= 2 and w[0] == w[-1]:
        total = total + 1

print(total)
