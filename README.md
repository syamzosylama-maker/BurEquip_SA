# BurEquip SA - Système de Gestion du Service Après-Vente (SAV)

## 📌 Présentation du Projet
**BurEquip SA** est une entreprise spécialisée dans la distribution de matériels de bureau de toute nature (bureaux, armoires, sièges) ainsi que de matériels technologiques sophistiqués tels que des photocopieuses, des imprimantes d'ordinateurs, des télécopieurs et des téléphones cellulaires [8].

Afin de garantir un service après-vente (SAV) d'excellence, de fidéliser sa clientèle et d'assurer une gestion financière optimale de ses contrats de maintenance, BurEquip SA s'est dotée d'une application informatique modulaire développée en **Programmation Orientée Objet (POO)** [8, 12]. Ce système permet de suivre les équipements vendus, de gérer les compétences de la vingtaine de techniciens et de planifier efficacement les interventions de dépannage et d'entretien périodique [8, 9, 11].

---

## 🛠️ Architecture Modulaire (Conception POO)

L'application est découpée en plusieurs modules indépendants et réutilisables, conformément aux spécifications techniques [13, 14]:

1. **`Zone.py`** : Modélise les secteurs d'activité de l'entreprise. Une zone est caractérisée par un ID, une désignation, une ville et un département [10]. Elle contient une méthode pour comparer deux zones et une fonction de contrôle de saisie [13, 19].
2. **`Competence.py`** : Définit le niveau d'expertise d'un technicien (soit *Expérimenté*, soit *Novice*) sur un type de matériel précis [2, 9].
3. **`Client.py`** : Gère les informations des entreprises clientes (nom, prénom, numéro de téléphone, adresse d'installation) et intègre un système robuste de validation des saisies pour corriger les erreurs utilisateur en temps réel [1].
4. **`Materiel.py`** : Représente chaque équipement identifié de manière unique, intégrant sa marque, son modèle, sa catégorie, le client propriétaire, son adresse physique d'installation et sa zone d'affectation [10, 11].
5. **`Technicien.py`** : Représente les collaborateurs techniques de BurEquip. Chaque technicien est rattaché à une zone géographique unique d'intervention et possède un portefeuille de compétences dynamiques [10, 15, 16].
6. **`Operation.py`** : Enregistre l'historique complet des interventions (date, type d'opération : *Dépannage* ou *Entretien périodique*, matériel concerné et technicien assigné) [11, 14]. Il propose des filtres de recherche par matériel ou par technicien [14].
7. **`main.py` / `burequip_app.py`** : Point d'entrée de l'application qui charge le jeu de données initial, implémente les contrôles métier globaux et affiche un menu de navigation interactif en console [12, 13, 20].

---

## ⚙️ Règles de Gestion Implémentées

Le système applique de manière stricte les règles métier de BurEquip SA :

* **Règle de Zone (Géolocalisation)** : Pour limiter les frais de déplacement et privilégier un contact de proximité, **un technicien ne peut intervenir que sur un matériel installé dans sa zone d'affectation** [10, 11]. Le système vérifie cette compatibilité lors de chaque planification d'intervention et alerte l'utilisateur en cas d'incohérence [11, 20].
* **Règle de Durée & Ressources Humaines (Découpage des Opérations)** : Une opération unitaire ne peut pas dépasser **1 jour** ni faire intervenir **plus d'un technicien** [11]. Si une intervention dépasse ces limites (ex: 3 jours d'effort cumulés), l'application la divise automatiquement en plusieurs opérations distinctes d'une journée dans l'historique afin de faciliter la future facturation [11].
* **Exigence d'Initialisation (Jeu d'essai)** : Au démarrage, l'application pré-charge de manière transparente [12] :
  - **3 zones géographiques** [10].
  - **2 clients enregistrés** [12].
  - **3 techniciens** avec leurs compétences initiales [12].
  - **3 matériels** déjà installés chez les clients [12].

---

## 🚀 Comment Lancer l'Application ?

### Prérequis
* **Python 3.8+** installé sur votre machine.

### Installation et Exécution
1. Téléchargez le fichier de l'application : **`burequip_app.py`** (qui regroupe l'ensemble des modules en un seul fichier exécutable pour plus de simplicité).
2. Ouvrez un terminal dans le dossier contenant le fichier.
3. Exécutez la commande suivante :
   ```bash
   python burequip_app.py
   ```

---

## 🕹️ Guide d'Utilisation du Menu

L'interface en ligne de commande vous propose un menu interactif structuré [12, 13]:

* **Consultation (Options 1 à 4)** : Affichez à tout moment la liste des zones, des clients, des techniciens (avec le détail de leurs spécialités et niveaux) et des matériels en service [1, 4, 15, 19].
* **Création (Options 5, 6, 7, 9)** : Ajoutez de nouvelles entités. Les systèmes de contrôle de saisie vous guideront pour éviter toute erreur de format (ex: numéros de téléphone invalides, noms contenant des chiffres) [1, 3, 18].
* **Gestion des Compétences (Option 8)** : Associez ou mettez à jour l'expertise d'un technicien sur une catégorie d'appareil (*Photocopieuse*, *Imprimante*, *Téléphone*, etc.) [2, 16].
* **Planification d'Opérations (Option 10)** : Enregistrez un dépannage ou un entretien périodique [11]. Le système calculera automatiquement si l'opération doit être découpée et validera la correspondance des zones entre le technicien et le matériel [11, 20].
* **Historiques (Options 11 à 13)** : Consultez l'historique complet de l'entreprise, ou filtrez les interventions par matériel spécifique ou par technicien [14].