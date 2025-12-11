def get_num_words(text: str) -> int:
    """
    Returns the number of words in the given text.
    """
    return len(text.split())


def get_char_counts(text: str) -> dict:
    """
    Returns a dictionary mapping each character to its count.
    Characters are converted to lowercase.
    """
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def sort_char_counts(char_dict: dict) -> list:
    """
    Takes the dictionary of character counts and returns a sorted list of
    dictionaries like: {"char": "a", "num": 12345}
    Sorted from highest count to lowest.
    """
    # convert dict -> list of {char: X, num: Y} dictionaries
    items = [{"char": c, "num": n} for c, n in char_dict.items()]

    # helper function for sorting by "num"
    def sort_key(item):
        return item["num"]

    # in-place sort, greatest to least
    items.sort(key=sort_key, reverse=True)

    return items
