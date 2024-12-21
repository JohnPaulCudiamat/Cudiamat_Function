def display_menu():
    """Function to display the food menu with prices."""
    menu = {
        1: {'item': 'Burger', 'price': 5.50},
        2: {'item': 'Pizza', 'price': 8.75},
        3: {'item': 'Pasta', 'price': 7.00},
        4: {'item': 'Salad', 'price': 4.25},
        5: {'item': 'Soda', 'price': 1.50}
    }
    
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value['item']} - ${value['price']}")
    return menu

def get_order(menu):
    """Function to get the user's order selection."""
    while True:
        try:
            choice = int(input("Please select an item number (1-5): "))
            if choice in menu:
                return menu[choice]['item'], menu[choice]['price']
            else:
                print("Invalid selection. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def process_payment(total_cost):
    """Function to process payment and handle insufficient funds."""
    while True:
        try:
            cash = float(input(f"Total amount due is ${total_cost}. Enter cash rendered: $"))
            if cash >= total_cost:
                change = cash - total_cost
                return cash, change
            else:
                print("Insufficient payment. Please provide enough cash.")
        except ValueError:
            print("Invalid input. Please enter a valid amount of cash.")

def main():
    """Main function to simulate the food ordering system."""
    print("Welcome to the Food Ordering System!")
    
   
    menu = display_menu()
    
    
    item, price = get_order(menu)
    print(f"You selected: {item} which costs ${price}.")
    
  
    cash, change = process_payment(price)
    
   
    print(f"Cash received: ${cash}")
    print(f"Change: ${change:.2f}")
    print("Thank you for your order!")


if __name__ == "__main__":
    main()
