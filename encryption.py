#https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec got idea from this
# key can only be numeric
# affects mapping of chars to numeric value
def tableDictEncryption(key, text):
    #KEY IS TRANSLATED FROM A STRING TO BINARY
    key = int(''.join(format(ord(x), 'b') for x in str(key)))

    plainText = list(text)
    chars = ['!','#','$','%','&','(',')','*','+',',','-','.','.','/','0','1','2','3','4','5','6','7','8','9',':',';'
    ,'<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
    'W','X','Y','Z','[','\\',']','^','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z','{','|','}','~']

    # from the base position of the chars array
    # this will shift the array by as much as the key
    # i.e if 'a' is in index 0 and length of chars list is 82
    # rotate the char around by 100, the new index will be 18
    shiftAmount = key % len(chars)
    chars = chars[-shiftAmount:] + chars[:-shiftAmount]

    encodingDict = {' ': ' '} # a space is just denoted by a space


    # each char is mapped to an integer Value
    # key value being whatever the first char in the list is
    # and it iterates so on
    for i in range(len(chars)):
        encodingDict[chars[i]] = "! !" + str(oct(key // 2 + i))[::-1] + "! !"
             
    # char is integer divided to obfuscate the key being apart of the process it when using it as the mapping value so as to not expose the key 
    # furthermore we increment this value by 1 to make sure each char is unique and there is no overlap between them we also convert this integer value to octal
    # Then we reverse the octal string so that it display backwards for even more obfuscation
    # "! !" was added at the start and end to further pad each character mapping
    # ex. with a key of 0 the character 'a' if  it is in index 0 of original char map from what is explained above it will be in index  18
    # so we see that is 10 // 2 + 18 which is 23 then we take the octal of this number and convert it to string '0o22'
    # Then we reverse this string '22o0'

    cipherText = ""
    # for every plaintext char convert it to ciphertext chars
    # using  the encodingDict 1:1 mapping 
    # Adds a '~~' to denote a space between each character
    for i in range(0, len(plainText)):
        char = plainText[i]
        mappedKey = str(encodingDict[char]) + '~~'
        plainText[i] = mappedKey
    plainText = "".join(plainText) # after all operations we make it all one

    # We convert everything to hex and denote this as the ciphertext
    for char in plainText:
        cipherText += char.encode('utf-8').hex()

    return(cipherText)