from Materiel import Materiel
from Technicien import Technicien

class Operation:
    def __init__(self, date: str, type_operation: str, materiel: Materiel, technicien: Technicien):
        self.date = date  # jj/mm/aaaa
        self.type_operation = type_operation  # "Dépannage" ou "Entretien périodique"
        self.materiel = materiel              # Instance de Materiel
        self.technicien = technicien          # Instance de Technicien

    def afficher_operation(self):
        mat_id = self.materiel.id_materiel if isinstance(self.materiel, Materiel) else str(self.materiel)
        tech_nom = self.technicien.nom if isinstance(self.technicien, Technicien) else str(self.technicien)
        print(f"[{self.date}] | Type : {self.type_operation:<20} | Matériel ID : {mat_id:<10} | Technicien : {tech_nom}")


def operations_par_materiel(liste_operations, materiel: Materiel):
    return [op for op in liste_operations if op.materiel.id_materiel == materiel.id_materiel]


def operations_par_technicien(liste_operations, technicien: Technicien):
    return [op for op in liste_operations if op.technicien.id_technicien == technicien.id_technicien]


def afficher_historique(liste_operations):
    if not liste_operations:
        print("Aucune opération enregistrée dans l'historique.")
        return
    print("\n======================= HISTORIQUE DES INTERVENTIONS =======================")
    for op in liste_operations:
        op.afficher_operation()
    print("============================================================================")

