class Table:
    def __init__(self, number):
        self.number = number
        self.waiter = "Undefined"
        self.assigned = False
        self.customers = 0
        self.orders = []
        self.Priceattained = 100
        self.Receipt = 1

    def IsAssigned(self):
        if self.assigned == False:
            return True
        else:
            return False

    def assignWaiter(self, Username):
        self.waiter = Username

    def add_customer(self, count):
        self.customers = count

        print(f'\nThere are now {self.customers} Customers in Table {self.number}\n')

    def remove_customer(self, count):
        self.customers -= count

    def add_order(self, item, quantity, price):
        order = {"item": item, "quantity": quantity, "price": price}
        self.orders.append(order)
        print("\nAll Orders:")
        for order in self.orders:
            print(f"| Item: {order['item']}, Quantity: {order['quantity']}, Price: {order['price']} | ")

    def clear_orders(self):
        self.orders = []

    def clear_waiter(self):
        self.waiter = "Undefined"

    def prepare_bill(self):
        total_price = 0

        
        for order in self.orders:
            quantity = order["quantity"]
            price = float(order["price"])
            total_price += quantity * price

        print("\nAll Orders:")
        for order in self.orders:
            print(f"| Item: {order['item']}, Quantity: {order['quantity']}, Price: {order['price']} Total = R{(int(order['quantity'])) * int(order['price'])} | ")
        
        print(f"The total for all of these items are {total_price}")

        print()

        
        return total_price
    
    def create_bill_file(self):
        print("File trigger ")

        folder_path = "TableReceipts"  # Specify the folder path
        file_name = f"Table {self.number} Receipt {self.Receipt}"
        file_path = f"{folder_path}/{file_name}.txt"  # Append the folder path to the file name
        
        self.Priceattained += self.prepare_bill()

        with open(file_path, "w") as file:
            file.write("All Orders:\n")
            for order in self.orders:
                total = int(order['quantity']) * int(order['price'])
                order_line = f"Item: {order['item']}, Quantity: {order['quantity']}, Price: {order['price']} Total = R{total}\n"
                file.write(order_line)
            file.write(f"The total for all of these items is {self.prepare_bill()}\n")

        self.Receipt += 1

        print(f"Bill file '{file_path}' created successfully.")
        print(f"The total for Tabel {self.number} is R{self.Priceattained}")
