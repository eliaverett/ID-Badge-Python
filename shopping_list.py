shopping_list = []
item = 'none'

print('Please enter the items of the shopping list (type: quit to finish)):')

while item != 'quit':
    item = input('Item:')

    if item != 'quit':
        shopping_list.append(item)

print('The shopping list is: \n')

for i in range (len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

print()
index = int(input('Which item would you like to change?'))
new_item = input("What is the new item?")

shopping_list[index] = new_item

print('The shopping list with indexes is:')

for i in range (len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')

