import sys

# Basic mappings: English to Braille and Braille to English
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  # Adding a space for multiple words
}

# Inverting braille_dict to create English-to-Braille mapping
english_dict = {v: k for k, v in braille_dict.items()}

# Special symbols
CAPITAL_FOLLOWS = '.....O'
NUMBER_FOLLOWS = '.O.OOO'

def translate_to_braille(english_text):
    braille_output = []
    for char in english_text:
        if char.isupper():
            braille_output.append(CAPITAL_FOLLOWS)  # Add capital marker
            char = char.lower()
        if char.isdigit():
            braille_output.append(NUMBER_FOLLOWS)  # Add number marker
            # Convert numbers (Braille treats 1-9 like a-j, so 0 is special)
            if char == '0':
                char = 'j'
            else:
                char = chr(ord('a') + int(char) - 1)
        braille_output.append(braille_dict.get(char, '......'))  # Default to space if not found
    return ''.join(braille_output)

def translate_to_english(braille_text):
    english_output = []
    i = 0
    capital_next = False
    number_mode = False
    while i < len(braille_text):
        symbol = braille_text[i:i + 6]
        i += 6
        
        if symbol == CAPITAL_FOLLOWS:
            capital_next = True
            continue
        if symbol == NUMBER_FOLLOWS:
            number_mode = True
            continue
        
        letter = english_dict.get(symbol, ' ')
        if number_mode:
            if letter == 'j':
                letter = '0'
            else:
                letter = str(ord(letter) - ord('a') + 1)
            number_mode = False
        if capital_next:
            letter = letter.upper()
            capital_next = False
        english_output.append(letter)
    
    return ''.join(english_output)

def detect_input_type(text):
    # Simple check for braille (all characters should be O or .)
    if all(c in 'O.' for c in text):
        return 'braille'
    return 'english'

def main():
    # Take input from command line
    input_text = sys.argv[1]
    
    # Determine input type
    input_type = detect_input_type(input_text)
    
    # Perform the appropriate translation
    if input_type == 'english':
        result = translate_to_braille(input_text)
    else:
        result = translate_to_english(input_text)
    
    # Print the translated result
    print(result)

if __name__ == "__main__":
    main()