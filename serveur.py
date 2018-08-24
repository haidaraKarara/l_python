#! /usr/bin/python3.6
# -*-coding:utf-8 -*
#IMPORTATION DE MES MODULES
# import socket

# def serveur():
#     # Construction de notre socket
#     connexionPrincipale = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # ip + tcp
#     # Connecter le socket
#     connexionPrincipale.bind(('',12800))
#     # Faire écouter notre socket
#         # On va avant tout lui préciser le nombre maximum de connexions 
#         # qu'il peut recevoir sur ce port sans les accepter
#     connexionPrincipale.listen(5)
#     # Accepter une connexion venant du client
#         #Il est important de noter que la méthode accept renvoie deux informations :
#             #le socket connecté qui vient de se créer, celui qui va nous permettre de dialoguer avec notre client tout juste connecté ;
#             #un tuple représentant l'adresse IP et le port de connexion du client.
#     connexionAvecUnClient, infoConnextion = connexionPrincipale.accept()
#     #print("Un client vient de se connecter")
#     #print("Adresse IP : {}".format(infoConnextion[0]))
#     connexionAvecUnClient.send(b"Je viens d'accepter la connexion !")
#     connexionAvecUnClient.close()

import socket
import select

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

serveur_lance = True
clients_connectes = []
while serveur_lance:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la connexion_principale en lecture
    # On attend maximum 50ms
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
        [], [], 0.05)
    
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        clients_connectes.append(connexion_avec_client)
    
    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            # Client est de type socket
            msg_recu = client.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            print("Reçu {}".format(msg_recu))
            client.send(b"5 / 5")
            if msg_recu == "fin":
                serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()

# if __name__ == "__main__":
#     serveur()
