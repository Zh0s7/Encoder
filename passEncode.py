import base64, binascii, sys

while (True):
    enc = input("(0)Exit (1)Reverse, (2)Base32, (3)Base64, (4)Base85 (5)Hex \nHow would you like to encode your string: ")
    try:
        enc = int(enc)
        if (enc > 5 or enc < 0):
            print("Please enter a valid number...\n")
        
        elif (enc==0):
            print("byebye!")
            sys.exit()

        else:
            string = input("What would you like to encode?: ")

        if (enc==1):
            stringReversed = string[::-1]
            
            print(f"Original: {string}, Reversed: {stringReversed}")

        elif (enc==2):
            base32Bytes = base64.b32encode(string.encode('utf-8'))
            base32String = base32Bytes.decode('utf-8')

            print(f"Original: {string}, Base32: {base32String}") 
        
        elif (enc==3):
            base64Bytes = base64.b64encode(string.encode('utf-8'))
            base64String = base64Bytes.decode('utf-8')

            print(f"Original: {string}, Base64: {base64String}") 
        
        elif (enc==4):
            base85Bytes = base64.b85encode(string.encode('utf-8'))
            base85String = base85Bytes.decode('utf-8')

            print(f"Original: {string}, Base85: {base85String}") 
        
        elif (enc==5):
            hexString = string.encode('utf-8').hex()

            print(f"Original: {string}, Hex: {hexString}")

    except ValueError:
        print("Please enter a valid integer...\n")
