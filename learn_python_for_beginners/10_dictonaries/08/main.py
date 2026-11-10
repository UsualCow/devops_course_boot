def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    most_common_enemy = None
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            most_common_enemy = enemy
    return most_common_enemy


def main():
    enemies_dict = {"jackal": 1, "kobold": 2, "soldier": 3, "gremlin": 5}
    print(get_most_common_enemy(enemies_dict))

main()
