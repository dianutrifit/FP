class Identifizierbar:

    def __init__(self,_id):
        self.id = id

class Gericht(Identifizierbar): #erbt - mosteneste Identifizierbar

    def __init__(self,_id,portionsgrosse,preis):
        super().__init__(_id)
        self.portionsgrosse = portionsgrosse
        self.preis = preis

class GekochterGericht(Gericht):

    def __init__(self,_id,portionsgrosse,preis,zubereitungszeit):
        super().__init__(_id, portionsgrosse, preis)
        self.zubereitungszeit = zubereitungszeit

class Getrank(Gericht):

    def __init__(self,_id,portionsgrosse,preis, alkoholgehalt):
        super().__init__(_id, portionsgrosse, preis,alkoholgehalt)
        self.alkoholgehalt = alkoholgehalt

class Kunde(Identifizierbar):

    def __init__(self,_id,name,adresse):
        super().__init__(_id)
        self.name = name
        self.adresse = adresse

class Bestellung(Identifizierbar):

   def __init__(self, _id, customer_id, dish_ids, drink_ids):
        super().__init__(_id)
        self.customer_id = customer_id
        self.dish_ids = dish_ids
        self.drink_ids = drink_ids
        self.total_cost = 0

    def calculate_total_cost(self, dishes, drinks):
        dish_prices = [dishes[dish_id].price for dish_id in self.dish_ids]
        drink_prices = [drinks[drink_id].price for drink_id in self.drink_ids]
        total_cost = reduce(lambda acc, price: acc + price, dish_prices + drink_prices, 0)
        self.total_cost = total_cost
        return total_cost

    def _generate_invoice_string(self, dishes, drinks, customers):
        customer_name = customers[self.customer_id].name
        invoice = f"Invoice for {customer_name} (Order ID: {self.id}):\n"

        for dish_id in self.dish_ids:
            dish = dishes[dish_id]
            invoice += f"{dish.portion_size}g {dish.__class__.__name__}: {dish.price}$\n"

        for drink_id in self.drink_ids:
            drink = drinks[drink_id]
            invoice += f"{drink.portion_size}g {drink.__class__.__name__} (Alcohol Content: {drink.alcohol_content}%): {drink.price}$\n"

        invoice += f"Total Cost: {self.total_cost}$"
        return invoice

    def display_invoice(self, dishes, drinks, customers):
        invoice = self._generate_invoice_string(dishes, drinks, customers)
        print("Generated Invoice:")
        print(invoice)



