Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0 
Slytherin = 0 


print("Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer = int(input("1 or 2?: "))

if answer == 1:
  Gryffindor = Gryffindor +1
  Ravenclaw = Ravenclaw +1
elif answer == 2:
  Hufflepuff = Hufflepuff +1
  Slytherin = Slytherin +1
else: 
  print("Wrong input.")

print("When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer = int(input("Pick a number: "))

if answer == 1:
  Hufflepuff = Hufflepuff +2
elif answer == 2:
  Slytherin = Slytherin +2
elif answer == 3:
  Ravenclaw = Ravenclaw +2
elif answer == 4:
  Gryffindor = Gryffindor +2
else: 
  print("Wrong input.")

print("Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer = int(input("Pick a number: "))

if answer == 1:
  Slytherin = Slytherin +4
elif answer == 2:
  Hufflepuff = Hufflepuff +4
elif answer == 3:
  Ravenclaw = Ravenclaw +4
elif answer == 4:
  Gryffindor = Gryffindor +4
else: 
  print("Wrong input.")

print("Slytherin: " + str(Slytherin))
print("Hufflepuff: " + str(Hufflepuff))
print("Gryffindor: " + str(Gryffindor))
print("Ravenclaw: " + str(Ravenclaw))

