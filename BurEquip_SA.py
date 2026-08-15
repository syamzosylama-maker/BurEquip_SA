class Zone:
    def __init__(self, id_zone:int , designation:str, ville:str, departement:str ):
        self.id_zone = id_zone
        self.designation = designation
        self.ville = ville
        self.departement = departement

#Fonction d'affichage de la zone
    def __str__(self):
        return f"La zone est : Id {self.id_zone} designation {self.designation}, ({self.ville}-{self.departement})"
    
#Comparer deux zones distincts
    def comparer_zone(self,autre_zone):
        if isinstance(autre_zone, Zone):
            return self.id_zone == autre_zone.id_zone
        return False


class Materiel:
    def __init__(self, id_materiel, marque, modele, categorie, client, adresse, zone):
        self.id_materiel = id_materiel
        self.marque = marque
        self.modele = modele
        self.categorie = categorie
        self.client = client
        self.adresse = adresse
        self.zone = zone
#Fonction d'affichage du materiels
    def __str__(self):
        return f"Materiel : Id {self.id_materiel}, {self.marque}, {self.modele}, {self.categorie}, {self.client}, {self.adresse}, {self.zone}"     



def main():
    #implementation de dependances de Zone
    
    zone = []
    def est_valide(Technicien,Materiel): #Verification de la validite de la zone du materiel confier a un technicien
        return techniciens.zone == materiels.zone


    #implementation des dependances de Client
    clients = []
    #implementation des dependances de Competence
    competences = []
    #implementation des dependances de Technicien
    techniciens = []
    #implementation des dependances de Materiel
    materiels = []
    #implementation des dependances de operations
    operations = []





    while True:
        print("\n==============================================")
        print("        SYSTÈME DE GESTION BURAQUIP SA       ")
        print("==============================================")
        print("1. Ajouter une Zone (id, designation, ville, departement)")
        print("2. EAjouter un Client (nom, adresse)")
        print("3. Ajouter un Technicien (nom, zone)")
        print("4. Ajouter un Matériel (id_materiel, marque, modele, categorie, adresse, client, zone)")
        print("5. Ajouter une Competence (categorie, niveau)")
        print("6. ENregistrer une Operation (date, type, materiel, tech)")
        print("7. Afficher le recapitulatif")
        print("0. Quitter l'application")
        print("==============================================")

        try:
            choix = int(input("Faites votre choix : "))
        except ValueError:
            print("Choix invalide ! Veuillez saisir un nombre")
            continue
            
        
        match choix:
            case 1:
                try:
                    id_zone=int(input("Saisir l'id de la zone"))
                    break
                except ValueError:
                    print(" Erreur l'id doit etre un entier")
                designation = input("Saisir la designation de la zone ")
                ville = input("Saisir la ville de la zone ")
                departement = input("Saisir le departement de la zone ")
                zone.append(Zone(id_zone, designation, ville, departement))
                return zone
                print(f" Zone ajoutee avec succees !")


            case 2:
                #implementer la gestion de la classe Client

            case 3:
                #implementer la gestion de la classe Technicien

            case 4:
                #implementer la gestion de la classe Materiel

            case 5:
                #implementation de la classe Competence 

            case 6:
                for i,m in enumerate(materiels,0): #Selection du Materiel
                    print(f"  [{i}] {m}")
                id_m = int(input("Selectionner le numero du materiel : "))
                mat_choisi = materiels[id_m]

                
                for i,t in enumerate(techniciens,0): #Selection du technicien
                    print(f"  [{i}] {m}")
                id_t = int(input("Selectionner le numero du technicien : "))
                tech_choisi = techniciens[id_t]

                if not est_valide(tech_choisi, mat_choisi):
                    print("Operation impossible : Zones incompatobles !")
                else:
                    op=Operation(date_op, type_op, mat_choisi, tech_choisi)
                    operations.apend(op)
                    print("Succes !")
                #implementer la gestion des operations
                
            case 7:
                print("\nFermeture de l'application BurEquip SA.")
                print("A Bientot !!!")
                break
            case _:
                print("Operation inexistante.")

if __name__ == "__main__":
    main()




