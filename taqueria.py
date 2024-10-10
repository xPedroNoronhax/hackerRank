menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


menu_lower = {}

for item in menu:
    menu_lower[item.lower()] = menu[item]

total = 0

while True:
    try:
        item = input("Item: ").lower()
        if item in menu_lower:
            total += menu_lower[item]
            print(f"Total ${total:.2f}")
        else:
            continue
    except EOFError:
        break




