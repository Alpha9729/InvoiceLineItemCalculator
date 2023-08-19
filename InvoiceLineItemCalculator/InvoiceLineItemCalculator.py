def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid interger. Please try again.")

def main():
    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity
        print("\nPRICE:      "+ str(price))
        print("QUANTITY:   "+ str(quantity))
        print("Total:      {:.2f}".format(total))

        another_item = input("Enter another line item? (y/n): ")
        if another_item.lower() != 'y':
            break
        
    print("\n\nBye!")

if __name__ == "__main__":
    print("The Invoice Line Item Calculator\n")
    main()
