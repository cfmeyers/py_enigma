from enigma_string_lib import turn_string_into_int_list, turn_int_list_into_alphabet_string, ALPHABET, snapshot, findInverseMapping

from enigma_data import I,II,III,IV,V,VI,VII,VIII, reflectorB
from enigma_data import testRotorI, testRotorII, testRotorIII 


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


def transform_char_with_rotor(character, rotor, inverse=False, v=False):
    """
    Example:  
    ABCDEFGHIJKLMNOPQRSTUVWXYZ  <--- input
    EKMFLGDQVZNTOWYHXUSPAIBRCJ  <--- output
    
    In the above example, you put in an A, you'll get out an E.  Here the offset is 0.

    Example:  
    ABCDEFGHIJKLMNOPQRSTUVWXYZ  <--- input
    KMFLGDQVZNTOWYHXUSPAIBRCJE  <--- output

    Now when you put in an A you'll get out a J.  The offset is 1.  Notice how all the
    output letters shifted over by 1.

    Note that in the actual code the characters are represented as integers
    (so A is 0, B is 1, C is 2, etc etc)
    """

    offset = rotor["offset"] #an integer between 0 and 25

    if inverse:
        wiring = rotor["inverse-wiring"] 
        # wiring = findInverseMapping(rotor["wiring"])
    else:
        wiring = rotor["wiring"] 

    pointer = abs(character + offset) % 26

    if v: #verbose flag for tracing process of transformation
        print "Through "+rotor["name"]+"\t:"+ALPHABET[character]+"->"+ALPHABET[wiring[pointer]]

    return wiring[pointer]
    

def use_enigma(plaintext, left, middle, right,
               leftOffset=0, middleOffset=0, rightOffset=0):

    leftRotor   = {"wiring"   :left["wiring"],
                   "inverse-wiring":left["inverse-wiring"],
                   "turnover" :left["turnover"],
                   "offset"   :leftOffset,
                   "name"     :"left rotor",
                   "nextRotor":None}

    middleRotor = {"wiring"   :middle["wiring"],
                   "inverse-wiring":middle["inverse-wiring"],
                   "turnover" :middle["turnover"],
                   "offset"   :middleOffset,
                   "name"     :"middle rotor",
                   "nextRotor":leftRotor}

    rightRotor  = {"wiring"   :right["wiring"],
                   "inverse-wiring":right["inverse-wiring"],
                   "turnover" :middle["turnover"],
                   "turnover" :right["turnover"],
                   "offset"   :rightOffset,
                   "name"     :"right rotor",
                   "nextRotor":middleRotor}


    ciphertextNumberList = []
    plaintextNumberList = turn_string_into_int_list(plaintext)

    for character in plaintextNumberList:
        step(rightRotor)
        # snapshot(leftRotor, middleRotor, rightRotor)

        print "TRANSFORMING "+ALPHABET[character].upper()

        character = transform_char_with_rotor(character, rightRotor, v=True)
        character = transform_char_with_rotor(character, middleRotor, v=True)
        character = transform_char_with_rotor(character, leftRotor, v=True)

        print "Through Reflector \t:"+ALPHABET[character]+"->"+ALPHABET[reflectorB[character]]
        character = reflectorB[character]

        character = transform_char_with_rotor(character, leftRotor, inverse=True,v=True)
        character = transform_char_with_rotor(character, middleRotor,inverse=True,v=True)
        character = transform_char_with_rotor(character, rightRotor,inverse=True,v=True)

        ciphertextNumberList.append(character)



    print turn_int_list_into_alphabet_string(ciphertextNumberList).upper()

    
# use_enigma("a",III,II,I)
# use_enigma("p",III,II,I)
# use_enigma("w",III,II,I,0,0,0)

# use_enigma("a",III,IV,I,3,7,6)
# use_enigma("w",III,IV,I,3,7,6)
# use_enigma("a",III,II,I)
# use_enigma("n",III,II,I)

use_enigma("a", testRotorIII, testRotorII, testRotorI, 1,1,1)
use_enigma("l", testRotorIII, testRotorII, testRotorI, 1,1,1)
# use_enigma("f", testRotorIII, testRotorII, testRotorI)

# print "I"
# print turn_int_list_into_alphabet_string(findInverseMapping(I["wiring"])).upper()
# print "UWYGADFPVZBECKMTHXSLRINQOJ"

# print "II"
# print turn_int_list_into_alphabet_string(findInverseMapping(II["wiring"])).upper()
# print "AJPCZWRLFBDKOTYUQGENHXMIVS"

# print "III"
# print turn_int_list_into_alphabet_string(findInverseMapping(III["wiring"])).upper()
# print "TAGBPCSDQEUFVNZHYIXJWLRKOM"

# print "IV"
# findInverseMapping(IV["wiring"])

# print "V"
# findInverseMapping(V["wiring"])

# print "VI"
# findInverseMapping(VI["wiring"])

# print "VII"
# findInverseMapping(VII["wiring"])

# print "VIII"
# findInverseMapping(VIII["wiring"])







   