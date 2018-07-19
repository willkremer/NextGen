# import random
# file = open('/Users/estherkremer/Desktop/harrypotter.txt', 'r')
# text = file.read()
# print(text)
# file.close()
# with open('/Users/estherkremer/Desktop/harrypotter.txt', 'r') as file:
#     text = file.read()
# print(text[:100])
#
# # s = text
# # text = text.lower
# # s_list = s.split
# # print(s_list)
# # print(len(s_list))
# # set_list = set(s_list)
# # print(len(set_list))
#
# with open('/Users/estherkremer/Desktop/harrypotter.txt', 'r') as file:
#     text = file.read()
# text = text.replace(',', '')
# text = text.replace
# print(len(set(tlist)))
# unique_list = list(set(tlist))
# print(random.choice(tlist))
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
import random

# Open file
with open('/Users/estherkremer/Desktop/harrypotter.txt', 'r') as file:
   text = file.read()

# Make lowercase
text = text.lower()

# Remove punctuation
# text = text.replace(',', '')
# text = text.replace(':', '')
# text = text.replace('.', ')'
# text = text.replace(‘?’,'')
# text = text.replace(‘)’,'')
# text = text.replace(‘(’,'')
# text = text.replace(‘“’,'')
# text = text.replace(‘!’,'')
# text = text.replace(‘;’,'')
# text = text.replace(‘-’,' ’)
# text = text.replace(“‘s”,’ ’)
# text = text.replace(“‘t”,'')

# Turn into a list
tlist = text.split()

# Print how many words
print(len(tlist))

# How "any times Harry appears
print("Harry appears:", tlist.count('harry'))

# Print how many unique words
print("Unique word count:", len(set(tlist)))

unique_list = list(set(tlist))  # turn the unique set to a list

rword = random.choice(unique_list)
print("Random word:", rword, 'apears', tlist.count(rword), "time(s).")

plt.bar(['total words', 'unique words'], [len(tlist), len(unique_list)])
plt.show()

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()
