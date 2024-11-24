def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    character_counts = count_characters(text)
    list_of_character_count = [{key: value} for key, value in character_counts.items()]

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} - number of words in the document")
    for dictionary in list_of_character_count:
        for key, value in dictionary.items():
            if key.isalpha():
                print(f"The {key} character was found {value} times")
    print(f"--- End of Report --- ")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    character_count = {}
    for char in text:
        lowered_text = char.lower()
        if lowered_text in character_count:
            character_count[lowered_text] += 1
        else:
            character_count[lowered_text] = 1
    return character_count

main()