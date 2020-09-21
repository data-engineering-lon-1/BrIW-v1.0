# from main.src.models.classesforapp.round import Round, Person, Drink
import mysql.connector


mydb = mysql.connector.connect(
    port='33066',
    user='root',
    password='insecure',
    database='demo'
)

# print(mydb)
mycursor = mydb.cursor()

# John's example:
# mycursor.execute("SELECT * FROM People")
# myresult = mycursor.fetchall()
# print(len(myresult))
# for row in myresult:
#     print(row)

# mycursor.execute("CREATE TABLE drinks (id INTEGER AUTO_INCREMENT PRIMARY KEY, name VARCHAR(40), price FLOAT(10), volume INTEGER(10))")
# write_to_table_placeholder = "INSERT INTO drinks (name, price, volume) VALUES (%s, %s, %s)"
# drinks_list_example = [("Vodka", 3, 25), ("Beer", 4.5, 500),]

# mycursor.executemany(write_to_table_placeholder, drinks_list_example)
# mydb.commit()

# prints rows from selected table
# mycursor.execute("SELECT * FROM drinks")
# rows = mycursor.fetchall()
# for row in rows:
#     print(row)

# mycursor.execute("CREATE TABLE person (id INTEGER AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(40), last_name VARCHAR(40) NULL, age INTEGER(3)) NULL")
# mycursor.execute("CREATE TABLE person (id INTEGER(100) PRIMARY KEY, forename VARCHAR(40))")


def read_people_from_mydb():
    result = {}
    key = 1
    mycursor.execute("SELECT * FROM person")
    rows = mycursor.fetchall()

    for row in rows:
        row = Person(row[1].replace("\n", "")).firstName
        result.update({key: row})
        key += 1
    return result


def read_drinks_from_mydb():
    result = {}
    key = 1
    mycursor.execute("SELECT * FROM drink")
    rows = mycursor.fetchall()

    for row in rows:
        row = Drink(row[1].replace("\n", "")).drink
        result.update({key: row})
        key += 1
    return result

# people_dict_from_db = read_people_from_mydb()
# drinks_dict_from_db = read_drinks_from_mydb()


# dict_from_app = {1: 'Ross', 2: 'Monica', 3: 'Joey', 4: 'Chandler', 5: 'Rachel', 6: 'Phoebe'}
def write_to_mysql_table_people(dict_from_app):
    # dict_from_app = {1: 'Ross', 2: 'Monica', 3: 'Joey', 4: 'Chandler', 5: 'Rachel', 6: 'Phoebe'}
    list_of_tuples = [(k, v) for k, v in dict_from_app.items()]
    # print(list_of_tuples)
    write_to_table = "REPLACE INTO person (id, forename) VALUES (%s, %s)"

    mycursor.executemany(write_to_table, list_of_tuples)
    mydb.commit()

# example = {7: "James", 8: "Paul"}
# write_to_mysql_table_people(dict_from_app)

# def write_to_mysql_table_drinks(dict_from_app):
#     list_of_tuples = [(k, v) for k, v in dict_from_app.items()]
#     write_to_table = "INSERT INTO drinks (id, forename) VALUES (%s, %s)"

#     mycursor.executemany(write_to_table, list_of_tuples)
#     mydb.commit()


# Alter person table to add foreign key linking to drink table
# mycursor.execute("""
# ALTER TABLE person
# ADD FOREIGN KEY (id) REFERENCES drink(id)
# """)
# CREATE TABLE Orders (
#     OrderID int NOT NULL,
#     OrderNumber int NOT NULL,
#     PersonID int,
#     PRIMARY KEY (OrderID),
#     FOREIGN KEY(PersonID) REFERENCES Persons(PersonID)

# create person table with drink id foreign key
# mycursor.execute("CREATE TABLE person (id INTEGER AUTO_INCREMENT PRIMARY KEY, forename VARCHAR(40), FOREIGN KEY (id) REFERENCES drink(id))")















class Person:
    def __init__(self, first_name):
        self.firstName = first_name
        # self.lastName = last_name
        # self.full_name = self.firstName + " " + self.lastName
        # self.age = age


class Drink:
    def __init__(self, drink):
        self.drink = drink
        # self.price = price
        # self.volume = volume
        # self.abv = abv

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