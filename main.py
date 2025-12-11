import sys
from stats import get_num_words, get_char_counts, sort_char_counts


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
    # Ensure user provided a path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  # book path from command line

    text = get_book_text(filepath)

    # stats
    word_count = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_char_counts = sort_char_counts(char_counts)

    # OUTPUT REPORT
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        char = item["char"]
        num = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
