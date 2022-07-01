def tableDictDecryption(key, cipherText):
    # KEY IS TRANSLATED FROM A STRING TO BINARY
    key = int(''.join(format(ord(x), 'b') for x in str(key)))

    # first decode the hex to utf-8 (string) characters before reversing the rest of the operations
    cipherText = bytes.fromhex(cipherText).decode('utf-8')

    # normal char table
    chars = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z', '[', '\\', ']', '^', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

    # shift the chars array using the key
    # to get the base char table that the encryption used
    shiftAmount = key % len(chars)
    chars = chars[-shiftAmount:] + chars[:-shiftAmount]

    # next recreate the mapping of characters to integer
    # that the encryptor used
    encodingDict = {' ': ' '}
    for i in range(len(chars)):
        encodingDict[chars[i]] = "! !" + str(oct(key // 2 + i))[::-1] + "! !"

    # now swap the key and value pairs to map the values to char
    reverseEncodingDict = {str(value): key for key,
                           value in encodingDict.items()}

    # spaces in the cipherText are denoted by '~~'
    # remove these by splitting it into an array at '~~'
    # this works as '~' has its own integer representation
    # there is no overlap between a plaintext '~'
    # store each integer block in array for easy iteration
    cipherText = cipherText.split('~~')

    # now map each integer to its char equivalent
    # iterates over each integer in cipherText list
    for i in range(0, len(cipherText)):
        char = cipherText[i]
        if (char == '' or char == ' '):
            # skip all other spaces which is unecessary
            # as all real spaces do not have an integer value
            # they are denoted by a real space
            pass
        else:
            mappedKey = str(reverseEncodingDict[char])
            cipherText[i] = mappedKey

    return (''.join(cipherText))
