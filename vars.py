t = 9
name = 'Mr. T'
animal = 'lion'


d = vars().copy()


for k, v in d.items():
    if "__" not in k:
        print(k, ':', v)
print(d['__name__'])