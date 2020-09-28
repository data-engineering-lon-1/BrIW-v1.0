import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
        port='33066',
        user='root',
        password='insecure',
        database='demo'
    )
    return mydb

# mycursor = mydb.cursor()

def read_people_from_mydb():
    mydb = connect_db()
    mycursor = mydb.cursor()
    result = {}
    key = 1
    mycursor.execute("SELECT * FROM person")
    rows = mycursor.fetchall()
    for row in rows:
        row = Person(row[1]).firstName
        result.update({key: row})
        key += 1
    return result
    mycursor.close()
    mydb.close()

def delete_person_from_mydb(name_id):
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM person WHERE id = {name_id}")
    mydb.commit()
    # print(f"Unable to delete record with id: {id}. Please try again.")
    mycursor.close()
    mydb.close()

def delete_drink_from_mydb(drink_id):
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM drink WHERE id = {drink_id}")
    mydb.commit()
    # print(f"Unable to delete record with id: {id}. Please try again.")
    mycursor.close()
    mydb.close()

# TODO: finish writing delete drinks function
# def delete_drink_from_mydb_orginal(drink_id):
#     try:
#         mycursor.execute(f"DELETE FROM drink WHERE id = {drink_id}")
#         mydb.commit()
#         print(f"{drink_id}")

#     except Exception:
#         print(f"Unable to delete record with id: {id}. Please try again.")


def read_drinks_from_mydb():
    mydb = connect_db()
    mycursor = mydb.cursor()
    result = {}
    key = 1
    mycursor.execute("SELECT * FROM drink")
    rows = mycursor.fetchall()

    for row in rows:
        row = Drink(row[1]).drink
        result.update({key: row})
        key += 1
    return result
    mycursor.close()
    mydb.close()

def read_favourites_from_mydb():
    mydb = connect_db()
    mycursor = mydb.cursor()
    result = {}
    mycursor.execute("SELECT forename, drink, name FROM person p LEFT JOIN drink d ON d.id = p.drink")
    rows = mycursor.fetchall()
    
    for row in rows:
        forename, drink, name = row
        result.update({forename: name})
    return result
    mycursor.close()
    mydb.close()

def write_favourite_drink_to_db(person_id, drink_id):
    mydb = connect_db()
    mycursor = mydb.cursor()
    person = person_id
    drink = drink_id
    sql = f"UPDATE person SET drink = {drink} WHERE id = {person}"
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()

def write_to_mysql_table_people(dict_from_app):
    mydb = connect_db()
    mycursor = mydb.cursor()
    list_of_tuples = [(k, v) for k, v in dict_from_app.items()]

    write_to_table = "INSERT IGNORE INTO person (id, forename) VALUES (%s, %s)"

    mycursor.executemany(write_to_table, list_of_tuples)
    mydb.commit()
    mycursor.close()
    mydb.close()

def write_to_mysql_table_drink(dict_from_app):
    mydb = connect_db()
    mycursor = mydb.cursor()
    list_of_tuples = [(k, v) for k, v in dict_from_app.items()]
    write_to_table = "INSERT IGNORE INTO drink (id, name) VALUES (%s, %s)"

    mycursor.executemany(write_to_table, list_of_tuples)
    mydb.commit()
    mycursor.close()
    mydb.close()
    
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