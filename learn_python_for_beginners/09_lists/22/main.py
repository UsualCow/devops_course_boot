def filter_messages(messages):
    good_words = []
    dang_counters = []
    new_messages = []

    for i in range(len(messages)):
        message = messages[i].split()
        dang_counters.append(0)
        for j in range(len(message)):
            if message[j] != "dang" and message[j] != "Dang":
                good_words.append(message[j])
            else:
                dang_counters[i] += 1
        new_messages.append(" ".join(good_words))
        good_words = []
    return new_messages, dang_counters





def main():
    messages = ["dang it hurts", "it hurts"]
    print(filter_messages(messages))

main()
