def filter_messages(messages):
    dang_counters = []
    new_messages = []

    for message in messages:
        good_words = []
        words = message.split()
        dang_counter = 0
        for word in words:
            if word in ("dang", "Dang"):
                good_words.append(word)
            else:
                dang_counter += 1
        new_messages.append(" ".join(good_words))
        dang_counters.append(dang_counter)
    return new_messages, dang_counters


def main():
    messages = ["dang it hurts", "it hurts"]
    print(filter_messages(messages))

main()
