def pig_latin_converter(word):
    vowels = "aeiou"

    if word.lower()[0] in vowels:
        pig_latin_word = word + "ay"
    else:
        pig_latin_word = word[1:] + word[0] + "ay"

    return pig_latin_word.lower() if word.islower() else pig_latin_word.capitalize()

# Example usage:
input_word = input("Enter an English word: ")
pig_latin_result = pig_latin_converter(input_word)
print(f"The Pig Latin version is: {pig_latin_result}")
