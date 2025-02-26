def get_num_words(str):
    return len(str.split())


def count_chars(str):
    chars = {}
    for c in str.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars


def count_letter_occurrence(chars):
    report = []

    for k, v in chars.items():
        letters = {}
        if k.isalpha():
            letters["letter"] = k
            letters["occurrence"] = v
            report.append(letters)

    return report


def sort_on(dict):
    return dict["occurrence"]
