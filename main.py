import sys

from stats import count_chars, count_letter_occurrence, get_num_words, sort_on

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        file_contents = f.read()

    num_words = get_num_words(file_contents)
    chars = count_chars(file_contents)
    report = count_letter_occurrence(chars)
    report.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("--------- Character Count -------")
    for d in report:
        print(f"{d['letter']}: {d['occurrence']}")
    print("============= END ===============")
