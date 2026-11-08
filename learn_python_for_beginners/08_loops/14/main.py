def calculate_experience_points(level):
    xp = 0
    for i in range(0, level):
        xp += (i * 5)
        print(f"Level: {i + 1}, Experience Points: {xp}")
    return xp

def main():
    print(calculate_experience_points(1))  # Output: 0
    print(calculate_experience_points(5))  # Output: 30
    print(calculate_experience_points(10)) # Output: 225

main()
