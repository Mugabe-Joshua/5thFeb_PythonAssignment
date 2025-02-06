# Write a program that asks the user to enter 5 numbers, one at a time, and then prints their sum.

numb = int(input("Enter a number: "))
suma = numb
num = 1
print(num)
while num < 5:
  num += 1
  numb = int(input("Enter a number: "))
  print(num)
  suma += numb

print(f"{suma} is your total!")