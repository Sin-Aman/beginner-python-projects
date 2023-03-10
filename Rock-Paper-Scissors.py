# my version of Rock-Paper-Scissors

import random
# print user name and welcome
user_name = input("What is your name?")
print("Welcome,", user_name, "!")
print()

# pick choices 
print("Ready for Rock-Paper-Scissors? Choose as you desire!!")
user_choice = input("Which one do you choose? (rock/paper/scissors):")
comp_choice = random.choice(["rock","paper","scissors"])
print()

# print both picked choices 
print("You chose", user_choice)
print("I chose", comp_choice)
print()

# the main brain 
if user_choice == "rock":

  if comp_choice == "rock":
    print("Aargh! We tied (but I will get you next time!)")
  elif comp_choice == "paper":
    print("FATALITY!! I WIN! My paper slashed your rock!")
  else:
    print('Alack! Your rock broke my scissors.')

elif user_choice == 'paper':

  if comp_choice == "scissors":
    print("FATALITY!! I WIN! My scissors cut your paper)")
  elif comp_choice == "paper":
    print("Aargh! We tied")
  else:
    print('Alack! Your paper wrapped my rock.')

elif user_choice == 'scissors':

  if comp_choice == "scissors":
    print("Aargh! We tied")
  elif comp_choice == "paper":
    print("Alack! Your scissors cut my paper.")
  else:
    print('FATALITY!! I WIN! My rock smashed your scissors.')

else:

  print("You have ventured into the unknown...")
  print("... but I probably won!!")

print()
print("Lets do it again!")