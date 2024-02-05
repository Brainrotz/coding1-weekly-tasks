nato_phonetic_alphabets = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

def text_to_nato(text):
    return ' '.join(nato_phonetic_alphabets.get(char.upper(), char) for char in text)

def nato_to_text(nato_text):
    reversed_lookup = {value: key for key, value in nato_phonetic_alphabets.items()}
    return ' '.join(reversed_lookup.get(word, word) for word in nato_text.split())

# Example usage:
input_text = input("Enter a word : ")
nato_result = text_to_nato(input_text)
print("NATO Phonetic Alphabets:", nato_result)

