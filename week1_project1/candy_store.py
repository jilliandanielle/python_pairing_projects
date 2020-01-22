candy_stock = {
    'gummy worms': 456 , 
    'gum':  217, 
    'chocolate bars': 156, 
    'licorice' : 722, 
    'lollipops': 316 }

while True:
    try:
        user_initial = int(input("\nEnter the number of how you would like to proceed:\n1. Check current stock levels.\n2. Candy Sales.\n3. Candy Shipment.\n4. Quit.\n"))
    except ValueError:
        continue

    if user_initial == 1:
    
         # Printing code
        for candy, stock_level in candy_stock.items():
            print(f"\nItem:  {candy.title()}\nStock: {stock_level}")
            

    elif user_initial == 2:
    # User input
        sold_items = input("\nWhich candy item did you sell?\n").lower()
        sold_candy = int(input("\nHow much candy did you sell?\n"))
 
    # Modify the database to reflect the item the user sold
        candy_stock[sold_items] = candy_stock[sold_items] - sold_candy
        
        if candy_stock[sold_items] < 0:
            print("You are out of stock.")       
        else:   
            print(f"\nItem:  {sold_items.title()}\nStock: {candy_stock[sold_items]}")

    elif user_initial == 3:
        shipment = input("\nWhich candy arrived in shipment?\n").lower()
        shipment_number = int(input("\nHow much of that candy did we receive?\n"))
    
        candy_stock[shipment] = candy_stock[shipment] + shipment_number
        
        for candy, stock_level in candy_stock.items():
            print(f"\nItem:  {candy.title()}\nStock: {stock_level}")
    
    # This is for user error   
    else:
        break


