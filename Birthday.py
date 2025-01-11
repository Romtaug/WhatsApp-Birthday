# Instructions pour configurer l'envoi automatique de messages sur WhatsApp

# 1. Connexion préalable à WhatsApp Web
#    Assurez-vous d'être connecté à WhatsApp Web via votre navigateur avant d'exécuter ce script.
#    Cela garantit que le message sera envoyé correctement.

# 2. Ajout d'une exception pour le fichier .bat dans l'antivirus
#    Si votre antivirus bloque le fichier .bat :
#    - Accédez aux paramètres de votre antivirus.
#    - Ajoutez une exception ou une exclusion pour le fichier .bat dans les paramètres de sécurité.
#      Exemple pour AVG :
#      - Allez dans "Menu" > "Paramètres" > "Exceptions".
#      - Ajoutez le chemin du fichier .bat.

# 3. Configuration du planificateur de tâches (Windows Task Scheduler)
#    - Ouvrez le planificateur de tâches sur Windows.
#    - Créez une nouvelle tâche.
#    - Configurez-la pour qu'elle s'exécute uniquement si vous êtes connecté à la session.
#    - Activez l'option "Exécuter la tâche dès que possible si une exécution planifiée est manquée".
#    - Assurez-vous de définir correctement l'heure et la fréquence d'exécution.
#######################################################################################################

import pywhatkit
import datetime
import time
import socket

# Fonction pour vérifier la connexion Internet
def check_internet():
    try:
        # Tente de se connecter à Google pour vérifier la connexion Internet
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

# Attendre jusqu'à ce que le Wi-Fi soit connecté
def wait_for_internet():
    print("Vérification de la connexion Internet...")
    while not check_internet():
        print("Pas de connexion Internet. Nouvelle tentative dans 5 secondes...")
        time.sleep(5)
    print("Connexion Internet établie.")

# Liste des contacts et leurs dates d'anniversaire
contacts = [  # Format MM-DD
    {"nom": "Afzal", "numéro": "+33778404427", "date_anniversaire": "02-19"},
    {"nom": "Alexis", "numéro": "+33750417617", "date_anniversaire": "06-10"},
]

# Obtenir la date d'aujourd'hui au format MM-DD
today = datetime.datetime.now().strftime("%m-%d")
print(f"Date d'aujourd'hui : {today}")

# Vérifier la connexion Internet
wait_for_internet()

# Parcourir tous les contacts pour vérifier les anniversaires
for contact in contacts:
    print(f"Vérification du contact : {contact['nom']}")
    if contact['date_anniversaire'] == today:
        print(f"C'est l'anniversaire de {contact['nom']} aujourd'hui!")

        # Planifier l'envoi du message dans la minute suivante
        heure = datetime.datetime.now().hour
        minute = (datetime.datetime.now().minute + 1) % 60
        if minute == 0:
            heure = (heure + 1) % 24

        print(f"Ne fermez pas le programme ! Heure planifiée pour l'envoi : {heure:02}:{minute:02}")

        # Envoyer le message via WhatsApp
        try:
            pywhatkit.sendwhatmsg(contact['numéro'], f"Happy Birthday {contact['nom']} !! 🎉🥳🎊🎇", heure, minute)
            print(f"Ne fermez pas le programme ! Message programmé pour {contact['nom']} à {heure:02}:{minute:02}.")
        except Exception as e:
            print(f"Erreur lors de l'envoi du message à {contact['nom']}: {e}")
    else:
        print(f"Pas d'anniversaire aujourd'hui pour {contact['nom']}.")

print("Vérification des anniversaires terminée.")
