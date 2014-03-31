
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

ALPHABET_MAP = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

def turn_string_into_int_list(text):

    numberList = []
    for character in text:
        numberList.append(ALPHABET_MAP[character])

    return numberList

def turn_int_list_into_alphabet_string(intlist):
    newString = ""
    for num in intlist:
        newString += ALPHABET[num]

    return newString

def snapshot(leftRotor, middleRotor, rightRotor):
    print leftRotor["offset"], middleRotor["offset"], rightRotor["offset"]

def findInverseMapping(regWiring, printing=True):
    invertedWiring = []

    for x in range(26):
        for i, char in enumerate(regWiring):
            if char == x:
                invertedWiring.append(i)

    if printing:
        # print turn_int_list_into_alphabet_string(invertedWiring).upper()
        for i,x in enumerate(invertedWiring):
            if i == 0:
                print "["+str(x)+",",
            elif i != 25:
                print str(x)+",",
            else:
                print str(x)+"]"

    return invertedWiring



