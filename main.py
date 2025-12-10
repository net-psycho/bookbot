# main.py

from stats import get_num_words

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


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)

    word_count = get_num_words(text)

    print(f"Found {word_count} total words.")


if __name__ == "__main__":
    main()
