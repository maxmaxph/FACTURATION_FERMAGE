# Fermage Facturation

## Description

**Fermage Facturation** est une application Python conçue pour automatiser la génération de factures liées au fermage agricole. Ce programme vise à simplifier le processus de facturation en combinant des données Excel et des fonctionnalités avancées pour produire des fichiers PDF personnalisés pour chaque propriétaire et fermier.

## Fonctionnalités principales
- Génération de factures PDF avec des informations détaillées sur les parcelles, surfaces, prix ajustés, et taxes.
- Aperçu en temps réel avant la génération de la facture pour validation.
- Gestion des données issues d'un fichier Excel.
- Interface utilisateur intuitive développée avec **Tkinter**.
- Ouvrir facilement les dossiers contenant les factures et le fichier Excel directement depuis l'application.
- Support des polices personnalisées pour des PDF esthétiques.
- Multi-plateforme : compatible avec Windows, macOS et Linux.

## Technologies utilisées
- **Python 3.13** : Langage principal pour le développement.
- **Tkinter** : Interface graphique pour l'utilisateur.
- **Pillow** : Gestion des images, notamment pour le logo.
- **OpenPyXL** : Manipulation des fichiers Excel.
- **FPDF** : Création et personnalisation des fichiers PDF.
- **Subprocess** : Ouvrir les dossiers dans l'explorateur natif du système d'exploitation.

## Structure du projet

```plaintext
Fermage Facturation/
├── assets/
│   ├── fonts/                 # Polices personnalisées (DejaVuSans, etc.)
│   ├── img/                   # Images (logo, icônes)
├── tableau/
│   └── tableau_fermage.xlsx   # Fichier Excel contenant les données de fermage
├── factures/                  # Dossier de sortie pour les fichiers PDF générés
├── generateur_facture_V4.py   # Code source principal
├── README.md                  # Documentation
```

## Prérequis

- Python 3.13 ou supérieur
- Modules Python nécessaires :
  - `Pillow`
  - `FPDF`
  - `OpenPyXL`

Installez les dépendances avec la commande suivante :
```bash
pip install Pillow fpdf openpyxl
```

## Utilisation

1. Lancez le script Python :
   ```bash
   python generateur_facture_V4.py
   ```

2. Sélectionnez l'année, le propriétaire, et le fermier dans les menus déroulants.
3. Sélectionnez les parcelles associées.
4. Cliquez sur **Générer la Facture** pour afficher un aperçu et confirmer.
5. Les fichiers PDF seront enregistrés dans le dossier `factures/`.

## Transformation en exécutable

Pour distribuer l'application sans nécessiter Python, vous pouvez la convertir en fichier exécutable avec **PyInstaller** :

```bash
pyinstaller --onefile --noconsole --icon=assets/img/facturation_fermage.ico generateur_facture_V4.py
```

L'exécutable sera généré dans le dossier `dist/`.

## Maintenance et améliorations

### prévisions d'améliorations :
- Ajouter la prise en charge de plusieurs langues.
- Intégrer une base de données pour remplacer le fichier Excel.
- Ajouter des options d'exportation vers d'autres formats (CSV, JSON).
- Améliorer le style graphique de l'interface utilisateur avec des bibliothèques comme `Tkinter.ttk` ou `PyQt`.

### Résolution des problèmes courants :
- **Erreur : Module non trouvé** : Assurez-vous que les modules nécessaires sont installés.
- **Chemin d'accès non trouvé** : Vérifiez que les chemins des fichiers dans le script correspondent à votre structure.

## Licence

Ce projet est sous licence **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Vous êtes libre de :

- Partager — copier, distribuer et communiquer le matériel par tous moyens et sous tous formats.
- Adapter — remixer, transformer et créer à partir du matériel pour toute utilisation, y compris commerciale.

À condition de créditer l'auteur :

```
Développé par Maxime LENFANT - https://maxime-lenfant.fr - maxmaxph@gmail.com
```

## Contact

- **Auteur** : Maxime LENFANT
- **Site web** : [maxime-lenfant.fr](https://maxime-lenfant.fr)
- **Email** : [maxmaxph@gmail.com](mailto:maxmaxph@gmail.com)
