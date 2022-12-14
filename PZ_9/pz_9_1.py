dict = {'cat':'кот', 'car':'машина', 'kitten':'котик', 'sky':'небо', 'honey':'мед', 'candy':'конфета','ice cream':'мороженое','juice':'сок', 'dog':'собака', "puppy":'щенок', 'star':'звезда'}
dictrus = {j: i for i, j in dict.items()}
n = input()
try:
    print(dict[n])
except KeyError:
    try:
        print(dictrus[n])
    except KeyError:
        print('Данного слова нет в словаре')