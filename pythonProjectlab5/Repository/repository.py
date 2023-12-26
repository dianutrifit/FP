import pickle
from Modelle.modelle import Gericht,GekochterGericht,Getrank,Kunde,Bestellung

class DataRepo:
    def __init__(self):
        self.list_with_objects = []

    def save(self, obj):
        self.list_with_objects.append(obj)
        print("Successfully added")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.list_with_objects, file)
        print("Successfully saved to file")

    def load_from_file(self, filename):
        with open(filename, 'rb') as file:
            self.list_with_objects = pickle.load(file)
        print("Successfully loaded from file")

    def read_file(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content

    def write_to_file(self, data, filename):
        with open(filename, 'w') as file:
            file.write(data)
        print("Successfully wrote to file")

    def convert_to_string(self):
        return '\n'.join(map(str, self.list_with_objects))

    def convert_from_string(self, data):
        self.list_with_objects = list(map(int, data.split('\n')))
        print("Successfully converted from string")

class CookedDishRepo(DataRepo):
    def __init__(self):
        super().__init__()

    def convert_to_string(self):
        return '\n'.join(map(str, self.list_with_objects))

    def convert_from_string(self, data):
        self.list_with_objects = list(map(int, data.split('\n')))
        print("Successfully converted CookedDishRepo from string")

class DrinkRepo(DataRepo):
    def __init__(self):
        super().__init__()

    def convert_to_string(self):
        return '\n'.join(map(str, self.list_with_objects))

    def convert_from_string(self, data):
        self.list_with_objects = list(map(int, data.split('\n')))
        print("Successfully converted DrinkRepo from string")

class CustomerRepo(DataRepo):
    def __init__(self):
        super().__init__()

    def convert_to_string(self):
        return '\n'.join(map(str, self.list_with_objects))

    def convert_from_string(self, data):
        self.list_with_objects = list(map(int, data.split('\n')))
        print("Successfully converted CustomerRepo from string")

class OrderRepo(DataRepo):
    def __init__(self):
        super().__init__()

    def convert_to_string(self):
        return '\n'.join(map(str, self.list_with_objects))

    def convert_from_string(self, data):
        self.list_with_objects = list(map(int, data.split('\n')))
        print("Successfully converted OrderRepo from string")

# Beispiel-Nutzung:
order_repo = OrderRepo()
order_repo.save(1)
order_repo.save(2)
order_repo.save(3)

# Konvertierung zu String und Ausgabe
order_repo_string = order_repo.convert_to_string()
print("OrderRepo as String:")
print(order_repo_string)

# Konvertierung von String und Ausgabe
order_repo.convert_from_string(order_repo_string)
print("Loaded Objects:", order_repo.list_with_objects)







