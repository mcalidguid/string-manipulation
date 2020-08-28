def swap_case(sentence):
    output = ""
    for letter in sentence:
        if letter == letter.upper():
            output += letter.lower()
        else:
            output += letter.upper()
    print(">>>: %s" % output)


def reverse_swap_words(sentence):
    output = ""
    for letter in sentence:
        if letter == letter.upper():
            output += letter.lower()
        else:
            output += letter.upper()
    result_words = output.split()
    reverse_words = " ".join(reversed(result_words))
    print(">>>: %s" % reverse_words)


def split_and_join(sentence):
    sentence = sentence.split(" ")
    output = "-".join(sentence)
    print(">>>: %s" % output)


while True:
    print("""---------------------------------------------------------------
    Select an option for String Manipulation:
        Enter \"1\" for Swap
        Enter \"2\" for Reverse & Swap
        Enter \"3\" for Split & Join
        Enter \"q\" to quit""")
    user_input = input(">>>: ")

    if user_input == "q":
        print(">>>: Danke, tschüss!~")
        break

    elif user_input == "1":
        print("You selected \'Swap\'"
              "\nThis will swap the case of all letters in the string")
        print("Input the string:")
        words = input(">>>: ")
        swap_case(words)

    elif user_input == "2":
        print("You selected \'Reverse & Swap\'"
              "\nThis will reverse the word order and swap the case of all letters in the string")
        print("Input the string:")
        words = input(">>>: ")
        reverse_swap_words(words)

    elif user_input == "3":
        print("You selected \'Split & Join\'"
              "\nThis will split the string on a space delimiter and join using a hyphen")
        print("Input the string:")
        words = input(">>>: ")
        split_and_join(words)

    else:
        print(">>>: Invalid input")
