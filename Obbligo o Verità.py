# IMPORAZIONE
import os
import random


# CONTROLLO FILE
if os.path.exists("Obblighi.txt"):
    print()
else:
    Ob = open("Obblighi.txt","w")
    BaseOb = "Scrivi un obbligo per ogni rigo: "
    Ob.write(BaseOb)
    Ob.close

if os.path.exists("Verità.txt"):
    print()
else:
    Vr = open("Verità.txt","w")
    BaseVr = "Scrivi una verità per ogni rigo: "
    Vr.write(BaseVr)
    Vr.close


# CONTEGGIO DOMANDE
Obl = 0
Ob = open("Obblighi.txt", "r")
for linea in Ob:
    Obl += 1
Obl = Obl - 1
Ob.close

Vrt = 0
Vr = open("Verità.txt", "r")
for linea in Vr:
    Vrt += 1
Vrt = Vrt - 1
Vr.close


# AVVISI INIZIALI
os.system("cls")
print("Benvenuto/a a obbligo o verità")
print("Creato da Samu369 (https://github.com/Samu369/Obbligo-Verita)")
print("\n Prima di iniziare a giocare devi avere scritto un elenco degli obblighi e delle verità nei file Obblighi.txt e Verità.txt presenti nella cartella insieme al programma. \n Lo hai fatto? [si/no]   (tutto minuscolo)")
Step1 = input()
if(Step1 == "no"):
    os.system("cls")
    print("Per iniziare a giocare dovrai scrivere alcuni obblighi e verità nei file Obblighi.txt e Verità.txt presenti in questa cartella, dopo averlo fatto riavvia il prigramma \n Se hai bisogno di aiuto consulta la documentazione presente a questo link: \n https://github.com/Samu369/Obbligo-Verita/blob/9babc0cc4102cc752312f027b85fcf5caf94e945/Documentazione.md ")
    os.system("pause")
    quit()
else:
    print("Perfetto! Allora iniziamo!")
    print("Hai scritto:")
    Obl_str = str(Obl)
    Vrt_str = str(Vrt)
    print(Obl_str + "  Obblighi")
    print(Vrt_str + "  Verità")
os.system("pause")
os.system("cls")



# GIOCO
while True:
    print("Obbligo o Verità? [o/v]   (tutto minuscolo)")
    D1 = input()
    if(D1 == "o"):
        A = open("Obblighi.txt","r")
        N = random.randint(1, Obl)
        print(A.readlines()[N])
        A.close
        os.system("pause")
        os.system("cls")
    else:
        A = open("Verità.txt","r")
        N = random.randint(1, Vrt)
        print(A.readlines()[N])
        A.close
        os.system("pause")
        os.system("cls")