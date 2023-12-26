def test_add_dish(order, dish):
    order.dishes.append(dish)
    print(f"Added dish: {dish}")

def test_search_customer_by_name(customers, name):
    result = list(filter(lambda customer: name.lower() in customer.name.lower(), customers))
    print(f"Search results for '{name}':")
    for customer in result:
        print(customer)

def test_search_customer_by_address(customers, address):
    result = list(filter(lambda customer: address.lower() in customer.address.lower(), customers))
    print(f"Search results for '{address}':")
    for customer in result:
        print(customer)

def test_update_customer_name(customer, new_name):
    customer.name = new_name
    print(f"Updated customer name to '{new_name}'")

def test_generate_invoice(order):
    invoice = order.generate_invoice()
    print("Generated Invoice:")
    print(invoice)

def test_save_and_load_order(order, filename):
    order.save_to_file(filename)
    loaded_order = OrderRepo()
    loaded_order.load_from_file(filename)
    print("Loaded Order:")
    print(loaded_order.generate_invoice())

# Beispiel-Nutzung
if __name__ == "__main__":
    # Beispiel-Daten
    dish1 = CookedDish("Pasta", 10)
    dish2 = CookedDish("Salad", 5)
    customer1 = Customer("John Doe", "123 Main St")
    order = Order(customer1, [dish1, dish2])

    # Testfunktionalitäten
    test_add_dish(order, CookedDish("Soup", 8))

    customers = [Customer("John Smith", "456 Oak St"), Customer("Jane Doe", "789 Maple St")]
    test_search_customer_by_name(customers, "Doe")
    test_search_customer_by_address(customers, "Maple")

    test_update_customer_name(customer1, "John Updated")
    test_generate_invoice(order)

    test_save_and_load_order(order, "example_order.pkl")
