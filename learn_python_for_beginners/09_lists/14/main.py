def get_odd_numbers(num):
    odd_numbers = []

    for i in range(num):
        # don't touch above this line
        if i % 2 != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers

def main():
    num = 10
    print(get_odd_numbers(num))

main()
