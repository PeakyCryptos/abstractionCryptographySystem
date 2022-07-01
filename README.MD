## Intro
abstractionCryptographySystem was a project created for a cryptography course that I took in University. The premise of the assignment was that it would be a contest where we were to come up with our own implementation of an asymmetric cryptography system that would be pitted up against others in the class. The assignment spanned the course of 2 weeks. Where we would have a week to come up with the system, and another week to crack the submissions of others.

The format in which the submission was expected to be submitted to class was as follows: The cryptography system should not leverage any existing encryption systems/libraries, as our implementation was required to be solely our own work. Furthermore, the only information released to the class during the cracking phase would be the key used to encrypt that data, and the ciphertext that key produced. However, our decryption functionality was required to be fully functional. So, that it wasn't possible to cheat by producing a cipher that was unfeasible to reverse engineer. It was also a requirement that in the plain text which was subsequently encrypted, that we have the phrase "Ontario Tech University" embedded anywhere of our choosing. Furthermore, we were only allowed to use a predefined set of symbols/characters in our initial plaintext. Which I have outlined below as being what I used for the "Base Char List" in the encryption and decryption steps. 

It should also be noted that this system was defined specifically for the task at hand. 'Reinventing the wheel' so as to speak with a new mathematical proof that could produce a truly uncrackable cipher is unfeasible. This cryptograpghy system relies heavily on abstraction from the original text to the final result. Going through a myraid of processes to make it near impossible to discren how the final result was achieved if someone was to just possess the key and ciphertext. Which really did show, as no one in the class we able to crack this using the information at hand. While I was able to crack the systems of two others. It is important to note though, as a public system this has some vulnerabilities which I speak about in the section below.   


## Encryption Methodology
1) I Created a char list that will be mapped to a number. The idea was taken from a UTF-8 encoding table which maps characters to a hexadecimal number.

Base Char list:
```
['!','#','$','%','&','(',')','*','+',',','-','.','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_',
'A','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
```

2) When the base key is passed in each individual number is translated into binary to obfuscate the actual key used

3) Depending on what key is passed in (the key can only be numeric) the base char list will be shifted the amount of the key.
i.e if 'a' is in index 0 and length of chars list is 82 and if the key is 100 
we shift the char list around by 100, the new index of 'a' will be 18


4) We create an encoding Dictionary that will map each of those characters to a numeric value.
So if we start with index 0 of the base char list '!' to assign this a numeric value we see what the key is.

5) I.e lets say the key is 100 then we do integer division by 2 to obscure the key in the mapping.
We increment the resulting integer by the current index of the char list we are mapping so 
that there is a linear progression of 1 between each char in the list.
So with key 100 the char '!' will be 100 // 2 + 0 = 50, then the next item is '#' which will be 100 // 2 + 1 = 51 and so on

6) After the integer division and the increment we convert the number into octal and then reverse the octal string This is done to further obfuscate the encoding of the character. Then we Add "! !" to the beginning and end 
of the encoded character block. So where we left off with '!' which was 50 it would become octal: 0o62, reversedis 26o0, then add "! !" to front and back, making the character the encoded string of '! !26o0! !'

7) We denote that '~~' in the encoding table will denote a space between each character. so if you have 2 characters '!' and '#' that are '! !26o0! !' and '! !36o0! !' if they were passed in as plaintext '!#' then
the cipher text will be: '! !26o0! !~~! !36o0! !'

8) We convert the final encoded string character by character into hexadecimal. 
The string from the previous step encoded into hex would be: 21202132366f302120217e7e21202133366f30212021
This is produced by each text character being mapped to a decimal code of the ASCII table
then converted from decimal to hex byte i.e 20 in hex denotes a space. The string was converted into hex for further obfuscation, it was felt the more complexity the cipher possessed the less likely it was to be cracked, attempted to be cracked, or increased the time to crack significantly. 

This is an example with a very small key which is very simple to visualize.
If we had a key of length 16 the output would be significantly larger.

## Decryption Methodology
The Decryption is just doing all the steps of the encryption, but in reverse.

1) The base key numbers are translated individually into binary

2) The entire hex string is decoded back into regular string format (UTF-8)

3) The decryption algorithm also has a copy of the base char table
Base Char list:
```
['!','#','$','%','&','(',')','*','+',',','-','.','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
```

4) The key given also shifts the list to normalize the char lists between the encryption and decryption

5) The encoding list is replicated to see what each character was mapped to numerically

6) then the encoding list is reversed as now we are working with the cipher so where '!':'! !26o0!' was the mapping, We will have it reversed as '! !26o0!': '!' so that each char can be reversed back into its original form

## Vulnerabilities
If this was used as a public system where everyone was privy to how the encryption and decryption processes work, then this system is suscepitble to brute force attacks. As they would just have to do all the encryption steps to reverse the text to the point where the base chars list is mapping to that key's relevant octal string. From there they could brute force different rotations of the char list until the mappings produce legible text. 

## How to Run

1) Any [Python](https://www.python.org/downloads/) version ^3.10.5 would be sufficient enough to run this program 

2) This was designed to be run as a command line program open a cli to where you have cloned this directory

3) From here launch main.py and follow the command line prompts that appear

![](encryption.JPG?raw=true) ![](decryption.JPG?raw=true) ![](producedCipher.JPG?raw=true)