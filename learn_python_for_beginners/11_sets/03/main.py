def count_vowels(text):
    vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    vowels_in_text = set()
    vowels_counter = 0

    for character in text:
        if character in vowels:
            vowels_counter += 1
            vowels_in_text.add(character)
    return vowels_counter, vowels_in_text

def main():
    text = "Did someone say Thunderfury, Blessed Blade of the Windseeker?"
    print(count_vowels(text))

main()
