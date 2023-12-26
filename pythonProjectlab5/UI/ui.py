from Controller.Controller import Controller
from Repository.repository import ClothingRepo

class UI:
    def __init__(self):
        self.repo = ClothingRepo()
        self.controller = Controller(self.repo)


    def show_menu(self):
        print("Optiunea 1: Adaugare articol nou\n")
        print("Optiunea 2: Update articol\n")
        user_input = int(input("Optiune aleasa: "))
        if user_input == 1:
            size = int(input("Size: "))
            colour = input("Colour: ")
            clothing_type = input("Clothing tyoe: ")
            price = int(input("Price: "))
            self.controller.add_new_object(size, colour, clothing_type, price)
