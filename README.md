# Minitel-To-K8s
## Contexte
Le but de ce projet est de mettre en place une connection série entre un minitel et un ordinateur. Déployer un controleur d'interfaces pour ce Minitel et y intégrer des fonctionnalités de controles d'un projet de FaaS.
Le projet FaaS en lien : https://github.com/oloyiin/faas-portal

## Prérequis
* Un ordinateur possédant une prise Série, python3 (dont le paquet serial) et une connection internet
* Un minitel 1B ou 2 (avec une prise DIN)
* Le cluster FaaS déployé sur au moins une machine
* Le Backend de l'interface web déployé sur le cluster

## Installation
```
git clone https://github.com/EliossH/Minitel-To-K8s
cd Minitel-To-K8s
```

## Configuration
Mettre à jour le chemin d'installation du module, l'addresse de l'API et le port Série à utiliser dans le fichier config/settings.py
```
# config/settings.py

# Chemin d'exécution du projet (chemin absolu vers le répertoire du projet)
exec_path = "/chemin/vers/Minitel-To-K8s"

# Adresse de l'API backend
api_path = "http://<adresse-api>:<port>/"

# Port série utilisé pour la communication avec le Minitel
serial_port = "/dev/ttyUSB0"  # exemple pour adaptateur USB-RS232
```

## Préparation du Minitel
1. Allumer le minitel
2. Brancher l'adaptateur DIN-Sérial
3. Effectuer les commandes suivantes sur le Minitel
  * Fnct + T puis A : Mets le Minitel en mode Videotex
  * Fnct + T puis E : Désactive l'écho local
  * Fnct + P puis 1 : Défini la vitesse à 1200 bauds

## Exécution
Lancement du module (sous linux l'utilisation de sudo est nécéssaire pour l'accés au port Série)
```
sudo python3 main.py
```
