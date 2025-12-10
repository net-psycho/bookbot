def get_book_text(filepath: str) -> str:
    """
    Reads and returns the full text of a book from a .txt file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")


def count_words(text: str) -> int:
    """
    Returns the number of words in the given text.
    """
    words = text.split()
    return len(words)


def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)

    # message with the *actual computed* number
    print(f"found {word_count} total words.")


if __name__ == "__main__":
    main()
