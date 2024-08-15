def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)

    generate_report(num_words, char_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def generate_report(num_words, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n\n")

    char_list = []
    for char in char_count:
        char_list.append({"char": char, "times": char_count[char]})

    char_list.sort(reverse=True, key=sort_on)
    for alpha in char_list:
        if alpha["char"].isalpha():
            char = alpha["char"]
            times = alpha["times"]
            print(f"The '{char}' character was found {times} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["times"]
main()