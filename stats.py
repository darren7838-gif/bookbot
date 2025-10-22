def count_words(text):
    words = text.split()
    word_counter = 0
    for word in words:
        word_counter += 1
    return word_counter


def character_count(text):
    char_counts = {}
    text = text.lower()
    for character in text:
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    return char_counts

def sort_char_counts(char_counts):
    result = []
    for char, count in char_counts.items():
        result.append({"char": char, "num": count})
    def get_num(d):
        return d["num"]
    result.sort(key=get_num, reverse=True)
    return result
