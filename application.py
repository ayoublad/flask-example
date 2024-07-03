from flask import Flask # type: ignore
from random import*

application = Flask(__name__)

@application.route('/')
def hello_world():
    
    NG = 0
    NP = 0
    MS = 0
    continuer=1
    while(continuer==1):
        a=randint (1,100)
        b=int(input("Saisir un entier entre 1 et 100"))
        n = 1
        while (b!=a) and (n < 10) :
            if (b<a):
                print("trop petit")
                n = n + 1
                b=int(input("Saisir un entier :"))
            elif (b>a):
                print("trop grand")
                n = n + 1
                b=int(input("Saisir un entier :"))
        if (b==a):
            print("Félicitations, le nombre etait",a,".")
            NG=NG+1
            MS=NG
        else:
            print("Perdu, le nombre était :",a, ",")
            print("Désolé, vous avez épuisé vos", n, "tentatives")
            NP=NP+1

        continuer=int(input("Si vous voulez rejouer tapez 1 si non tapez 2")) 
    print("Vous avez gagné", NG, "parties.", "Vous avez perdu", NP, "parties, ", "Votre meilleur score est :",MS)
    
    #return 'Je suis en stage chez Capgemini. [MAJ] Cela fait plus de deux semaines.'