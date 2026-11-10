def merge(dict1, dict2):
    new_dict = {}
    for keys in dict1:
        new_dict[keys] = dict1[keys]
    for keys in dict2:
        new_dict[keys] = dict2[keys]
    return new_dict


def main():
    two_towers = {"Frodo": 56, "Aragorn": 10}
    rotk = {"Aragorn": 100, "Gandalf": 809}
    print(merge(two_towers, rotk))

main()
