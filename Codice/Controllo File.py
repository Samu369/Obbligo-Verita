# IMPORAZIONE
import os
import random

# CONTROLLO FILE
if os.path.exists("Obblighi.txt"):
    print()
else:
    Ob = open("Obblighi.txt","w")
    BaseOb = "Scrivi 10 obblighi qua sotto (uno per ogni riga): "
    Ob.write(BaseOb)
    Ob.close

if os.path.exists("Verità.txt"):
    print()
else:
    Vr = open("Verità.txt","w")
    BaseVr = "Scrivi 10 verità qua sotto (uno per ogni riga): "
    Vr.write(BaseVr)
    Vr.close