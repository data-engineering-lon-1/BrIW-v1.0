import mysql.connector

mydb = mysql.connector.connect(
    port='33066',
    user='root',
    password='insecure',
    database='demo'
)

print(mydb)
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

# mycursor.execute("CREATE TABLE people (id INTEGER AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(40), last_name VARCHAR(40), age INTEGER(3))")
# mycursor.execute("CREATE TABLE people (id INTEGER(100), forename VARCHAR(40))")



def write_to_mysql_table(dict_from_app):
    # dict_from_app = {1: 'Ross', 2: 'Monica', 3: 'Joey', 4: 'Chandler', 5: 'Rachel', 6: 'Phoebe'}
    list_of_tuples = [(k, v) for k, v in dict_from_app.items()]
    # print(list_of_tuples)
    write_to_table = "INSERT INTO people (id, forename) VALUES (%s, %s)"

    mycursor.executemany(write_to_table, list_of_tuples)
    mydb.commit()