print("Mr. Eliot, Good Evening?")
bill = int(input("What is your bill value? "))
print(type(bill))
if bill > 200:

  discount = bill * 0.2                   #Mr. Eria's qn: Why does this produce a float?
  new_bill = bill - discount
  print(f" :) Discount of {discount} applied.")
  print(f"New bill: ${new_bill}")
if 100 <= bill <= 200:
  discount = bill * 0.1                   #Mr. Eria's qn: Why does this produce a float?
  new_bill = bill - discount
  print(f" :) Discount of {discount} applied.")
  print(f"New bill: ${new_bill}")
  card = input("Do you have a loyalty card?(Yes/No) ").title().strip()
  cj = bill * 0.05
  if card == "Yes":
    extra_discount = bill * 0.25
    new_bill = bill - extra_discount
    print(f" :) Discount of {cj} applied.")
    print(f"New bill: ${new_bill}")
  else: 
    print("OK")
    print(f":( Discount of ${cj} not applied since you lack a loyalty card!")
    print(f'New bill: "${new_bill}".')
  today = input("What day is it? ").title().strip()
  hakim = bill * 0.02
  round_bill = round(new_bill)
  if today == "Tuesday":
    final_discount = bill * 0.27
    new_bill = bill - final_discount
    print(f" :) Discount of {hakim} applied.")
    print(f"New bill: ${new_bill}")
  else:
    print(f":( Discount of {hakim} not applied as today isn't Tuesday, our special day!")
    print(f"New bill: ${new_bill}.")
  print(f"Thank you for coming, your new bill is ${round_bill}!")

else: 
  print(""":( No discounts applied, 
          BUT 
Thank you and come again.""")
  print(f"Your Bill: ${bill}!")