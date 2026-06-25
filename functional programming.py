import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

capital_names = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [create_fantasy_name(prefixes, capital_names) for _ in range(10)]

def fire_in_name(name):
    return 'Fire' in name

def concatenate_names(name1, name2):
    return name1 + name2

firename = list(filter(fire_in_name, random_names))
concatenatednames = reduce(concatenate_names, firename) if firename else ''

def display_name_info():
    print('Fantasy Names:')
    for name in random_names:
        print(name)

    print('Filtered names with "Fire": ' + str(firename))
    print('Concatenated names: ' + concatenatednames)

display_name_info()


