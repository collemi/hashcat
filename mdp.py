alph = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"

#aaaa1111
with open("passwd.txt","a") as file:
    for letter1 in alph:
        for letter2 in alph:
            for letter3 in alph:
                for letter4 in alph:
                    for nb1 in num:
                        for nb2 in num:
                            for nb3 in num:
                                for nb4 in num:
                                    file.write(f"{letter1}{letter2}{letter3}{letter4}{nb1}{nb2}{nb3}{nb4}\n")
        print(letter1)