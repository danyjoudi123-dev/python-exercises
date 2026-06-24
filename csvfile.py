import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try: 
     with open('packing_list.csv', mode = 'r', newline='', encoding='utf-8') as file:
        filereader = csv.reader(file)
        for row in filereader:
            print(row)
except FileNotFoundError:
    print('Packing list file not found. Creating a new one.')
    with open('packing_list.csv', mode = 'w', newline='', encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerows(data)

        

