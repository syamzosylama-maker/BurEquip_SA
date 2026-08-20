from Client import Client
from Zone import Zone

class Materiel:
    def __init__(self, id_materiel: str, marque: str, modele: str, categorie: str, client: Client, adresse: str, zone: Zone):
        self.id_materiel = id_materiel
        self.marque = marque
        self.modele = modele
        self.categorie = categorie
        self.client = client  # Instance de Client
        self.adresse = adresse
        self.zone = zone      # Instance de Zone

    def __str__(self):
        nom_client = self.client.get_nom() if isinstance(self.client, Client) else str(self.client)
        nom_zone = self.zone.designation if isinstance(self.zone, Zone) else str(self.zone)
        return (f"Matériel ID: {self.id_materiel} | {self.marque} {self.modele} ({self.categorie}) | "
                f"Client: {nom_client} | Adresse: {self.adresse} | {nom_zone}")