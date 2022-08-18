# IMPORAZIONE
import os
import random


# CONTROLLO FILE
if os.path.exists("Obblighi.txt"):
    print()
else:
    Ob = open("Obblighi.txt","w")
    BaseOb = "Scrivi 5 obblighi qua sotto (uno per ogni riga): "
    Ob.write(BaseOb)
    Ob.close

if os.path.exists("Verità.txt"):
    print()
else:
    Vr = open("Verità.txt","w")
    BaseVr = "Scrivi 5 verità qua sotto (uno per ogni riga): "
    Vr.write(BaseVr)
    Vr.close


# AVVISI INIZIALI
os.system("cls")
print("Benvenuto/a a obbligo o verità")
print("Creato da Samu369 (https://github.com/Samu369/Obbligo-Verita)")
print("\n Prima di iniziare a giocare devi avere scritto un elenco degli obblighi e delle verità nei file Obblighi.txt e Verità.txt presenti nella cartella insieme al programma. \n Lo hai fatto? [si/no]   (tutto minuscolo)")
Step1 = input()
if(Step1 == "no"):
    os.system("cls")
    print("Per iniziare a giocare dovrai scrivere tutti gli obblighi e verità richiesti dalla tua edizione (in questo caso 5) dopo averlo fatto riavvia il prigramma \n Se hai bisogno di aiuto consulta la documentazione presente a questo link: \nhttps://github.com/Samu369/Obbligo-Verita/blob/03d5ce78e9b1930d4a11787527c945f221aca8e3/Documentazione.md ")
    os.system("pause")
    quit()
else:
    print("Perfetto! Allora iniziamo!")
os.system("pause")
os.system("cls")




# GIOCO
while True:
    print("Obbligo o Verità? [o/v]   (tutto minuscolo)")
    D1 = input()
    if(D1 == "o"):
        A = open("Obblighi.txt","r")
        N = random.randint(1, 5)
        print(A.readlines()[N])
        A.close
        os.system("pause")
        os.system("cls")
    else:
        A = open("Verità.txt","r")
        N = random.randint(1, 5)
        print(A.readlines()[N])
        A.close
        os.system("pause")
        os.system("cls")