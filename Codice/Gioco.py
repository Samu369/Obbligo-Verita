# IMPORAZIONE
import os
import random

# GIOCO
while True:
    print("Obbligo o Verità? [o/v]   (tutto minuscolo)")
    D1 = input()
    if(D1 == "o"):
        A = open("Obblighi.txt","r")
        N = random.randint(1, 10)
        print(A.readlines()[N])
        A.close
        os.system("pause")
        os.system("cls")
    else:
        A = open("Verità.txt","r")
        N = random.randint(1, 10)
        print(A.readlines()[N])
        A.close
        os.system("pause")
        os.system("cls")