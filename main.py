"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending):
    if not isinstance(items, list):
        raise RuntimeError(f"It can't be sorted {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascSort = False
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascSort = sys.argv[3].lower() != "desc"
    else:
        print("First argument is required (textfile)")
        print("Second argument is required (delete dups or not)")
        print("Third argument is required (asc | desc)")
        sys.exit(1)

    print(f"The file {filename}'s words will be readed")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"Not found {filename}")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list,ascSort))
