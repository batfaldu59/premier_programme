
# Premier programme

"""
fORMATION python
udemy
"""


def demander_nom():
    nom_user = ""
    while nom_user == "":
        nom_user = input("Quel est votre nom ? ")
    return nom_user


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne+": quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: vous devez renseigner un age valide!!!")
    return age_int


def afficher_information_personne(nom_personne, age_personne, taille=0):
    print()
    print("Vous vous appellez " + nom_personne + ", vous avez " + str(age_personne) + " ans")
    print("L'an prochain vous aurez " + str(age_personne + 1) + " ans")

    if age_personne == 17:
        print("Vous êtes presque majeur")
    elif age_personne == 18:
        print("Tout juste majeur, félicitation")
    elif age_personne > 60:
        print("Vous êtes sénior")
    elif age_personne > 18:
        print("Vous êtes majeur")
    elif age_personne < 10:
        print("Vous êtes enfant")
    else:
        print("Vous êtes mineur")

    if not taille == 0:
        print("Vous mesurez "+str(taille)+" m")


NOMBRE_PERSONNE = 1

for i in range(NOMBRE_PERSONNE):
    nom = "Personne "+str(i+1)
    age = demander_age(nom)
    afficher_information_personne(nom, age, 1.86)

