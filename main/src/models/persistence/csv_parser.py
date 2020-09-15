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