#!/usr/bin/env python3

import base64, binascii, sys

def encode(string, currEnc):
    enc = input("(0)Exit (1)Reverse, (2)Base32, (3)Base64, (4)Base85 (5)Hex \nHow would you like to encode your string: ")
    enc = int(enc)
    if (enc > 5 or enc < 0):
        print("Please enter a valid number...\n")
    
    elif (enc==0):
        if (currEnc!=""):
            print(f"\nYour last encoding was {currEnc}.")
        print("\nbyebye!")
        sys.exit()

    if (enc==1):
        stringReversed = string[::-1]
        currEnc = stringReversed
        
        print(f"\nOriginal: {string}, Reversed: {stringReversed}")

    elif (enc==2):
        base32Bytes = base64.b32encode(string.encode('utf-8'))
        base32String = base32Bytes.decode('utf-8')
        currEnc = base32String

        print(f"\nOriginal: {string}, Base32: {base32String}") 
    
    elif (enc==3):
        base64Bytes = base64.b64encode(string.encode('utf-8'))
        base64String = base64Bytes.decode('utf-8')
        currEnc = base64String

        print(f"\nOriginal: {string}, Base64: {base64String}") 
    
    elif (enc==4):
        base85Bytes = base64.b85encode(string.encode('utf-8'))
        base85String = base85Bytes.decode('utf-8')
        currEnc = base85String

        print(f"\nOriginal: {string}, Base85: {base85String}") 
    
    elif (enc==5):
        hexString = string.encode('utf-8').hex()
        currEnc = hexString

        print(f"\nOriginal: {string}, Hex: {hexString}")

    return currEnc

currEnc = ""

while (True):
    inp = input("\nWhat would you like to encode? (0)Exit: ")
    try:
        if (inp=="0"):
            if (currEnc!=""):
                print(f"\nYour last encoding was {currEnc}.")
            print("\nbyebye!")
            sys.exit()
        currEnc = encode(inp, currEnc)
        while (True):
            repeat = input(f"\nWould you like to encode {currEnc} agian? (y/n): ").lower()
            if (repeat=="y"):
                currEnc = encode(currEnc, currEnc)
            elif (repeat=="n"):
                break
            else:
                print("Please enter a valid input...")

    except ValueError:
        print("Please enter a valid input...\n")
