import csv
from main.src.models.classesforapp.round import Round, Person, Drink
from main.src.models.functions.create_functions import read_items, names, drinks



def csv_reader(csv_file, dict_file):
    with open(csv_file, "r") as r:
        reader = csv.reader(r)
        
        for row in reader:
            person = row[0]
            drink = row[1]
            dict_file[person] = drink

def csv_writer(csv_file, dict_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(dict_file.items())

def csv_parser(csv_file):
    with open(csv_file, "r") as r:
        for l in r:
            for idx, c in enumerate(l):
                if c == '"':
                    if idx % 2 == 0:
                        print("Even")
                    else:
                        print("Odd")

def csv_parser2(csv_file):
    with open(csv_file, "r") as r:
        for l in r:
            for idx, c in enumerate(l):
                if c == ',':
                    if l[idx+1] == '"':
                        print("True")
                    else:
                        print("False")

def write_items_list(txt_file, items_dict):
    f = open(txt_file, "w")
    try:
        for line in items_dict.values():
            f.write(line + "\n")
    finally:
        f.close()

def save_and_exit():
    write_items_list("main/src/models/functions/names.txt", names)
    write_items_list("main/src/models/functions/drinks.txt", drinks)