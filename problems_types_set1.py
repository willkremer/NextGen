print(int(2.9))

a = 3
b = 5
c = 7
print (a < b and b < c) or (a>b and b>c)
print (a <b <c or a>b>c)

year = random.randint(1000,2018)
#use % if year is divisibleby 4
# unless its divisible by 100
#its ok to be divisible by 100
#if also divisible by 400
print('was', year, 'a leap yer')
print((year % 4 == 0) and (year % 100!= 0 or year % 400 == 0))

print(random.choice(('dog','cat','bird')))