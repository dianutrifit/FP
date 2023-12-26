from Modelle.modelle import Gericht,GekochterGericht,Getrank,Kunde,Bestellung
from Repository.repository import CookedDishRepo,DrinkRepo,CustomerRepo,OrderRepo

class Controller:
    def __init__(self, repo):
        self.repo = repo

    def add_new_object(self, size, colour, clothing_type, price):
        new_price = price + 10
        new_item = Clothing(size, colour, clothing_type, new_price)
        self.repo.save(new_item)
        self.repo.display_objects()
