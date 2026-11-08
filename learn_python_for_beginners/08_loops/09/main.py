def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end - 1, 2):
        total += (i + 1)
        print(f"total: {total}")
    return total

def main():
    print(sum_of_odd_numbers(5))    

main()


