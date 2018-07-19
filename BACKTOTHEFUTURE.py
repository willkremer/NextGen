import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# Open file
with open('/Users/estherkremer/Desktop/BACK TO THE FUTURE.txt', 'r') as file:
    text = file.read()
# Make lowercase
text = text.lower()
# Turn into a list
tlist = text.split()
# Print how many words
print(len(tlist))
