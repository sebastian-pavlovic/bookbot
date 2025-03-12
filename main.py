from sys import argv
from stats import word_count, character_count, sort_dictionary

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(argv[1])
    count = word_count(contents)
    dictionary = character_count(contents)
    sorted = sort_dictionary(dictionary)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at ")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for d in sorted:
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")

    
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    

main()