#! /usr/bin/python3.6
# -*-coding:utf-8 -*
#IMPORTATION DE MES MODULES
# import socket

# def client():
#     # Contruction de notre socket
#     connexionAvecServeur = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # ip + tcp
#     # Connecter le client
#     connexionAvecServeur.connect(('localhost', 12800))
#     #Reception du message
#     msg = connexionAvecServeur.recv(1024)
#     msg = msg.decode()
#     print("Message reçu : << {} >>".format(msg))
#     connexionAvecServeur.close()


import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion_avec_serveur.close()

# if __name__ == "__main__":
#     client()
