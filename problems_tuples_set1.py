#1
# text = "how are you today good sir? I hope you are well."
#
# text = text.replace('?', '')
# text = text.replace('.', '')
# text_tuple = tuple(text.split())
# print(text_tuple)
# print('there are', len(text_tuple), 'words')
#2
# names = ('kathy', 'benji', 'ian', 'alejandro')
# for n in names:
#     print(len(n))

#3
# import random
# firstnames = ('bryan', 'eva', 'elliot', 'jared', 'will', 'sophia')
# lastnames = ('doyle', 'floyd', 'reid', 'webb', 'collier', 'ward')
# num_names = int(input("how many names"))
# for n in range(num_names):
#     print(random.choice(firstnames), random.choice(lastnames))

#4
# import random
# import time
# comp_num = random.randint(1, 10)
# print("Think of a random number between 1 and 10. I'm going to guess.")
# time.sleep(1)
# print("Ready?")
# time.sleep(1)
# print("Ok.")
# time.sleep(1)
# print("Is it", comp_num, "?")
# computer_guess = random.randint(1,10)
# answer = input("is it" + str(computer_guess),"?")
# turn = 1
# old_guesses = ()
# player_answer = input()
# while player_answer == "no":
#     comp_num = random.randint(1, 10)
#     old_guessses = old_guesses + (computer_guess,)
#     print("Is it", comp_num, "?")
#     player_answer = input()
# print ('you win')

#set 2 #1
import random
correct_guesses = ()
word = random.choice(('dog', 'bird', 'truck'))
for w in word:
    print("_ ", end=' ')
print()
letter = input("guess a letter")
letter = letter.lower()
if letter in word:
    print("good guess")
    correct_guesses += (letter,)
else:
    print('horrible guess')
print(correct_guesses)
for w in word:
    if w in correct_guesses:
        print(w, end='')
    else:
        print('_ ', end='')
while len(word) > len(correct_guesses):
    letter = input("\nguess a letter")
    letter = letter.lower()
    if letter in word:
        print("good guess")
        correct_guesses += (letter,)
    else:
        print('horrible guess')
    print(correct_guesses)
    for w in word:
        if w in correct_guesses:
            print(w, end='')
        else:
            print('_ ', end='')

