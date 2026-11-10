from tabnanny import check


def check_ingredient_match(recipe, inventory):
    missing_ingredients = []
    counter = 0
    for ingredient in recipe:
        if ingredient in inventory:
            counter += 1
        else:
            missing_ingredients.append(ingredient)
    percentage = counter / len(recipe) * 100
    return(percentage, missing_ingredients)


def main():
    recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
    inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

    print(check_ingredient_match(recipe, inventory))

main()
