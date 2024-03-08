MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '': ''
}
def encode(message):
    encoded_message = ''
    for char in message:
        if char != ' ':
            encoded_message += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            encoded_message += '   '
    return encoded_message
def decode(morse_code):
    morse_code += ' '
    decipher = ''
    citext = ''
    for char in morse_code:
        if (char != ' '):
            i = 0
            citext += char
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher
print('1. Encode a message \n2. Decode a message\n')
inp=int(input('Select one of the following options (1/2): '))
if inp == 1:
    message = input("Enter the message: ")
    print("The encoded message in morse code: " + encode(message))
elif inp == 2:

    morse_code = input("Enter the morse code: ")
    print(f"The decoded more code has the message:\n{decode(morse_code)}")
else:
    print("Wrong option chosen. please try again.")