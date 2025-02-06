#Create a program that asks for two numbers and then prints all even numbers between them (inclusive).

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

for num in range(num1,num2+1): #the +1 added 20 to the list: Joshua & guess work at their best :)
  if num % 2 == 0:
    print(f"{num} - even")
  else:
    print(num)