############# FOR LOOPS = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence etc.

#Itterating over a range:

#COUNTING TO TEN
# for x in range(1, 11):
#   print(x)

#COUNTING BACKWARDS
# for x in reversed(range(1,11)):
#   print(x)
# print("Happy New Year!")

#COUNTING WITH GAPS
# for x in range(1,11, 2):
#   print(x)

#COUNTING EVEN NUMBERS
# for x in range(1,11):
#   if x % 2 == 0:
#     print(x)

#COUNTING ODD NUMBERS
# for x in range(1,11):
#   if x % 2 == 1:
#     print(x)

#Iterating over a list:

#PRINTING A LIST
# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

#Iterating over a string:

# credit_card_number = "1322-6544-7665-0008"

# for x in credit_card_number:
#   print(x)

########### CONTINUE and BREAK
#Counting to twenty
# for x in range (1,21):
#   if x == 13:
#     continue # skips 13
#   else: 
#     print(x)

# for x in range (1,21):
#   if x == 13:
#     break # stops at 13 without including it
#   else: 
#     print(x)
    

############# WHILE LOOPS = execute some code WHILE some condition remains True
#ASKING FOR USER NAME
# name = input("Enter your name: ")

# if name == "":
#   print("You didn't enter your name!")
# else:
#   print(f"Hello {name}.")

#Can't continue without typing in their name:
# name = input("Enter your name: ")

# while name == "": #while condition is True, run this block of code forever
#   print("You didn't enter yout name!")
#   name = input("Enter your name: ")

# print(f"Hello {name}.") #when condition is False, this is executed

#INFINITE LOOPS
# name = input("Enter your name: ")

# while name == "": 
#   print("You didn't enter yout name!") #If user doesn't enter their name the first time, they experience an INFINITE LOOP (Ctrl + C: gets you out of the loop.)
#That's why we reprompt the user to type the name. Giving them a chance to escape the INFINTE LOOP.

# age = int(input("How old are you? "))

# while age < 0:
#   print("Age can't be negative") #Now look for a strategy to escape the INFINTE LOOP
#   age = int(input("How old are you? "))# This

# print(f"You are {age} years.")
# age = input("Enter your age: ")

################################################################
# while age == "":
#   print("This object is needed!")
#   age = input("Enter your age: ")

#   age = int(input("Enter your age: "))
#   if age < 0:
#     print("Enter a valid age: ")
#     age = int(input("Enter your age: "))
#   else: 
#     print(f"SO, you are {age} years.")
#################################################################

# while True:
#   try:
#     age = input("Enter your name: ")
#     if age == "":
#       print("Age cannot be empty!")
#       continue
    
#     age = int(age)
#     if age < 0:
#       print("Age cannot be negative!")
#     else:
#       break
#   except ValueError:
#     print("Invalid input. Please enter a valid age.")
# print(f"Your age is: {age}")
####################################################################

# while True:
#   try:
#     age = int(input("Enter your age: "))
#     if age >= 0:
#       break
#     print("Age cannot be negative!")
#   except ValueError:
#     print("Invalid input. Please enter a valid age.")
# print(f"Your age is: {age}")
#####################################################################

#LOGICAL OPERATORS
# food = input("Press 'q' to quit \nEnter your fav. food: ")
# while not food == "q":
#   print(f"You like {food}")
#   food = input("Press 'q' to quit \nEnter your other fav. food: ")
  
# print("Bye")

##################################################################################
# food = input("Press 'q' to quit \nEnter your fav. food: ")

# while food == "q":
#   print("You have quitted!")
#   break
#   if food == "":
#     print("Submit an answer!")
#     food = input("Press 'q' to quit \nEnter your fav. food: ")
#   else:
#     print("Thank you for your submission.")
##################################################################################

#OR OPERATOR
# num = int(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#   print(f"{num} is not valid.")
#   num = int(input("Enter a number between 1 - 10: "))

# print(f"Your number is {num}")
