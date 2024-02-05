import re

def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r') as file:
        return set(word.strip().lower() for word in file)

def spell_check(input_file, dictionary):
    with open(input_file, 'r') as infile:
        content = infile.read()

    words = re.findall(r'\b\w+\b', content)
    misspelled_words = {word for word in words if word.lower() not in dictionary}

    if misspelled_words:
        print("Spelling errors found:")
        print("\n".join(f"- {word}" for word in misspelled_words))
    else:
        print("No spelling errors found.")

def main():
    input_file = input("Enter the path of the text file to check: ")
    dictionary_file = input("Enter the path of the dictionary file: ")

    dictionary = load_dictionary(dictionary_file)

    print(f"Dictionary loaded with {len(dictionary)} words.")

    spell_check(input_file, dictionary)

if __name__ == '__main__':
    main()

