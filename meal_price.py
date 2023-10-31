#In this code, I added a couple fun things to play around with to make this more of an all around restauraunt arrangement code. I added if anyone would need baby seats, and cost of appetizers and drinks. 
childs_meal= float(input("What is the price of a child's meal?"))
adult_meal = float(input("What is the price of an adult's meal?"))
appetizers = float(input("What is the price of appetizers?"))
drinks = float(input("What is the price of drinks other than water?"))
cost_appetizers = int(input("How many people ordered appetizers?"))
cost_drinks = int(input("How many people ordered drinks?"))
children = int(input("How many children are there?"))
adults = int(input("How many adults are there?"))
baby_seats = int(input("How many babies will need high chairs?"))

print()

subtotal = (childs_meal * children) + (adult_meal * adults) + (cost_appetizers * appetizers) + (cost_drinks * drinks)

print(f'{baby_seats} high chairs will be needed for this table.')


print(f'subtotal: ${subtotal:.2f}')

tax_percentage = float(input("What is the sales tax rate (in percentage)?"))

tax_decimal = tax_percentage / 100

tax = subtotal * tax_decimal
print(f'tax: ${tax:.2f}')


total = subtotal + tax
print(f'total: ${total:.2f}')

payment = float(input("What is the payment amount?"))
change = payment - total
print(f'change: ${change:.2f}')

