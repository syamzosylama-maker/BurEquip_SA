from Zone import Zone
from Competence import Competence

class Technicien:
    def __init__(self, id_technicien: int, nom: str, zone: Zone):
        self.id_technicien = id_technicien
        self.nom = nom
        self.zone = zone      # Instance de Zone

    def __str__(self):
        return f"Technicien : Id {self.id_technicien}, {self.nom}, Zone {self.zone.designation}"

    def comparer_technicien(self, autre_technicien):
        if isinstance(autre_technicien, Technicien):
            return self.id_technicien == autre_technicien.id_technicien
        return False

    def changer_zone(self, nouvelle_zone: Zone):
        self.zone = nouvelle_zone

    def ajouter_competence(self, type_materiel: str, niveau: str, liste_competences: list):
        for comp in liste_competences:
            if comp.id_technicien == self.id_technicien and comp.type_materiel.lower() == type_materiel.lower():
                comp.niveau = niveau
                return
        liste_competences.append(Competence(self.id_technicien, type_materiel, niveau))

    def verifier_competence(self, type_materiel: str, liste_competences: list):
        for comp in liste_competences:
            if comp.id_technicien == self.id_technicien and comp.type_materiel.lower() == type_materiel.lower():
                return comp.niveau
        return None

    def afficher_avec_competences(self, liste_competences: list):
        print(f"\n--- Fiche Technicien : {self.nom} (ID: {self.id_technicien}) ---")
        print(f"Zone d'affectation : {self.zone.designation} ({self.zone.ville})")
        mes_competences = [c for c in liste_competences if c.id_technicien == self.id_technicien]
        if mes_competences:
            print("Spécialités :")
            for comp in mes_competences:
                print(f"  - {comp.type_materiel} : Niveau {comp.niveau}")
        else:
            print("  - Aucune spécialité déclarée (Novice par défaut sur tout ou en attente de formation).")


def controle_technicien():
    while True:
        try:
            id_technicien = int(input("Saisir l'ID du technicien (entier) : "))
            break
        except ValueError:
            print("Erreur : L'ID doit être un nombre entier.")
    nom = input("Saisir le nom du technicien : ").strip()
    return id_technicien, nom