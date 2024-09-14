'''
Script: CaesarCipherTool_v1.7.py
Author: Billy Teta / BillyN7
Date: 14 September 2024
Version: 1.7
Description: Simple tool for creating and decoding Caesar Ciphers
'''

# Imported Libraries

import sys

# Functions

def shiftChar(character, shiftAmount, isEncoding=True):
    
    '''
    Shifts a character by the given amount.
    
    Parameters:
    - character: The letter to shift (either uppercase or lowercase)
    - shiftAmount: The number of positions to shift the letter
    - isEncoding: Boolean flag; if True, shift right (encode), if False, shift left (decode)
    
    Returns:
    - The shifted character or the original character if it's not a letter
    '''
    
    if 'A' <= character <= 'Z':  # If the character is uppercase
        base = ord('A')  # Get the ASCII code for 'A'
        shift = shiftAmount if isEncoding else -shiftAmount  # Shift right for encoding, left for decoding
    elif 'a' <= character <= 'z':  # If the character is lowercase
        base = ord('a')  # Get the ASCII code for 'a'
        shift = shiftAmount if isEncoding else -shiftAmount
    else:
        return character  # Non-alphabet characters remain unchanged
    
    # Perform the character shift within the bounds of the alphabet
    return chr((ord(character) - base + shift) % 26 + base)

def encodeMessage(message, shiftAmount):
    '''
    Encodes a message using a Caesar Cipher with a specific shift.
    
    Parameters:
    - message: The plaintext message to encode
    - shiftAmount: The number of positions to shift for the cipher
    
    Returns:
    - The encoded message as a string
    '''
    return ''.join(shiftChar(char, shiftAmount, isEncoding=True) for char in message)

def decodeMessage(message, shiftAmount):
    '''
    Decodes a message encoded with a Caesar Cipher by shifting left.
    
    Parameters:
    - message: The encoded message
    - shiftAmount: The number of positions to shift for the cipher
    
    Returns:
    - The decoded message as a string
    '''
    return ''.join(shiftChar(char, shiftAmount, isEncoding=False) for char in message)

def encodeAllShifts(message):
    '''
    Encodes a message using all possible shift values from 1 to 25.
    
    Parameters:
    - message: The plaintext message to encode
    
    Prints:
    - The encoded message for each shift from 1 to 25
    '''
    for shift in range(1, 26):
        encodedMessage = ''.join(shiftChar(char, shift, isEncoding=True) for char in message)
        print(f"Shift {shift}: {encodedMessage}")

def decodeAllShifts(message):
    '''
    Decodes a message using all possible shift values from 1 to 25.
    
    Parameters:
    - message: The encoded message
    
    Prints:
    - The decoded message for each shift from 1 to 25
    '''
    for shift in range(1, 26):
        decodedMessage = ''.join(shiftChar(char, shift, isEncoding=False) for char in message)
        print(f"Shift {shift}: {decodedMessage}")

def main():
    '''
    Main function to run the Caesar Cipher script.
    Prompts the user for input and performs encoding or decoding based on user choice.
    '''
    print("Type 'quit' or 'q' to end script.")

    running = True
    while running:
        # Ask user whether they want to encrypt or decrypt
        userChoice = ""
        while userChoice not in ["encrypt", "decrypt", "e", "d", "quit", "q"]:
            userChoice = input("\nDo you want to encrypt or decrypt a message? ").strip().lower()
            if userChoice not in ["encrypt", "decrypt", "e", "d", "quit", "q"]:
                print("Invalid input. Please enter 'encrypt', 'decrypt', or 'quit'.")

        if userChoice in ["encrypt", "e"]:
            # Get the message for encryption
            message = ""
            while not message.strip():  # Ensure non-empty input
                message = input("Enter the message to be encrypted: ").strip()
                if not message:
                    print("Invalid input. Please enter a non-empty message.")
            
            # Get shift value or all shifts
            shiftOption = ""
            while not (shiftOption.isdigit() and 1 <= int(shiftOption) <= 25 or shiftOption in ['a', 'all', 'quit', 'q']):
                shiftOption = input("Enter shift amount (1-25) or 'A' for all shifts: ").strip().lower()
                if not (shiftOption.isdigit() and 1 <= int(shiftOption) <= 25 or shiftOption in ['a', 'all', 'quit', 'q']):
                    print("Invalid input. Please enter a number between 1 and 25, or 'A'.")

            # Process the encryption
            if shiftOption in ['all', 'a']:
                print("\nEncoding with all shifts...\n")
                encodeAllShifts(message)
                print()
            elif shiftOption in ['quit', 'q']:
                running = False
            else:
                shiftAmount = int(shiftOption)
                print(f"\nEncoding with shift of {shiftAmount}...")
                encodedMessage = encodeMessage(message, shiftAmount)
                print(f"Encrypted message: {encodedMessage}\n")

        elif userChoice in ["decrypt", "d"]:
            # Get the message for decryption
            message = ""
            while not message.strip():  # Ensure non-empty input
                message = input("Enter the message to be decrypted: ").strip()
                if not message:
                    print("Invalid input. Please enter a non-empty message.")
            
            # Get shift value or all shifts
            shiftOption = ""
            while not (shiftOption.isdigit() and 1 <= int(shiftOption) <= 25 or shiftOption in ['a', 'all', 'quit', 'q']):
                shiftOption = input("Enter shift amount (1-25) or 'A' for all shifts: ").strip().lower()
                if not (shiftOption.isdigit() and 1 <= int(shiftOption) <= 25 or shiftOption in ['a', 'all', 'quit', 'q']):
                    print("Invalid input. Please enter a number between 1 and 25, or 'A'.")

            # Process the decryption
            if shiftOption in ['all', 'a']:
                print("\nDecoding with all shifts...\n")
                decodeAllShifts(message)
                print()
            elif shiftOption in ['quit', 'q']:
                running = False
            else:
                shiftAmount = int(shiftOption)
                print(f"\nDecoding with shift of {shiftAmount}...")
                decodedMessage = decodeMessage(message, shiftAmount)
                print(f"Decrypted message: {decodedMessage}\n")

        elif userChoice in ["quit", "q"]:
            print("Ending program.")
            running = False

        # Ask user if they want to run the program again
        if running:
            runPrompt = ""
            while runPrompt not in ['yes', 'y', 'no', 'n', 'quit', 'q']:
                runPrompt = input("Run again? (Yes/No): ").strip().lower()
                if runPrompt not in ['yes', 'y', 'no', 'n', 'quit', 'q']:
                    print("Invalid input. Please specify Yes or No.")
            
            if runPrompt in ['no', 'n', 'quit', 'q']:
                print("Exiting program.")
                running = False

if __name__ == '__main__':
    '''
    Entry point of the script. Runs the main function and catches any exceptions.
    '''
    try:
        main()
    except Exception as error:
        sys.exit(f"An error has occurred: {error}. The script has been terminated.")

  