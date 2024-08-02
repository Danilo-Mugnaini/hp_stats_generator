print("⚔️ Character Stats Generator ⚔️")

char1Name = input("\nName your warrior 1: ").upper()
char2Name = input("\nName your warrior 2: ").upper()
char3Name = input("\nName your warrior 3: ").upper()
sides = int(input("\nHow many sides does your dice have? "))


def rollDiceAny(sides):
  import random
  roll = random.randint(1, sides)
  print("You rolled", roll)
  return roll


def rollDices():
  import random
  rollSix = random.randint(1, 7)
  rollEight = random.randint(1, 9)
  return rollSix * rollEight


sides = rollDiceAny(sides)
print("\n⚔️ Character Stats ⚔️")

haveAChar = "yes"

while haveAChar == "yes" or haveAChar == "y":
  char1Health = rollDices()
  char2Health = rollDices()
  char3Health = rollDices()
  print("\n|", char1Name, "|", "|", char1Health, "HP |")
  print("\n|", char2Name, "|", "|", char2Health, "HP |")
  print("\n|", char3Name, "|", "|", char3Health, "HP |")
  haveAChar = input("\nWant to create another 3 warriors? ")

print("\nMay your name go down in Legend...")
print("Thanks for playing!")
