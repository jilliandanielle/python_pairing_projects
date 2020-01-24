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
    
    def print_stock(candy_stock):
        for candy, stock_level in candy_stock.items():
            print(f"\nItem:  {candy.title()}\nStock: {stock_level}")
        return None
    
    def receive_shipment(candy_stock, sold_items, sold_candy):
        candy_stock[sold_items] = candy_stock[sold_items] - sold_candy
        if candy_stock[sold_items] < 0:
            print("You are out of stock.")
        return candy_stock
    
    def record_sales(candy_stock, shipment, shipment_number):
        candy_stock[shipment] = candy_stock[shipment] + shipment_number
        # for candy, stock_level in candy_stock.items():
        return candy_stock
    
    if user_initial == 1:
        print_stock(candy_stock)

    elif user_initial == 2:
        sold_items = input("\nWhich candy item did you sell?\n").lower()
        sold_candy = int(input("\nHow much candy did you sell?\n"))
        candy_stock = receive_shipment(candy_stock, sold_items, sold_candy)

    elif user_initial == 3:
        shipment = input("\nWhich candy arrived in shipment?\n").lower()
        shipment_number = int(input("\nHow much of that candy did we receive?\n"))
        candy_stock = record_sales(candy_stock, shipment, shipment_number)

    else:
        break

