from stats import get_word_count, get_char_count, get_dict_list
import sys


def get_book_text(path):
    with open(path,"r",encoding="utf-8") as f:
        file_cont=f.read()
    return file_cont


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text=get_book_text(sys.argv[1])
        char_dict=get_char_count(text)
        print(f"""============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}...
    ----------- Word Count ----------
    Found {get_word_count(text)} total words
    --------- Character Count -------""")
        for i in get_dict_list(char_dict):
            print(f"{i['char']}: {i['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)