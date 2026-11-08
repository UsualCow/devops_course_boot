def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        ausgabe = "correct amount"
    else:
        ausgabe = "incorrect amount"
    return ausgabe

def main():
    print(check_swords_for_army(500, 1000))
    print(check_swords_for_army(800, 800))
    print(check_swords_for_army(1500, 1000))
    print(check_swords_for_army(200, 200))

main()