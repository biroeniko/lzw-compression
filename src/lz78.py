''' 
MIT License

Copyright (c) 2018 Biro Eniko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import sys

def longest_common_substring(s1, s2):
    # go along the first string and search for the longest match
    maxLongest = 0
    offset = 0
    for i in range(0, len(s1)):
        longest = 0
        if ((i == len(s1) - len(s2) - 2)):
            break            
        for j in range(0, len(s2)):
            if (i+j < len(s1)):
                if s1[i+j] == s2[j]:
                    longest = longest + 1
                    if (maxLongest < longest):
                        maxLongest = longest
                        offset = i
                else:
                    break
            else:
                break
    return maxLongest, offset

    
def encode_lz78(text):
    dictionary = dict()
    i = 0
    index = 1
    encodedNumbers = []
    encodedLetters = []
    while i < len(text):
        stringToBeSaved = text[i]
        indexInDictionary = 0
        while stringToBeSaved in dictionary:
            indexInDictionary = dictionary[stringToBeSaved]
            if (i == len(text) - 1):
                stringToBeSaved = " "
                break
            i = i + 1
            stringToBeSaved = stringToBeSaved + text[i]
        #print ("<{0}, {1}>".format(indexInDictionary, stringToBeSaved[len(stringToBeSaved) - 1]))
        encodedNumbers.append(indexInDictionary)
        encodedLetters.append(stringToBeSaved[len(stringToBeSaved) - 1])
        if (stringToBeSaved not in dictionary):
            dictionary[stringToBeSaved] = index
            index = index + 1
        i = i + 1

    return encodedNumbers, encodedLetters, dictionary
        
def decode_lz78(encodedNumbers, encodedLetters, dictionary):
    i = 0
    while i < len(encodedNumbers):
        if (encodedNumbers[i] != 0):    
            print(list(dictionary.keys())[list(dictionary.values()).index(encodedNumbers[i])], end="")
        print(encodedLetters[i], end="")
        i = i+1
    print('\n')

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        exit("You must specify the text which will be encoded! (Run with python3 lz77.py abracadabra)")
    stringToEncode = ' '.join(sys.argv[1:2])
    [encodedNumbers, encodedLetters, dictionary] = encode_lz78(stringToEncode)
    print("Encoded string: ", end="")
    i = 0
    while i < len(encodedNumbers):
        print ("<{0}, {1}>".format(encodedNumbers[i], encodedLetters[i]), end=" ")
        i = i + 1
    print('\n')
    print("Decoded string: ", end = "")
    decode_lz78(encodedNumbers, encodedLetters, dictionary)
            