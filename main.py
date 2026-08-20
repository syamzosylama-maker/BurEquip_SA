def est_valide(technicien: Technicien, materiel: Materiel):
    """
    Règle de gestion : Un technicien n'intervient que dans sa zone d'affectation.
    Cette fonction vérifie si la zone du technicien est identique à celle du matériel.
    """
    return technicien.zone.comparer_zone(materiel.zone)


def menu():
    print("\n" + "="*50)
    print("             BUREQUIP SA - MENU DE NAVIGATION             ")
    print("="*50)
    print("1. Afficher la liste des Zones")
    print("2. Afficher la liste des Clients")
    print("3. Afficher la liste des Techniciens (avec compétences)")
    print("4. Afficher la liste des Matériels (Équipements)")
    print("5. Enregistrer une nouvelle Zone")
    print("6. Enregistrer un nouveau Client")
    print("7. Enregistrer un nouveau Technicien")
    print("8. Associer une compétence à un Technicien")
    print("9. Enregistrer un nouveau Matériel")
    print("10. Enregistrer une nouvelle Opération (Dépannage / Entretien)")
    print("11. Consulter l'Historique complet des interventions")
    print("12. Consulter l'Historique par Matériel")
    print("13. Consulter l'Historique par Technicien")
    print("0. Quitter l'application")
    print("="*50)
    return input("Saisissez votre choix : ").strip()


def main():
    # Initialisation des listes pour stocker les données du projet
    zones = []
    clients = []
    techniciens = []
    competences = []
    materiels = []
    operations = []

    # -------------------------------------------------------------------------
    # DONNÉES PRÉ-ENREGISTRÉES (Exigence du Projet : au moins 3 équipements, 2 clients, 3 techniciens)
    # -------------------------------------------------------------------------
    # 1. Enregistrement de 3 zones géographiques
    z1 = Zone(1, "Zone Nord-Dakar", "Guediawaye", "Dakar")
    z2 = Zone(2, "Zone Centre-Dakar", "Dakar Plateau", "Dakar")
    z3 = Zone(3, "Zone Saint-Louis", "Saint-Louis", "Saint-Louis")
    zones.extend([z1, z2, z3])

    # 2. Enregistrement de 2 clients (conforme à l'exigence)
    c1 = Client("DIONG", "Khadim", "774926515", "Guediawaye")
    c2 = Client("SARR", "Fatou", "771234567", "Dakar Plateau")
    # Pas d'appel de validation SaisieIncorrecte() au démarrage pour ne pas bloquer l'initialisation automatique offline
    clients.extend([c1, c2])

    # 3. Enregistrement de 3 techniciens (conforme à l'exigence)
    t1 = Technicien(101, "Amath", z1)      # Affecté à Guediawaye (Zone 1)
    t2 = Technicien(102, "Mariama", z2)    # Affectée à Dakar Plateau (Zone 2)
    t3 = Technicien(103, "Ousmane", z2)    # Affecté à Dakar Plateau (Zone 2)
    techniciens.extend([t1, t2, t3])

    # 4. Enregistrement de quelques compétences de départ
    t1.ajouter_competence("Photocopieuse", "Expérimenté", competences)
    t1.ajouter_competence("Téléphone", "Novice", competences)
    t2.ajouter_competence("Imprimante", "Expérimenté", competences)
    t3.ajouter_competence("Photocopieuse", "Novice", competences)

    # 5. Enregistrement de 3 matériels (équipements) (conforme à l'exigence)
    # Un matériel appartient à une zone selon l'adresse de son client
    m1 = Materiel("MAT001", "Canon", "iR2520", "Photocopieuse", c1, "Guediawaye", z1)
    m2 = Materiel("MAT002", "HP", "LaserJet", "Imprimante", c2, "Dakar Plateau", z2)
    m3 = Materiel("MAT003", "Samsung", "Galaxy", "Téléphone", c1, "Guediawaye", z1)
    materiels.extend([m1, m2, m3])

    # 6. Historique de départ (quelques opérations de démonstration)
    op1 = Operation("14/08/2026", "Dépannage", m1, t1) # Valide (Guediawaye / Zone 1)
    op2 = Operation("15/08/2026", "Entretien périodique", m2, t2) # Valide (Plateau / Zone 2)
    operations.extend([op1, op2])

    print("--- BUR EQUIP SA : Système de gestion initialisé avec succès ! ---")

    while True:
        choix = menu()
        
        if choix == "1":
            print("\n--- LISTE DES ZONES DÉLIMITÉES ---")
            for z in zones:
                print(z)
        
        elif choix == "2":
            print("\n--- LISTE DES CLIENTS ---")
            for c in clients:
                c.afficherClient()
        
        elif choix == "3":
            print("\n--- LISTE DES TECHNICIENS ET LEURS SPÉCIALITÉS ---")
            for t in techniciens:
                t.afficher_avec_competences(competences)
        
        elif choix == "4":
            print("\n--- LISTE DES ÉQUIPEMENTS (MATÉRIELS) ---")
            for m in materiels:
                print(m)
        
        elif choix == "5":
            print("\n--- ENREGISTRER UNE NOUVELLE ZONE ---")
            nouvelle_zone = controle_zone()
            # Éviter les doublons d'ID
            if any(z.id_zone == nouvelle_zone.id_zone for z in zones):
                print("Erreur : Une zone avec cet ID existe déjà.")
            else:
                zones.append(nouvelle_zone)
                print(f"Zone '{nouvelle_zone.designation}' enregistrée avec succès !")
        
        elif choix == "6":
            print("\n--- ENREGISTRER UN NOUVEAU CLIENT ---")
            nom = input("Saisir le nom du client : ").strip()
            prenom = input("Saisir le prénom du client : ").strip()
            tel = input("Saisir le numéro de téléphone : ").strip()
            adresse = input("Saisir l'adresse de l'installation : ").strip()
            nouveau_client = Client(nom, prenom, tel, adresse)
            nouveau_client.SaisieIncorrecte() # Corriger si mauvaise saisie
            clients.append(nouveau_client)
            print("Client enregistré avec succès !")
            nouveau_client.afficherClient()
        
        elif choix == "7":
            print("\n--- ENREGISTRER UN NOUVEAU TECHNICIEN ---")
            if not zones:
                print("Erreur : Vous devez d'abord créer au moins une Zone.")
                continue
            id_t, nom_t = controle_technicien()
            if any(t.id_technicien == id_t for t in techniciens):
                print("Erreur : Un technicien avec cet ID existe déjà.")
                continue
            
            print("Sélectionnez la zone d'affectation :")
            for idx, z in enumerate(zones):
                print(f"[{idx}] - {z}")
            while True:
                try:
                    choix_z = int(input("Choix du numéro de la zone : "))
                    if 0 <= choix_z < len(zones):
                        zone_choisie = zones[choix_z]
                        break
                    print("Index hors limites, réessayez.")
                except ValueError:
                    print("Entrée invalide.")
            
            nouveau_tech = Technicien(id_t, nom_t, zone_choisie)
            techniciens.append(nouveau_tech)
            print(f"Technicien {nom_t} enregistré et affecté à la zone '{zone_choisie.designation}' !")
        
        elif choix == "8":
            print("\n--- ASSOCIER OU METTRE À JOUR UNE COMPÉTENCE ---")
            if not techniciens:
                print("Erreur : Aucun technicien enregistré.")
                continue
            print("Sélectionnez le technicien :")
            for idx, t in enumerate(techniciens):
                print(f"[{idx}] - {t.nom} (ID: {t.id_technicien})")
            while True:
                try:
                    choix_t = int(input("Choix : "))
                    if 0 <= choix_t < len(techniciens):
                        tech = techniciens[choix_t]
                        break
                    print("Index incorrect.")
                except ValueError:
                    print("Entrée invalide.")
            
            type_mat = input("Saisir la catégorie de matériel concernée (ex: Photocopieuse, Imprimante) : ").strip()
            while True:
                niv = input("Saisir le niveau (Expérimenté / Novice) : ").strip()
                if niv.lower() in ["experimente", "expérimenté", "novice"]:
                    niv = "Expérimenté" if "ex" in niv.lower() else "Novice"
                    break
                print("Niveau invalide.")
            
            tech.ajouter_competence(type_mat, niv, competences)
            print(f"Compétence mise à jour pour {tech.nom} !")
        
        elif choix == "9":
            print("\n--- ENREGISTRER UN NOUVEAU MATÉRIEL ---")
            if not clients or not zones:
                print("Erreur : Vous devez disposer de Clients et de Zones enregistrées.")
                continue
            id_mat = input("Saisir l'identifiant unique du matériel (ex: MAT999) : ").strip()
            if any(m.id_materiel == id_mat for m in materiels):
                print("Erreur : Un matériel avec cet ID existe déjà.")
                continue
            marque = input("Marque : ").strip()
            modele = input("Modèle : ").strip()
            cat = input("Catégorie de matériel (ex: Photocopieuse, Imprimante, Téléphone, Télécopieur) : ").strip()
            adresse_install = input("Adresse d'installation : ").strip()
            
            print("Sélectionnez le client propriétaire :")
            for idx, c in enumerate(clients):
                print(f"[{idx}] - {c.get_prenom()} {c.get_nom()}")
            while True:
                try:
                    choix_c = int(input("Choix : "))
                    if 0 <= choix_c < len(clients):
                        client_choisi = clients[choix_c]
                        break
                    print("Index incorrect.")
                except ValueError:
                    print("Entrée invalide.")
            
            print("Sélectionnez la Zone géographique d'installation :")
            for idx, z in enumerate(zones):
                print(f"[{idx}] - {z}")
            while True:
                try:
                    choix_z = int(input("Choix : "))
                    if 0 <= choix_z < len(zones):
                        zone_choisie = zones[choix_z]
                        break
                    print("Index incorrect.")
                except ValueError:
                    print("Entrée invalide.")
            
            nouveau_mat = Materiel(id_mat, marque, modele, cat, client_choisi, adresse_install, zone_choisie)
            materiels.append(nouveau_mat)
            print(f"Équipement {id_mat} enregistré avec succès !")
        
        elif choix == "10":
            print("\n--- ENREGISTRER UNE OPÉRATION D'ENTRETIEN OU DÉPANNAGE ---")
            if not techniciens or not materiels:
                print("Erreur : Veuillez enregistrer des matériels et des techniciens au préalable.")
                continue
            
            print("Sélectionnez le matériel à dépanner/entretenir :")
            for idx, m in enumerate(materiels):
                print(f"[{idx}] - ID: {m.id_materiel} | {m.marque} {m.modele} | Zone: {m.zone.designation}")
            while True:
                try:
                    choix_m = int(input("Choix matériel : "))
                    if 0 <= choix_m < len(materiels):
                        mat = materiels[choix_m]
                        break
                    print("Index incorrect.")
                except ValueError:
                    print("Entrée invalide.")
            
            print("Sélectionnez le technicien intervenant :")
            for idx, t in enumerate(techniciens):
                print(f"[{idx}] - ID: {t.id_technicien} | Nom: {t.nom} | Zone d'affectation : {t.zone.designation}")
            while True:
                try:
                    choix_t = int(input("Choix technicien : "))
                    if 0 <= choix_t < len(techniciens):
                        tech = techniciens[choix_t]
                        break
                    print("Index incorrect.")
                except ValueError:
                    print("Entrée invalide.")
            
            # --- RÈGLE DE GESTION 1 : COMPATIBILITÉ DES ZONES ---
            if not est_valide(tech, mat):
                print("\n⚠️ AVERTISSEMENT / RÈGLE DE GESTION :")
                print(f"Le technicien {tech.nom} est affecté à la zone '{tech.zone.designation}'")
                print(f"mais le matériel est situé en zone '{mat.zone.designation}'.")
                print("BurEquip impose qu'un technicien n'intervienne que dans sa propre zone d'affectation !")
                poursuivre = input("Souhaitez-vous quand même forcer l'opération (o/n) ? ").strip().lower()
                if poursuivre != "o":
                    print("Opération annulée.")
                    continue
            
            # --- RÈGLE DE GESTION 2 : VÉRIFICATION COMPÉTENCE (Facultatif mais utile pour l'image de BurEquip) ---
            niveau_competence = tech.verifier_competence(mat.categorie, competences)
            if niveau_competence is None:
                print(f"⚠️ Note : {tech.nom} n'a aucune compétence enregistrée pour '{mat.categorie}'. Il interviendra comme novice absolu.")
            else:
                print(f"💡 Info : {tech.nom} a un niveau '{niveau_competence}' sur ce type d'appareil.")
            
            date = input("Saisir la date de l'opération (jj/mm/aaaa) : ").strip()
            while True:
                type_op = input("Type d'opération (Dépannage / Entretien périodique) : ").strip()
                if type_op.lower() in ["depannage", "dépannage", "entretien", "entretien periodique", "entretien périodique"]:
                    type_op = "Dépannage" if "dep" in type_op.lower() else "Entretien périodique"
                    break
                print("Erreur : Veuillez choisir parmi 'Dépannage' ou 'Entretien périodique'.")
            
            # --- RÈGLE DE GESTION 3 : DURÉE & RESSOURCES ---
            print("\nBurEquip impose qu'une opération ne puisse pas dépasser 1 jour ou faire intervenir plus d'un technicien.")
            duree = input("L'intervention a-t-elle duré plus d'une journée ou requis d'autres techniciens ? (o/n) : ").strip().lower()
            if duree == "o":
                nb_jours = int(input("Saisissez le nombre estimé de jours/techniciens (par ex. 2 ou 3) : "))
                print(f"Conformément aux règles BurEquip, nous allons enregistrer {nb_jours} opérations distinctes de 1 jour.")
                for day in range(1, nb_jours + 1):
                    nouvelle_op = Operation(f"{date} (Partie {day})", type_op, mat, tech)
                    operations.append(nouvelle_op)
                print(f"Les {nb_jours} sous-opérations ont été ajoutées à l'historique !")
            else:
                nouvelle_op = Operation(date, type_op, mat, tech)
                operations.append(nouvelle_op)
                print("Opération d'intervention enregistrée avec succès !")
        
        elif choix == "11":
            afficher_historique(operations)
        
        elif choix == "12":
            print("\n--- HISTORIQUE DES INTERVENTIONS PAR MATÉRIEL ---")
            if not materiels:
                print("Aucun matériel enregistré.")
                continue
            for idx, m in enumerate(materiels):
                print(f"[{idx}] - {m.id_materiel} ({m.marque} {m.modele})")
            while True:
                try:
                    choix_m = int(input("Choix : "))
                    if 0 <= choix_m < len(materiels):
                        mat_sel = materiels[choix_m]
                        break
                    print("Index incorrect.")
                except ValueError:
                    print("Entrée invalide.")
            
            ops_mat = operations_par_materiel(operations, mat_sel)
            print(f"\n--- Historique pour le matériel {mat_sel.id_materiel} ---")
            afficher_historique(ops_mat)
        
        elif choix == "13":
            print("\n--- HISTORIQUE DES INTERVENTIONS PAR TECHNICIEN ---")
            if not techniciens:
                print("Aucun matériel enregistré.")
                continue
            for idx, t in enumerate(techniciens):
                print(f"[{idx}] - {t.nom} (ID: {t.id_technicien})")
            while True:
                try:
                    choix_t = int(input("Choix : "))
                    if 0 <= choix_t < len(techniciens):
                        tech_sel = techniciens[choix_t]
                        break
                    print("Index incorrect.")
                except ValueError:
                    print("Entrée invalide.")
            
            ops_tech = operations_par_technicien(operations, tech_sel)
            print(f"\n--- Historique pour le technicien {tech_sel.nom} ---")
            afficher_historique(ops_tech)
        
        elif choix == "0":
            print("\nMerci d'avoir utilisé le portail de gestion de BurEquip SA. Au revoir !")
            break
        
        else:
            print("Choix invalide, veuillez sélectionner une option entre 0 et 13.")


if __name__ == "__main__":
    main()