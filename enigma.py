from enigma_string_lib import turn_string_into_int_list, turn_int_list_into_alphabet_string, ALPHABET, snapshot, findInverseMapping, build_stepping_list

from enigma_data import I,II,III,IV,V,VI,VII,VIII, reflectorB


def step(rotor):
    """
    This function steps the rotor.
    It advances the rotor and (if needed) steps next roter
    """
    offset = rotor["offset"]

    #advance this rotor by 1 (mod 26 for alphabet wrap-around)
    rotor["offset"] = (offset + 1) % 26

    #check if there is another rotor after this one (i.e. if this is first or second rotor)
    if rotor["nextRotor"]:
        #check if this rotor is at a turnover position
        if rotor["offset"] in rotor["turnover"]:
            #if it is at a turnover position, call step on the next rotor
            step(rotor["nextRotor"])


def transform_char_with_rotor(charIndex, rotor, inverse=False, v=True):
    """
    Maps rotor input (a character represented by an integer between 0 and 25)
    to rotor output (also a character represented by an integer between 0 and 25).
    """
   
    offset = rotor["offset"] 
    wiring = rotor["wiringList"][offset]
    newCharIndex = wiring[charIndex]
    # newCharIndex = (wiring[charIndex] - 1)  % 26

    if inverse:
        wiring = findInverseMapping(wiring, printing=False)
        newCharIndex = wiring[charIndex]
        # newCharIndex = (wiring[charIndex] + 1)  % 26


    if v: #verbose flag for tracing process of transformation
        print("Through "+rotor["name"]+"\t:"+
              ALPHABET[charIndex]+"->"+ALPHABET[newCharIndex])

    return newCharIndex



def use_enigma(plaintext, left, middle, right,
               leftOffset=0, middleOffset=0, rightOffset=0):
    """
    Models the 3 rotors as simple dictionaries
           -  turnover  - list of indices where rotor will cause next rotor to increment                          1 space
           -  offset    - corresponds to the letters on the dials with original enigma
           -  name      - either left, middle, or right rotor
           -  nextRotor - indicates the rotor to this rotor's left
           -  wiringList- list of each possible list of mappings for this rotor
                          e.g. for a rotor whose mapping list (when the dial is turned
                          to A) is [3,0,1,2] would have a wiringList of
                          [[3,0,1,2], [0,1,2,3], [1,2,3,0], [2,3,0,1]]
    
    """


    leftRotor   = {
                   "wiringList": build_stepping_list(left["wiring"]),
                   "turnover" :left["turnover"],
                   "offset"   :leftOffset,
                   "name"     :"left rotor",
                   "nextRotor":None}

    middleRotor = {
                   "wiringList": build_stepping_list(middle["wiring"]),
                   "turnover" :middle["turnover"],
                   "offset"   :middleOffset,
                   "name"     :"middle rotor",
                   "nextRotor":leftRotor}

    rightRotor  = {
                   "wiringList": build_stepping_list(right["wiring"]),
                   "turnover" :right["turnover"],
                   "offset"   :rightOffset,
                   "name"     :"right rotor",
                   "nextRotor":middleRotor}


    plaintextNumberList = turn_string_into_int_list(plaintext)
    ciphertext = ""

    for charIndex in plaintextNumberList:
        step(rightRotor)
        #steps after the key is pressed but before signal is sent to the first rotor
        snapshot(leftRotor, middleRotor, rightRotor)

        print "TRANSFORMING "+ALPHABET[charIndex].upper()

        #Through the rotors moving left
        charIndex = transform_char_with_rotor(charIndex, rightRotor)
        charIndex = transform_char_with_rotor(charIndex, middleRotor)
        charIndex = transform_char_with_rotor(charIndex, leftRotor)

        print "Through Reflector \t:"+ALPHABET[charIndex]+"->"+ALPHABET[reflectorB[charIndex]]

        charIndex = reflectorB[charIndex] #through the reflector

        #Through the rotors moving right (so must invert the mappings)
        charIndex = transform_char_with_rotor(charIndex, leftRotor, inverse=True)
        charIndex = transform_char_with_rotor(charIndex, middleRotor,inverse=True)
        charIndex = transform_char_with_rotor(charIndex, rightRotor,inverse=True)

        #Process is finished for this character
        ciphertext+= ALPHABET[charIndex]

    print ciphertext.upper()

    return ciphertext

    
use_enigma("a",I,II,III,0,0,0)
use_enigma("d",I,II,III,0,0,0)



# ct = use_enigma("a",I,II,III,0,0,0)[0]
# ct = use_enigma("a",III,IV,I,3,7,6)[0]
# ct = use_enigma("a",III,IV,I,0,0,1)[0]
# ct = ALPHABET[ct]
# use_enigma(ct,III,IV,I,3,7,6)
# use_enigma(ct,I,II,III,0,0,0)


