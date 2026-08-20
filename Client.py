class Client:
    def __init__(self, nom: str, prenom: str, num_tel, adresse: str):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_tel = num_tel
        self.__adresse = adresse

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_num(self):
        return self.__num_tel

    def get_adresse(self):
        return self.__adresse

    def SaisieIncorrecte(self):
        # Validation du nom (lettres uniquement)
        while not str(self.__nom).replace(" ", "").isalpha():
            print("Le nom saisi est incorrect : écrivez en lettres.")
            self.__nom = input("Saisissez le nom : \n")
        
        # Validation du prénom (lettres uniquement)
        while not str(self.__prenom).replace(" ", "").isalpha():
            print("Le prénom saisi est incorrect : écrivez seulement en lettres.")
            self.__prenom = input("Saisissez le prénom : \n")
        
        # Validation du téléphone (chiffres uniquement)
        while not str(self.__num_tel).isdigit():
            print("Le numéro de téléphone saisi est incorrect : écrivez en chiffres.")
            self.__num_tel = input("Saisissez le numéro de téléphone : \n")
        self.__num_tel = int(self.__num_tel)
        
        # Validation de l'adresse (pas seulement des chiffres)
        while str(self.__adresse).isdigit():
            print("L'adresse doit comporter au moins une lettre.")
            self.__adresse = input("Saisissez la bonne adresse : \n")

    def afficherClient(self):
        print("======== CLIENT ========")
        print(f"| Prénom : {self.__prenom} | NOM : {self.__nom} | ADRESSE : {self.__adresse} | Tél : {self.__num_tel} |")
        print("========================")