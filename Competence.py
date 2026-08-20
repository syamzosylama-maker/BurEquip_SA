class Competence:
    def __init__(self, id_technicien: int, type_materiel: str, niveau: str):
        self.id_technicien = id_technicien
        self.type_materiel = type_materiel  # Ex: Photocopieuse, Imprimante, etc.
        self.niveau = niveau  # "Expérimenté" ou "Novice"

    def __str__(self):
        return f"Compétence : Technicien ID {self.id_technicien} | Matériel: {self.type_materiel} | Niveau: {self.niveau}"

    def comparer_competence(self, autre_competence):
        if isinstance(autre_competence, Competence):
            return (self.id_technicien == autre_competence.id_technicien and 
                    self.type_materiel == autre_competence.type_materiel)
        return False


def controle_competence():
    while True:
        try:
            id_technicien = int(input("Saisir l'ID du technicien : "))
            break
        except ValueError:
            print("Erreur : L'ID doit être un nombre entier.")
    type_materiel = input("Saisir le type de matériel : ").strip()
    while True:
        niveau = input("Saisir le niveau (Expérimenté / Novice) : ").strip()
        if niveau.lower() in ["experimente", "expérimenté", "novice"]:
            niveau = "Expérimenté" if "ex" in niveau.lower() else "Novice"
            break
        print("Erreur : Veuillez saisir 'Expérimenté' ou 'Novice'.")
    return Competence(id_technicien, type_materiel, niveau)