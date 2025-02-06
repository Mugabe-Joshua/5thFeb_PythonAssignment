# Write a program where a user enters numbers, and the program sums them up.
# The loop stops when the user enters "done."

# num = input("Type 'done' to exit \nEnter a number: ")
# sum = num
# while not num == "done":
#   print(f"Number = {num}")
#   num = input("Enter a number: ")
#   _sum += int(num)

# print(f"Total = {_sum}")
num = []

while True:
  i = input("TYPE 'done' TO QUIT\n Enter a number: ").strip()
  if i.lower() == "done":
    break
  else:
    num.append(int(i))
print(sum(num))