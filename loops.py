#FOR LOOPS
#Loops are used to iterate over a sequence or to repeat certain lines of code
# USED WHEN YOU KNOW HOW LONG YOU WANT THE LOOP TO RUN FOR

#syntax
#for variable in sequence:
  #code block is expected
  #multiple lines of code

# for step in range(10): #for sequences, it starts from 0 when indexing until the stop index
#   print(f"Step {step}")

# for step in range(1,10): #for sequences, using the indexing in range until the stop index
#   print(f"Step {step}")

# for step in range(4,10,2): #for 2, this means its skips every 2 indices until the stop index
#   print(f"Step {step}")

# for step in range(4,10,3): #for 3, this means its skips every 2 indices until the stop index
#   print(f"Step {step}")

# for character in "Python":
#   print(character)
  
# for character in range(20):
#   if (character % 2 == 0): #displays even numbers
#     character += 2
#     print(character) #prints only even numbers
#   # else:
#   #   print(character) #prints all numbers
  

# WHILE LOOPS
#a while loop runs as long as a certain condition is True.
# USED WHEN YOU don't KNOW HOW LONG YOU WANT THE LOOP TO RUN FOR

#syntax
# mark = 5
# # while (mark < 10): #read as: As long as mark is less than 10, please execute code in the block below
# #   print("Yeah, i'm less than 10") #an infinite loop is created
  
# while (mark < 10): 
#   print(f"Yeah, {mark} i'm less than 10") 
#   mark = mark + 1

# break and continue statements

# mark = 5
# while (mark < 10):
#   print("Hello")
#   if mark == 7:
#     break
#     mark = mark + 1
    
# mark = 5
# while (mark < 10):
#   print("Hello")
# #   break # if condition = TRUE, break is applied

# #Continue statements
# for char in "Python":
#   if char == 't': #skip 't' and go to the next one
#     continue
#   print(char)

# mark = 5
# while (mark < 10):
#   if mark == 7:
#     continue  # tiny infinte loop since mark = 7 forever, the code below is not executed
#   print(f"{mark}") 
#   mark = mark + 1

# mark = 5
# while (mark < 10):
#   mark = mark + 1
#   if mark == 7:
#     continue  # tiny infinte loop since mark = 7 forever, the code below is not executed
#   print(f"{mark}") 
# # print("GWE")

#EXERCISE 1
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# num4 = int(input("Enter a number: "))
# num5 = int(input("Enter a number: "))
# sum = num1 + num2 + num3 + num4 + num5
# print(sum)

# #exercise 2
# numb = 0
# finish = "Done"
# print(" NB: When done, type the word 'Done'.")
# while numb < 6:
#   numb = numb + 1
#   num = int(input("Enter a number: "))
#   num += num
#   print(sum)
#   if 
#     finish = input("Done: ")
#   break

# sum = 0
# while True: 
#   user_input = input("Enter a number of your choice: \nEnter done to quit: ").title().strip()
#   if user_input == "Done":
#     break
#   else:
#     sum += int(user_input)
# print(f"Total sum: {sum}")

# Write a program where a user enters numbers, and the program sums them up.
# The loop stops when the user enters "done."

# Write a program that asks the user to enter 5 numbers, one at a time, and then prints their sum.
# Create a program that asks for two numbers and then prints all even numbers between them (inclusive).

# Create a guessing game where the user has to guess a secret number.
# The loop ends when the correct number is guessed.

# Question 2:
# Create a program for a delivery service that determines shipping status and cost.
# Conditions:
# - If distance < 5km:
#   * If weight < 2kg: $5 delivery fee
#   * If weight 2-5kg: $8 delivery fee
#   * If weight > 5kg: $12 delivery fee
# - If distance 5-10km:
#   * If weight < 2kg: $8 delivery fee
#   * If weight 2-5kg: $12 delivery fee
#   * If weight > 5kg: $15 delivery fee
# - If distance > 10km:
#   * Add $5 to all above rates

# Also check if:
# - If it's raining: Add $2 surcharge
# - If it's a holiday: Add 20% to final price
#
# Write a program that calculates delivery fee based on these conditions.

# Smartphone Installment Payment Eligibility System
# Question:
# Create a program that determines if a customer can buy a phone on installments. Use these rules:

# Base eligibility:

# Credit score must be ≥ 650
# Monthly income ≥ $2500
# Must check last 6 months of payment history


# If eligible, determine interest rate & term:

# Credit score ≥ 750: 5% interest, up to 24 months
# Credit score ≥ 700: 8% interest, up to 18 months
# Credit score < 700: 12% interest, 12 months only


# Additional rules:

# For each month employed beyond 6 months, allow one extra month of payment term
# Maximum late payments allowed: 1
# Down payment reduces final monthly payment
# Maximum 2 existing loans allowed has context menu