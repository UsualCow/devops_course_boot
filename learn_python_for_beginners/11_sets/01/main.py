def remove_duplicates(spells):
    set_of_spells = set(spells)
    return list(set_of_spells)

def main():
    spells = [
        "fireball",
        "eldritch blast",
        "fireball",
        "eldritch blast",
        "chill touch",
        "eldritch blast",
        "chill touch",
        "chill touch",
        "fireball",
        "fireball",
        "shocking grasp",
        "fireball",
        "fireball",
    ]

    print(remove_duplicates(spells))

main()
