def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    return items[0]

def main():
    print(get_first_item(items))
    print(get_first_item(items1))

items = ["1", "2", "3"]
items1 = []
main()
