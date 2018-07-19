def find_max(num1, num2, num3):
   ''
   Return the max of 3 nums.
   :param num1:
   :param num2:
   :param num3:
   :return:
   ''
   return max((num1, num2, num3))

def find_sum(a):
   total = 0
   for x in a:
       total += x
   return total

def find_product(b):
   total = 1
   for x in b:
       total *= x
   return total

def reverse(c):
   d = ''
   c = 'kitty'
   for x in range(len(c) - 1,-1, -1):
       d += c[x]
   return d

def factorial(f):
   if f == 0:
       return 1
   else:
       return f * factorial(f-1)

Message Input

Message #general