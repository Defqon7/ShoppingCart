class ShoppingCart:
    # default constructor
    def __init__(self):
        self.name = "none"
        self.date = "January 1, 2020"
        self.cart_items = []

    # parameterized constructor
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.cart_items = []

    # append item to cart_items list
    def add_item(self, item):
        self.cart_items.append(item)
        print(item.item_name + ' added to your Shopping Cart')

    # remove item from cart_items list
    def remove_item(self, item_name):
        # check if cart is empty
        if len(self.cart_items) == 0:
            print('Item not found in cart, nothing removed.')
        # if item exists in cart, remove it
        for i in range(len(self.cart_items)):
            if item_name == self.cart_items[i].item_name:
                print(self.cart_items[i].item_name + ' removed from shopping cart.')
                self.cart_items.pop(i)
                return
        # if item cannot be found in cart
        print('Item not found in cart, nothing modified.')

    def modify_item(self, item_name):
        # check if cart is empty
        if len(self.cart_items) == 0:
            print('Item not found in cart, nothing modified.')
        # decide what you want to change about item
        while True:
            print('What would you like to modify about item: ' + item_name)
            print('d - description')
            print('p - price')
            print('c - quantity')
            print('q - quit')
            option = input('Choose an option: ')

            if option.lower() == 'q':
                break;
            # change item description to users input
            elif option.lower() == 'd':
                for i in range(len(self.cart_items)):
                    if item_name == self.cart_items[i].item_name:
                        description = input('What would you like the description changed to? ')
                        self.cart_items[i].item_description = description
                        print('Description changed to ' + self.cart_items[i].item_description)
                        return
                print('Item not found in cart, nothing modified.')
                break
            # change item price to users input
            elif option.lower() == 'p':
                for i in range(len(self.cart_items)):
                    if item_name == self.cart_items[i].item_name:
                        price = input('What would you like the price changed to? ')
                        self.cart_items[i].item_price = price
                        print('Price changed to ' + self.cart_items[i].item_price)
                        return
                print('Item not found in cart, nothing modified.')
                break
            # change item quantity to users input
            elif option.lower() == 'c':
                for i in range(len(self.cart_items)):
                    if item_name == self.cart_items[i].item_name:
                        quantity = input('What would you like the quantity changed to? ')
                        self.cart_items[i].item_quantity = quantity
                        print('Quantity changed to ' + self.cart_items[i].item_quantity)
                        return
                print('Item not found in cart, nothing modified.')
                break
            # users input does not match menu options
            else:
                print('Invalid input.')

    # return number of items in cart_items list
    def get_num_items_in_cart(self):
        return len(self.cart_items)

    # return total cost of all items in cart
    def get_cost_of_cart(self):
        total_cost = 0
        for i in range(len(self.cart_items)):
            total_cost += self.cart_items[i].item_quantity * self.cart_items[i].item_price
        return total_cost

    # print item's, their costs, and total cost to console
    def print_total(self):
        print(self.name + 's Shopping Cart - ' + self.date)
        print('Number of items: ' + str(self.get_num_items_in_cart()))
        if len(self.cart_items) == 0:
            print('Shopping cart is empty.')
        else:
            total_cost = 0

            for i in range(len(self.cart_items)):
                total_cost += float(self.cart_items[i].item_quantity) * float(self.cart_items[i].item_price)

            for i in range(len(self.cart_items)):
                self.cart_items[i].print_item_cost()
            cost_formatted = "{:.2f}".format(total_cost)
            print('Total: $' + str(cost_formatted))

    # print all items descriptions from cart_items list
    def print_descriptions(self):
        print(self.name + 's Shopping Cart - ' + self.date)
        print('Item Descriptions:')
        for i in range(len(self.cart_items)):
            print(self.cart_items[i].item_name + ' - ' + self.cart_items[i].item_description)


class ItemToPurchase:
    # default constructor
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_quantity = 0
        self.item_price = 0

    # parameterized constructor
    def __init__(self, item_name, item_price, item_quantity, item_description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # print total cost of item to console
    def print_item_cost(self):
        # convert attributes to floats for arithmetic
        total_price = float(self.item_price) * int(self.item_quantity)
        # format to 2 decimals
        price_formatted = "{:.2f}".format(float(self.item_price))
        total_formatted = "{:.2f}".format(float(total_price))
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' +
              str(price_formatted) + ' = $' + str(total_formatted))


def print_menu(customer):
    while True:
        print('MENU')
        print('a - add item to cart')
        print('r - remove item from cart')
        print('c - change items quantity, price, or description')
        print('i - output items descriptions')
        print('o - output shopping cart')
        print('q - quit')
        option = input('Choose an option: ')

        if option.lower() == 'q':
            break;

        elif option.lower() == 'a':
            item_name = input('Enter item name: ')
            item_price = input('Enter item price: ')
            item_quantity = input('Enter item quantity: ')
            item_description = input('Enter item description: ')
            item = ItemToPurchase(item_name, float(item_price), int(item_quantity), item_description)
            customer.add_item(item)

        elif option.lower() == 'r':
            remove_item = input('Which item would you like to remove? ')
            customer.remove_item(remove_item)

        elif option.lower() == 'c':
            item_to_modify = input('Which item would you like to modify? ')
            customer.modify_item(item_to_modify)

        elif option.lower() == 'i':
            print('OUTPUT ITEMS DESCRIPTIONS')
            customer.print_descriptions()

        elif option.lower() == 'o':
            print('OUTPUT SHOPPING CART')
            customer.print_total()
        else:
            print('Incorrect input')


def main():
    customer_name = input('Enter customers name: ')
    date = input('Enter todays date: ')
    print('Customers name: ' + customer_name)
    print('Todays date: ' + date)
    customer = ShoppingCart(customer_name, date)
    print_menu(customer)


if __name__ == '__main__':
    main()
