def print_status(player_health):
    if player_health <= 0:
        print("Player is dead")
        return
    else:
        print("Player is healthy")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()
