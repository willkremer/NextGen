residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
print(residents['Sloth'])

menu = {}
menu['sunday'] = 16.78
menu['monday'] = 3
menu['tuesday'] = 0
for key in menu:
    print(key, ':', menu[key])

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Children Zoo Area'

for k in zoo_animals:
    print(k, ':', zoo_animals[k])


webster = {"Aardvark" : "A star of a popular children's cartoon show.",
"Baa" : "The sound a goat makes.",
"Carpet": "Goes on the floor.",
"Dab": "A small amount."}
for k in webster:
    print(k, ':', webster[k])

my_dict={'title':'Stranger Things', 'is_show':True, 'seasons':2}
print(my_dict.items())
for k,v in my_dict.items():
    print(k, ':', v)