# Morse Code Translator

This Python program allows you to encode messages into Morse code and decode Morse code back into plain text. It's a handy tool for secret communication or just for fun!

## Usage

1. **Encode a Message:**
    - Run the program and select option 1.
    - Enter the message you want to encode.
    - The program will provide the corresponding Morse code.

2. **Decode a Message:**
    - Run the program and select option 2.
    - Enter the Morse code you want to decode.
    - The program will reveal the original message.

## How It Works

The program uses a dictionary called `MORSE_CODE_DICT` to map each letter, number, or punctuation mark to its Morse code representation. Here's a snippet of the dictionary:

```python
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', ...,
    '1': '.----', '2': '..---', ...,
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', ...,
}
```

### Example

Suppose you want to encode the message "HELLO WORLD." The program will convert it to:

```
.... . .-.. .-.. ---   .-- --- .-. .-.. -..
```

And if you input the Morse code `.... . .-.. .-.. ---   .-- --- .-. .-.. -..`, the program will decode it back to "HELLO WORLD."

## How to Run

1. Clone this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the script using `python morsecodetrans.py`.
