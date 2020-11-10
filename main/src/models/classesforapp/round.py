class Round:
    total_price = 0
    drink_person_dict = {}
    drink = ""
    name = ""

    def __init__(self, whose_round, drink_person_dict):
        self.whose_round = whose_round
        self.drink_person_dict = drink_person_dict
        self.active = False

    def add_to_round(self, name, drink):
        if self.active == True:
            self.drink_person_dict.update({name: drink})
        else:
            print("Not taking any more orders!")

    def update_round(self, favourite_drinks):
        self.drink_person_dict = favourite_drinks

    def show_round(self, my_round):
        print(self.drink_person_dict)

    def is_active(self):
        return self.active

    def set_active(self):
        self.active = True
    
    def set_inactive(self):
        self.active = False

    def print_order(self):
        for name, drink in self.drink_person_dict.items():
            print(name, drink)

    def return_order(self, drink_person_dict):
        return self.drink_person_dict

class Person:
    def __init__(self, forename):
        self.firstName = forename
        # self.lastName = last_name
        # self.full_name = self.firstName + " " + self.lastName
        # self.age = age


class Drink:
    def __init__(self, drink):
        self.drink = drink
        # self.price = price
        # self.volume = volume
        # self.abv = abv