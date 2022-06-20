import random

small_chars = "abcdefghijklmnopqrstuvwxyz"
big_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "*&^%$#@!?"
random_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*&^%$#@!?" 

psswd_state = ("enter a to generate password using small letters. \n"
"enter b to generate password using capital letters. \n"
"enter c to generate password using special characters. \n"
"enter any letter to generate password using random letters AND special characters.")

print(psswd_state)
user_inp = str(input(": "))

if (user_inp.isalpha()) == True:
    psswd_count = int(input("specify the total number of passwords that need to be generated: "))
    psswd_len = int(input("specify the required length for your password: "))

    for i in range(0, psswd_count):
        result  = ""
        
        for j in range(0, psswd_len):
            if user_inp == "a":
                psswd_char = random.choice(small_chars)
                result = result + psswd_char

            elif user_inp == "b":
                psswd_char = random.choice(big_chars)
                result = result + psswd_char

            elif user_inp == "c":
                psswd_char = random.choice(special_chars)
                result = result + psswd_char 

            else:
                psswd_char = random.choice(random_chars)
                result = result + psswd_char    

        print("The Generated Password is : ", result)

else:
    print("wrong input")            
