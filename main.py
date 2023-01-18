# Restored English Texts
# ----------------------------------------------------------
# The open design principle increases confidence in security
# ----------------------------------------------------------
# Learning how to write secure software is a necessary skill
# ----------------------------------------------------------
# Secure key exchange is needed for symmetric key encryption
# ----------------------------------------------------------
# Security at the expense of usability could damage security
# ----------------------------------------------------------
# Modern cryptography requires careful and rigorous analysis
# ----------------------------------------------------------
# Address randomization could prevent malicious call attacks
# ----------------------------------------------------------
# It is not practical to rely solely on symmetric encryption
# ----------------------------------------------------------
# I shall never reuse the same password on multiple accounts

permutations = []  # List of lists of permutations


def xor_ciphers():  # XORing ciphers
    for i in range(0, len(myList)):  # Iterating over list of input
        # print("Message " + str(i) + " Permutations")
        permutations.append([])  # permutations is a list of lists
        for j in range(0, len(myList)):  # Iterating again over the list of input
            if i != j:
                xor_output = hex(int(myList[i], 16) ^ int(myList[j],
                                                          16))  # converting string to hex then xoring and converting to hex
                xor_output = xor_output[2:]  # removing 0x
                if len(xor_output) < len(myList[i]):  # if the length of the output smaller than the actual length
                    xor_output = xor_output.zfill(len(myList[i]))  # padding is done
                permutations[-1].append(xor_output)  # appending to last list
                # print_with_spaces(xor_output)
    # print(permutations)


restored_spaces = []


def search_for_spaces():  # searching for spaces
    # permutations is a list of lists => [[msg 1+msg2,msg1+msg3,...],[msg2+msg1,msg2+msg3,..],...]
    for i in range(0, len(permutations)):  # iterating through all permutations
        j = 0
        myStr = ""
        for k in range(0, len(permutations[i][j]), 2):
            # step 2 because one byte is 2 hexadecimal so the check is on 2 hexadecimals
            isSpace = 1
            for j in range(0, len(permutations[i])):
                # iterating on a certain permutation list for example msg1 permutations
                # permutations[i][j][k:k + 2] check all j position in msg1+msg2,msg1+msg3,... (for example: all msg1 permutations)
                if permutations[i][j][k:k + 2] <= '40' and permutations[i][j][k:k + 2] != '00':  # not a space
                    isSpace = 0
                    break
            if isSpace == 1:
                myStr += "20"  # add space(hex) to str
            else:
                myStr += "xx"  # add a don't care
        restored_spaces.append(myStr)


# if space is found then one byte is restored for each message
def restore_messages():  # restoring hex using spaces
    # the idea here is to use j to know from which list of permutation did the space come from
    # for example if the byte space is from msg7 then msg7+msg1 , msg7+msg2,.... will be brought to restore the corresponding characters
    j = 0
    for k in range(0, len(restored_spaces[j]), 2): # iterating with step 2 on restored spaces
        isSpace = 0
        for j in range(0, len(restored_spaces)): # This loop check for spaces
            # j will be used with permutations since it will tell from which permutations the space is generated
            if restored_spaces[j][k:k + 2] == "20":  # if it is a space then add it
                restored_english_sentences[j] += " "  # adding a space in the message bec this msg has a space in it
                isSpace = 1
                break
        if isSpace == 1:
            permutationIndex = 0  # index for m1+m2 , m1+m3,....
            english_index = 0  # index for the restored_english_sentences
            while permutationIndex < len(permutations[j]):
                if english_index != j:
                    xor_output = hex(int(permutations[j][permutationIndex][k:k + 2], 16) ^ int("20",
                                                                                16))  # To restore correct case of the letter, xor with "20 Hex" space
                    xor_output = xor_output[2:]  # removing 0x
                    bytes_array = bytes.fromhex(xor_output)  # converting to hex
                    ascii_str = bytes_array.decode()  # then decoding to ascii
                    restored_english_sentences[english_index] += ascii_str  # concatenating in a sentence english_index
                    permutationIndex += 1
                english_index += 1
        else:
            for p in range(0, len(permutations)): # loop to add ? for unknown letters
                restored_english_sentences[p] += "?"  # symbol for unknown letters


def print_with_spaces(my_string):
    for i in range(0, len(my_string), 2):
        print(my_string[i:i + 2], end=" ")
    print("")


if __name__ == '__main__':
    myList = [
        "68AF0BEF7F39982DA975B5E6D06947E61C22748C94A2155CFCCC464DEAFB6F4844DB2D7312ED192B6B7251580C61D5A296964E824A16648B16B9",
        "70A20FBD7E209324A979BFE2997A46E61B22749692EB1655FA995D46A9FA654F43C93F2114A21E3E227714580A6790B88BD74F9E09107D8B0EAC",
        "6FA20DBA622CDD28EC68F0F0C16D41A7023778C29EB8455EFC894B46EDA96C46459E2D2A1CEF1239707F571604618CEB9DD85E955013628B0DAE",
        "6FA20DBA6220893AA970A4B5CD664CE609286D8799B80010F68A0F56FAE868405BD72A2A51E118386E7214520E6994AC9D964E824A16648B16B9",
        "71A80AAA6227DD20FB68A0E1D6695BA71C3864C285AE1445F09E4A50A9EA6B5B52D82B3F51E3192922645D5100769ABE8B965C89480F6F910BB3",
        "7DA30ABD753A8E63FB70BEF1D66340BC0D24748D99EB065FEC804B03F9FB6F5F52D02A731CE31B24617F5B431C2496AA94DA1D865D17778109B3",
        "75B34EA66369932CFD31A0E7D86D5DAF0F3171C283A44542FC805603FAE6664C5BC77E3C1FA204346F7B51421D6D96EB9DD85E955013628B0DAE",
        "75E71DA771259163E774A6F0CB2E5BA3192378C283A30010EA8D4246A9F96B5A44C9312115A21823227B415A1B6D85A79D965C844A0C638C16B3",
    ]
    xor_ciphers()
    search_for_spaces()
    # print("Spaces Location")
    # for r in range(0, len(restored_spaces)):
    #     print_with_spaces(restored_spaces[r])
    restored_english_sentences = ["" for i in range(len(permutations))]

    restore_messages()
    print()
    print("Restored English")
    for r in range(0, len(restored_english_sentences)):
        print("----------------------------------------------------------")
        print(restored_english_sentences[r])

    # Description:
    # First: XOR c1 with c2,c3,...,c8 (if xor give less than 8 bits then padding is done using zfill) and repeat for all ciphers
    # Second: Search for space is Done. In this part, The search was done by checking if every byte(two hexadecimal) of c1+c2,c1+c3,...c1+c8 satisfy two conditions:
    # 1) This byte is larger than 40 in all c1+c2,c1+c3,....
    # 2) This byte is larger than 40 or is equal to zero in all c1+c2,c1+c3,....
    # If any byte satisfies these conditions then it will be definitely a space (below some examples that i made to make the condition)
    # ex: the column which have brackets( ) is definitely a space as all is larger than 40, also the column which have brackets[] is definitely a space as all is larger than 40 or equal to zero
    # 18 0d 04 (52) 01 19 0b 09 [00] 0c 0a 04 49 13 01 [00] 07 00 00 1a 06 49 03 09 06 (55) 1b 0b 43 01 0a 07 07 12 12 [52] 06 4f 07 15 49 05 45 00 06 06 (45) 1a 1d [41] 01 1c 43 06 19 00 18 15
    # 07 0d 06 (55) 1d 15 45 05 [45] 1d 45 16 11 04 06 [41] 1e 15 0c 4e 0a 1a 50 02 00 (45) 0d 0b 07 52 03 0e 01 45 00 [59] 0e 02 0b 12 1b 0d 06 4e 08 00 (59) 49 0b [4e] 10 17 1a 05 06 00 1b 17
    # 07 0d 06 (55) 1d 19 11 17 [00] 05 11 53 1d 0f 0b [00] 15 0a 19 0b 0d 1a 15 4c 0a (46) 49 1b 10 13 07 08 1f 0c 07 [59] 43 0c 01 13 05 00 45 0a 02 08 (41) 0e 0b [00] 00 00 00 00 00 00 00 00
    # 19 07 01 (45) 1d 1e 45 0d [52] 1d 15 07 06 00 1c [41] 00 1a 10 4e 11 0c 01 19 0c (52) 0c 1d 43 11 04 13 16 03 06 [4c] 43 0e 00 02 49 16 0c 09 0c 17 (4f) 1c 1d [00] 12 0b 02 19 0b 1a 1d 0a
    # 15 0c 01 (52) 0a 03 16 4e [52] 05 0b 17 06 0a 07 [5a] 11 06 00 01 0d 49 13 03 10 (4c) 0d 4e 13 00 00 17 16 0b 07 [00] 0e 0e 02 0f 0a 0d 0a 1b 10 45 (43) 08 02 [4c] 53 04 17 01 13 0a 1f 0a
    # 1d 1c 45 (49) 1c 50 0b 01 [54] 44 15 01 08 04 1a [49] 13 13 05 4e 17 06 50 1e 00 (4c) 10 4e 10 1d 09 04 1f 1c 53 [4f] 0d 4f 1d 1f 04 09 00 1a 11 0c (43) 49 0b [4e] 10 17 1a 05 06 00 1b 17
    # 1d 48 16 (48) 0e 1c 09 4e [4e] 01 13 16 1b 47 1c [45] 05 01 0c 4e 17 01 15 4c 16 (41) 04 0b 43 02 04 12 00 12 1c [52] 07 4f 01 08 49 09 10 02 17 0c (50) 05 0b [00] 12 06 00 1a 07 07 00 0a
    # Third: After getting all spaces, it will be used to get corresponding character for example if i knew the byte that is a space in msg1 then i can get the character of
    # this byte in other messages for example if a byte of msg1 + msg2 = 48 and msg1 is a space then this byte in msg2 is 48 xor 20 = 68
    # Fourth: After this, hexadecimal will be converted to ascii and guessing the remaining letters will be easy. for example if i wasn't able to guess a word in msg2 but i know
    # the same bytes in msg1 then i can simply xor msg1 with the msg1+msg2 which will produce msg2 bytes

    # Examples on space to make a rule => TODO: Required: check if in msg0 xor with all messages if there is 00 and they are all larger than 40 or if they are all larger than 40
    # space = "20"
    # test = "68"  # small h
    # print(hex(int(test, 16)))
    # print(hex(int(space, 16) ^ int(test, 16)))  # now capital H
    # print()
    #
    # test = "48"  # capital h
    # print(hex(int(test, 16)))
    # print(hex(int(space, 16) ^ int(test, 16)))  # now small h
    # print()
    #
    # test1 = "48"  # capital h
    # test2 = "46"  # capital f
    # print(hex(int(test1, 16)))
    # print(hex(int(test2, 16)))
    # print(hex(int(test1, 16) ^ int(test2, 16)))  # control character
    # print()
    #
    # test1 = "68"  # small h
    # test2 = "66"  # small f
    # print(hex(int(test1, 16)))
    # print(hex(int(test2, 16)))
    # print(hex(int(test1, 16) ^ int(test2, 16)))  # control character
    # print()
    #
    # test1 = "48"  # capital h
    # test2 = "66"  # small f
    # print(hex(int(test1, 16)))
    # print(hex(int(test2, 16)))
    # print(hex(int(test1, 16) ^ int(test2, 16)))  # control character
    # print()
