class Round:
    # whose_round = ""
    total_price = 0
    # active = False
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

    # def write_round(self, my_round):
    #     my_round = open("drinks.txt", "r")
    #     lines = drinks_file.readlines()

    #     rows = [my_round]
    #     csv_columns = []
    #     key = 1
    #     for line in lines:
    #         my_dict.update({key: line.replace("\n", "")})
    #         key += 1
    #         csv_columns.append(key - 1)
    #     save_names = open("saves_names.csv", "w")
    #     writer = csv.DictWriter(save_names, fieldnames=csv_columns)
    #     writer.writeheader()
    #     writer.writerows(rows)


# while input("Whose round is it? ").lower().capitalize() not in names:
#     print("Person does not exist in database, would you like to add them? ")

# my_round = Round(whose_round)
# print(my_round.whose_round)


# my_round = Round("Charlie")

# print(my_round.is_active())
# my_round.set_active()

# my_round.add_to_round("James", "Fanta")
# my_round.add_to_round("Becks", "Wine")
# my_round.add_to_round("Jason", "Cider")
# my_round.show_round(my_round)
# my_round.print_order()


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

# beer = Drink("Beer", 3, 330, 5)

# print(beer.price)

# beer =
# mocktail
# tea
# coffee
# herbal
