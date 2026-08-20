class Zone:
    def __init__(self, id_zone: int, designation: str, ville: str, departement: str):
        self.id_zone = id_zone
        self.designation = designation
        self.ville = ville
        self.departement = departement

    def __str__(self):
        return f"Zone {self.id_zone} : {self.designation} ({self.ville} - {self.departement})"

    def comparer_zone(self, autre_zone):
        if isinstance(autre_zone, Zone):
            return self.id_zone == autre_zone.id_zone
        return False


def controle_zone():
    while True:
        try:
            id_zone = int(input("Saisir l'ID de la zone (chiffre) : "))
            break
        except ValueError:
            print("Erreur : L'ID de la zone doit être un entier.")
    designation = input("Saisir la désignation de la zone : ").strip()
    ville = input("Saisir la ville : ").strip()
    departement = input("Saisir le département : ").strip()
    return Zone(id_zone, designation, ville, departement)