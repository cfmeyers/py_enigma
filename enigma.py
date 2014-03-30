
# rotor1 = {"wiring": I,  "turnover":turnoverI,   "offset":start1, "position":1}
def step(rotor):
    """This function steps the rotor.  It advances the rotor and (if needed) steps next roter"""

    #advance this rotor by 1 (mod 26 for alphabet wrap-around)
    rotor["offset"] = (rotor["offset"] + 1) % 26

    #check if there is another rotor after this one (i.e. if this is first or second rotor)
    if rotor["nextRotor"]:
        #check if this rotor is at a turnover position
        if rotor["offset"] in rotor["turnover"]:
            #if it is at a turnover position, call step on the next rotor
            step(rotor["nextRotor"])

def transform_char_with_rotor(character, rotor):
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

    wiring = rotor["wiring"] #list of 26 integers (0-25, order given by wiring table)

    pointer = abs(character - offset) % 26

    return wiring[pointer]
    

    

# Reflector
reflectorB = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19] 

otherreflector = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

# Rotors
I = [ 4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9 ] 

II = [ 0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4 ] 

III = [ 1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14 ] 

IV = [ 4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1 ] 

V = [ 21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10 ] 

VI = [ 9, 15, 6, 21, 14, 20, 12, 5, 24, 16, 1, 4, 13, 7, 25, 17, 3, 10, 0, 18, 23, 11, 8, 2, 19, 22 ] 

VII = [ 13, 25, 9, 7, 6, 17, 2, 23, 12, 24, 18, 22, 1, 14, 20, 5, 0, 8, 21, 11, 15, 4, 10, 16, 3, 19 ] 

VIII =  [ 5, 10, 16, 7, 19, 11, 23, 14, 2, 1, 9, 18, 15, 3, 25, 17, 0, 12, 4, 22, 13, 8, 20, 24, 6, 21 ] 

turnoverI    = [24] #Y
turnoverII   = [12] #M
turnoverIII  = [3] #D
turnoverIV   = [17] #R
turnoverV    = [7] #H
turnoverVI   = [7,20] #H and U
turnoverVII  = [7,20] #H and U
turnoverVIII = [7,20] #H and U

# start1 = 0
# start2 = 0
# start3 = 0

# rotor1 = {"wiring": III,"turnover":turnoverIII, "offset":start1, "nextRotor":None}
# rotor2 = {"wiring": II, "turnover":turnoverII,  "offset":start2, "nextRotor":rotor1}
# rotor3 = {"wiring": I,  "turnover":turnoverI,   "offset":start3, "nextRotor":rotor2}

offset1 = 3
offset2 = 7
offset3 = 6

rotor1 = {"wiring": III,"turnover":turnoverIII, "offset":offset1, "nextRotor":None}
rotor2 = {"wiring": IV, "turnover":turnoverIV,  "offset":offset2, "nextRotor":rotor1}
rotor3 = {"wiring": I,  "turnover":turnoverI,   "offset":offset3, "nextRotor":rotor2}



plaintext = "a"
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_to_int = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

plaintextNumberList = []
ciphertextNumberList = []

# for character in plaintext:
for character in plaintext:
    plaintextNumberList.append(alphabet_to_int[character])
    
ciphertext = ""

def snapshot():
    print rotor1["offset"], rotor2["offset"], rotor3["offset"]




for ptCharInt in plaintextNumberList:
    snapshot()

    # pt -> R3
    charThruRotor3 = transform_char_with_rotor(ptCharInt, rotor3)
    print "Through Rotor3   :",alphabet[charThruRotor3]

    # R3 -> R2
    charThruRotor2 = transform_char_with_rotor(charThruRotor3, rotor2)
    print "Through Rotor2   :",alphabet[charThruRotor2]

    # R2 -> R1
    charThruRotor1 = transform_char_with_rotor(charThruRotor2, rotor1)
    print "Through Rotor1   :",alphabet[charThruRotor1]

    # R1 -> reflector
    charThruReflector = reflectorB[charThruRotor1]
    print "Through Reflector:",alphabet[charThruReflector]

    # reflector -> R1
    reflectedCharThruRotor1 = transform_char_with_rotor(charThruReflector, rotor1)
    print "Through Rotor1   :",alphabet[reflectedCharThruRotor1]

    # R1 -> R2
    reflectedCharThruRotor2 = transform_char_with_rotor(reflectedCharThruRotor1, rotor2)
    print "Through Rotor2   :",alphabet[reflectedCharThruRotor2]

    # R2 -> R3
    reflectedCharThruRotor1 = transform_char_with_rotor(reflectedCharThruRotor2, rotor1)
    print "Through Rotor3   :",alphabet[reflectedCharThruRotor3]


    ciphertextNumberList.append(reflectedCharThruRotor1)
    
    step(rotor3)


def turn_int_list_into_alphabet_string(intlist):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newString = ""
    for num in intlist:
        newString += alphabet[num]

    return newString



print turn_int_list_into_alphabet_string(ciphertextNumberList).upper()

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# alphamap = {}
# for i,letter in enumerate(alphabet):
    # alphamap[i] = letter



# for num in reflectorB:
    # print num, alphamap[num]
    