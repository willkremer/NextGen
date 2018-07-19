
things = ['camera', 'couch', 'potato salad', 'energy drink', 'comb', 'suitcase']
prices = [50, 100, 5, 5, 1, 25]

for t in (0, 1, 2, 3, 4, 5):
    print('{0:>12} ${1:>7.2f}'.format(things[t], prices[t]))

