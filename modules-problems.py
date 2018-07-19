import random
# create secret number
secret_number = random.randint(0, 10)
# get users guess
print(int(input("guess a number between 1 and 10")) ==secret_number)
# compare
print("the number was", secret_number)

import statistics
ages = (18, 20, 21, 17, 15, 16, 20, 18, 21, 17, 22, 14, 20)
print(statistics.median(ages))
print(statistics.mode(ages))

print("how old are you")
age = input()
age = int(age)
if age >= 18 :
    # show news
    news = "riots on the streets."
    print(news)
else:
    # show sorry message
    print("Sorry, you are too young! This Website contains mature content and can only be accessed if over the age of 18")






