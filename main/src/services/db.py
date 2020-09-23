import mysql.connector

mydb = mysql.connector.connect(
    port='33066',
    user='root',
    password='insecure',
    database='demo'
)

mycursor = mydb.cursor()

def read_people_from_mydb():
    result = {}
    key = 1
    mycursor.execute("SELECT * FROM person")
    rows = mycursor.fetchall()
    for row in rows:
        row = Person(row[1]).firstName
        result.update({key: row})
        key += 1
    return result


def read_drinks_from_mydb():
    result = {}
    key = 1
    mycursor.execute("SELECT * FROM drink")
    rows = mycursor.fetchall()

    for row in rows:
        row = Drink(row[1]).drink
        result.update({key: row})
        key += 1
    return result

def read_favourites_from_mydb():
    result = {}
    # mycursor.execute("SELECT drink, forename FROM person")
    mycursor.execute("SELECT forename, drink, name FROM person p LEFT JOIN drink d ON d.id = p.drink")
    rows = mycursor.fetchall()
    
    for row in rows:
        forename, drink, name = row
        result.update({forename: name})
    return result


def write_favourite_drink_to_db(person_id, drink_id):
    person = person_id
    drink = drink_id
    sql = f"UPDATE person SET drink = {drink} WHERE id = {person}"
    mycursor.execute(sql)
    mydb.commit()

    # mycursor.execute("SELECT * FROM person")
    # myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    

# ORIGINAL
# def write_to_mysql_table_people(dict_from_app):
    
#     list_of_tuples = [(k, v) for k, v in dict_from_app.items()]
    
#     write_to_table = "REPLACE INTO person (id, forename) VALUES (%s, %s)"

#     mycursor.executemany(write_to_table, list_of_tuples)
#     mydb.commit()

def write_to_mysql_table_people(dict_from_app):
    
    list_of_tuples = [(k, v) for k, v in dict_from_app.items()]
    
    write_to_table = "INSERT IGNORE INTO person (id, forename) VALUES (%s, %s)"

    mycursor.executemany(write_to_table, list_of_tuples)
    mydb.commit()

    # mycursor.execute("SELECT * FROM person")
    # myresult = mycursor.fetchall()
    # print(myresult)
    # input()
    # for x in myresult:
    #     print(x)
    # input()

def write_to_mysql_table_drink(dict_from_app):
    list_of_tuples = [(k, v) for k, v in dict_from_app.items()]
    write_to_table = "INSERT IGNORE INTO drink (id, name) VALUES (%s, %s)"

    mycursor.executemany(write_to_table, list_of_tuples)
    mydb.commit()

    # mycursor.execute("SELECT * FROM person")
    # myresult = mycursor.fetchall()
    # print(myresult)
    # input()
    # for x in myresult:
    #     print(x)
    # input()

# dict_example = {1 : ["Beer", 5, 500]}
# not working yet
# def write_fixed_sql():
#     dict_example = {1 : ["Coke", 2, 330]}
#     write_to_table = "REPLACE INTO drink (id, name, price, volume) VALUES (%s, %s, %s, %s)"

#     mycursor.execute(write_to_table, dict_example)
#     mydb.commit()














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