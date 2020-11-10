from main.src.models.classesforapp.round import Round, Person, Drink
from main.src.models.functions.read_write_functions import csv_reader, csv_parser, csv_parser2, write_items_list
from main.src.models.functions.create_functions import create_person, create_drink, read_items, assign_fave_drinks, print_dict, clearScreen, favourite_drinks
import main.src.models.persistence.csv_parser
from main.src.services.db import write_to_mysql_table_people, write_to_mysql_table_drink, read_favourites_from_mydb, write_favourite_drink_to_db, delete_person_from_mydb, delete_drink_from_mydb, read_people_from_mydb, read_drinks_from_mydb 
import time
import sys
import unittest
from unittest.mock import Mock
sys.path.append(".")
sys.path.append('main')

def check_user_input():
    clearScreen()
    global user_input
    user_input = input(msg)
    clearScreen()
    while user_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        user_input = input(
            msg.replace(
                "Enter your selection: ",
                f"{user_input} is not a valid option. \nPlease enter a valid selection (1-10): ",
            )
        )
        clearScreen()


def nested_menu():
    go_to_menu_input = input(go_to_menu).upper()
    while go_to_menu_input not in ["YES", "Y"]:
        if go_to_menu_input in ["NO", "N"]:
            clearScreen()
            choose_exit = input(exit_offer).upper()
            if choose_exit in ["YES", "Y"]:
                global user_input
                user_input = "10"
                return user_input
            elif choose_exit in ["NO", "N"]:
                clearScreen()
                go_to_menu_input = input(go_to_menu).upper()
            else:
                print("Please enter Y or N")
        else:
            print("Please enter Y or N")
            go_to_menu_input = input(go_to_menu).upper()
    if go_to_menu_input in ["YES", "Y"]:
        check_user_input()


def is_id_valid(id, my_dict):
    return int(id) in my_dict

round_order = {}
go_to_menu = "Would you like to return to the main menu? Y/N "
exit_offer = "Would you like to exit the app? Y/N "

msg = """Welcome to BrIW v1.0!
Please, select an option by entering a number:
[1] Get all people
[2] Get all drinks
[3] Assign favorite drink to person
[4] Get all favourite drinks
[5] Order round of assigned drinks
[6] Create a new person
[7] Create a new drink
[8] Delete person record
[9] Delete drink record
[10] Exit
Enter your selection: """

if __name__ == '__main__':
    user_input = " "
    check_user_input()
    while user_input != "10":
        if user_input == "1":
            names = read_people_from_mydb()
            print_dict(names, "People")
            nested_menu()
        elif user_input == "2":
            drinks = read_drinks_from_mydb()
            print_dict(drinks, "Drinks")
            nested_menu()
        elif user_input == "3":
            favourite_drinks = read_favourites_from_mydb()
            assign_fave_drinks()
            check_user_input()
        elif user_input == "4":
            favourite_drinks = read_favourites_from_mydb()
            print_dict(favourite_drinks, "favourite drinks")
            nested_menu()
        elif user_input == "5":
            round_select = input("Whose round is it? ").lower().capitalize()
            while round_select not in names.values():
                add_person = input(
                    f"{round_select} does not exist in the database, would you like to add them? Y/N ").upper()
                if add_person in ["YES", "Y"]:
                    create_person(round_select)
                elif add_person in ["NO", "N"]:
                    nested_menu()
                    break
                else:
                    print("Please enter Y or N")
            if round_select in names.values():
                print(f"This round's on {round_select}!")
                selection = input(
                    f"Is {round_select} still taking orders? Y/N ")
                global current_round
                current_round = Round(round_select, favourite_drinks)
                while selection.upper() not in ["YES", "Y", "NO", "N"]:
                    selection = input(
                        f"{selection.upper()} is not recognised. Please select Y or N.\nIs {round_select} still taking orders? Y/N ")
                if selection.upper() in ["YES", "Y"]:
                    current_round.set_active()
                    select = input("Add drinks to order? Y/N ")
                    while select.upper() not in ["YES", "Y", "NO", "N"]:
                        select = input(
                            f"{select} is not recognised. Please select Y or N.\nAdd drinks to order? Y/N ").upper()
                    if select.upper() in ["YES", "Y"]:
                        while True:
                            assign_fave_drinks()
                            select = input("Add more drinks to order? Y/N ")
                            while select.upper() not in ["YES", "Y", "NO", "N"]:
                                select = input(
                                    f"{select} is not recognised. Please select Y or N.\nAdd more drinks to order? Y/N ").upper()
                            if select.upper() in ["YES", "Y"]:
                                continue
                            elif select.upper() in ["NO", "N"]:
                                see_final_order = input(
                                    "Would you like to see the final order? Y/N ")
                                while see_final_order.upper() not in ["YES", "Y", "NO", "N"]:
                                    see_final_order = input(
                                        f"{see_final_order.upper()} is not recognised. Please select Y or N.\nWould you like to see the final order? Y/N ")
                                if see_final_order.upper() in ["YES", "Y"]:
                                    final_order_return = current_round.return_order(
                                        favourite_drinks)
                                    print_dict(final_order_return,
                                            f"{round_select}'s round")
                                    current_round.update_round(
                                        favourite_drinks)
                                    current_round.set_inactive()
                                    nested_menu()
                                    break
                                else:
                                    nested_menu()
                    elif select.upper() in ["NO", "N"]:
                        nested_menu()
                    current_round.update_round(favourite_drinks)
                else:
                    current_round.set_inactive()
                    print(
                        f"{round_select} is no longer taking orders for the round!")
                    nested_menu()
        elif user_input == "6":
            new_name = input("Please enter a new name: ")
            names = read_people_from_mydb()
            create_person(new_name)
            check_user_input()
        elif user_input == "7":
            new_drink = input("Please enter a new drink: ")
            drinks = read_drinks_from_mydb()
            create_drink(new_drink)
            clearScreen()
            check_user_input()
        elif user_input == "8":
            print_dict(names, "People")
            name_id = input("Please enter the name or id of the person you'd like to remove from the database: ")
            delete_person_from_mydb(name_id)
            clearScreen()
            check_user_input()
        elif user_input == "9":
            print_dict(drinks, "Drinks")
            drink_id = input("Please enter the name or id of the drink you'd like to remove from the database: ")
            delete_drink_from_mydb(drink_id)
            clearScreen()
            check_user_input()
        else:
            break

    clearScreen()
    

    names = read_people_from_mydb()
    drinks = read_drinks_from_mydb()
    write_to_mysql_table_people(names)
    write_to_mysql_table_drink(drinks)


    print("Exited successfully!")