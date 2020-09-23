import time
import os
from main.src.models.classesforapp.round import Round, Person, Drink
from main.src.services.db import read_people_from_mydb, read_drinks_from_mydb, write_favourite_drink_to_db

# TODO: add delete function
# TODO: review classes
# TODO: mocks, stubs, spies


def read_items(txt_file, person_or_drink):
    result = {}
    key = 1
    try:
        f = open(txt_file, "r")
        lines = f.readlines()
        if person_or_drink == "person":
            for line in lines:
                line = Person(line.replace("\n", "")).firstName
                result.update({key: line})
                key += 1
        elif person_or_drink == "drink":
            for line in lines:
                line = Drink(line.replace("\n", "")).drink
                result.update({key: line})
                key += 1
        f.close()
    except FileNotFoundError:
        print(f"{txt_file} not found")
    return result


# names = read_items("main/src/models/functions/names.txt", "person")
# drinks = read_items("main/src/models/functions/drinks.txt", "drink")
names = read_people_from_mydb()
drinks = read_drinks_from_mydb()
favourite_drinks = {}


def create_person(first_name):
    first_name = Person(first_name)
    first_name = first_name.firstName
    names.update({len(names) + 1: first_name.lower().capitalize()})
    print(f"{first_name.lower().capitalize()} has been added!")
    time.sleep(0.5)
    # print(names)
    return names.get(len(names))

# assert person created


def test_create_person(first_name):

    actual_output = create_person(first_name)
    expected_output = first_name

    assert expected_output == actual_output
    print("Success")


def create_drink(drink):
    new_drink = Drink(drink)
    new_drink = new_drink.drink
    drinks.update({len(drinks) + 1: new_drink.lower().capitalize()})
    print(f"{new_drink.lower().capitalize()} has been added!")
    time.sleep(0.5)


def assign_fave_drinks():
    print_dict(names, "names")
    person_id = "not a key"
    while person_id not in names:
        try:
            person_id = int(input("Please enter the person's id: "))
        except:
            print("\nPlease enter a valid person ID")
            time.sleep(0.5)
            pass
    clearScreen()
    person = names[person_id]
    print_dict(drinks, "drinks")
    drink_id = "not a key"
    while drink_id not in drinks:
        try:
            drink_id = int(
                input(f"Please enter id of {person}'s favorite drink: ")
            )
        except:
            print("Please enter a valid drinks ID")
            time.sleep(0.5)
            pass
    global favourite_drinks
    favourite_drinks[person] = drinks[drink_id]
    write_favourite_drink_to_db(person_id, drink_id)


def clearScreen():
    os.system("cls")


bar = "+============================"


def print_dict(my_dict, header):
    print(f"{bar}+\n| {header.upper()}\n{bar}|")
    for key, value in my_dict.items():
        print(f"| {key} {value}")
    print(f"{bar}+\n")
