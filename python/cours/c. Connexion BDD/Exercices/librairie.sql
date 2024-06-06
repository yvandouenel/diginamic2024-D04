CREATE DATABASE IF NOT EXISTS Librairie;
USE Librairie;

CREATE TABLE Auteur (
    id_auteur INT PRIMARY KEY,
    nom_auteur VARCHAR(255),
    prenom_auteur VARCHAR(255)
);

CREATE TABLE Livre (
    id_livre INT PRIMARY KEY,
    id_auteur_livre INT,
    titre_livre VARCHAR(255),
    ISBN_livre VARCHAR(13),
    date_parution_livre DATE,
    prix_livre DECIMAL(10, 2),
    disponibilite_livre DATE,
    langue_livre VARCHAR(50),
    image_url_livre VARCHAR(255),
    FOREIGN KEY (id_auteur_livre) REFERENCES Auteur(id_auteur)
);

CREATE TABLE Client (
    id_client INT PRIMARY KEY,
    nom_client VARCHAR(255),
    prenom_client VARCHAR(255),
    email_client VARCHAR(255),
    mot_de_passe_client VARCHAR(255)
);

CREATE TABLE Panier (
    id_panier INT PRIMARY KEY,
    id_client_panier INT,
    date_creation_panier DATETIME,
    status_panier ENUM('en_cours', 'valide', 'annule'),
    FOREIGN KEY (id_client_panier) REFERENCES Client(id_client)
);

CREATE TABLE Panier_Livre (
    id_panier_pl INT,
    id_livre_pl INT,
    quantite_pl INT,
    PRIMARY KEY (id_panier_pl, id_livre_pl),
    FOREIGN KEY (id_panier_pl) REFERENCES Panier(id_panier),
    FOREIGN KEY (id_livre_pl) REFERENCES Livre(id_livre)
);

CREATE TABLE Commande (
    id_commande INT PRIMARY KEY,
    id_client_commande INT,
    date_commande DATETIME,
    montant_total_commande DECIMAL(10, 2),
    status_commande ENUM('en_attente', 'traitee', 'annulee'),
    FOREIGN KEY (id_client_commande) REFERENCES Client(id_client)
);

CREATE TABLE Commande_Livre (
    id_commande_cl INT,
    id_livre_cl INT,
    quantite_cl INT,
    PRIMARY KEY (id_commande_cl, id_livre_cl),
    FOREIGN KEY (id_commande_cl) REFERENCES Commande(id_commande),
    FOREIGN KEY (id_livre_cl) REFERENCES Livre(id_livre)
);

CREATE TABLE Commentaire (
    id_commentaire INT PRIMARY KEY,
    id_client_commentaire INT,
    id_livre_commentaire INT,
    contenu_commentaire TEXT,
    date_commentaire DATETIME,
    FOREIGN KEY (id_client_commentaire) REFERENCES Client(id_client),
    FOREIGN KEY (id_livre_commentaire) REFERENCES Livre(id_livre)
);
