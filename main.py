def main():
    book_path = "./books/frankenstein.txt"
    book = read_book(book_path)
    word_count = count_words(book)
    character_count = count_characters(book)
    convert_to_list = create_list(character_count)
    print_report(convert_to_list)


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(book):
    return len(book.split())


def count_characters(book):
    chars = {}
    for char in book:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def create_list(dict):
    character_list = []
    for key in dict:
        if key.isalpha():
            character_list.append({"Character": key, "Count": dict[key]})
    return character_list


def sort_on(dict):
    return dict["Character"]


def print_report(dict):
    dict.sort(key=sort_on)
    for item in dict:
        character = item["Character"]
        count = item["Count"]
        print(f"The Character: {character} has {count} instances")


if __name__ == "__main__":
    main()
