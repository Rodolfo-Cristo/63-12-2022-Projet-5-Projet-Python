import customtkinter
import os
import user_and_group_listing
import manager

# Création de la Frame droite concernant les utilisateurs
class UsersPage(customtkinter.CTkFrame):
    
    # Constructeur
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        # appel de la fonction user_display se trouvant dans le module user_and_group_listing
        # passage des listes XXXXX_1 du module user_and_group_listing en arguments dans la fonction
        # pour lors de l'appel de la méthode ci-dessous, on est quelque chose à afficher par défaut quand on ouvre la page des utilisateurs  
        user_and_group_listing.user_display(user_and_group_listing.users_1, user_and_group_listing.users_admin_1, user_and_group_listing.users_account_1)

        # Appel de la méthode ayant pour but de générer graphiquement les utilisateurs
        self.generate_users()

        # Création du conteneur qui contiendra les boutons des Onglets + configuration de sa disposition
        self.tab_frame = customtkinter.CTkFrame(master=self)
        self.tab_frame.grid(row=2, column=0, sticky="w", padx=20, pady=20)


        # Création des boutons qui déclencheront l'actualisation de l'interface graphique grâce au passage des arguments dans la fonction user_display
        # Selon les arguments passés, on affiche une de nos sous liste provenant du module user_and_group_listing
        # + configuration de leur position
        tab_button_1 = customtkinter.CTkButton(master=self.tab_frame,
                                            text="Onglet 1",
                                            command= lambda : [user_and_group_listing.user_display(user_and_group_listing.users_1, user_and_group_listing.users_admin_1, user_and_group_listing.users_account_1), self.refresh_users()])
        tab_button_1.grid(row=0, column=0, pady=10, padx=10)

        tab_button_2 = customtkinter.CTkButton(master=self.tab_frame,
                                             text="Onglet 2",
                                             command= lambda : [user_and_group_listing.user_display(user_and_group_listing.users_2, user_and_group_listing.users_admin_2, user_and_group_listing.users_account_2), self.refresh_users()])
        tab_button_2.grid(row=0, column=1, pady=10, padx=10)

        tab_button_3 = customtkinter.CTkButton(master=self.tab_frame,
                                             text="Onglet 3",
                                             command= lambda : [user_and_group_listing.user_display(user_and_group_listing.users_3, user_and_group_listing.users_admin_3, user_and_group_listing.users_account_3), self.refresh_users()])
        tab_button_3.grid(row=0, column=2, pady=10, padx=10)

        tab_button_4 = customtkinter.CTkButton(master=self.tab_frame,
                                             text="Onglet 4",
                                             command= lambda : [user_and_group_listing.user_display(user_and_group_listing.users_4, user_and_group_listing.users_admin_4, user_and_group_listing.users_account_4), self.refresh_users()])
        tab_button_4.grid(row=0, column=3, pady=10, padx=10)


        # Bouton déclenchant la méthode list_all qui affiche tous les utilisateurs dans 1 fenêtre + configuration de sa position
        self.refresh_button = customtkinter.CTkButton(master=self.tab_frame,
                                                text="Afficher la liste complète",
                                                command=self.list_all) 
        self.refresh_button.grid(row=0, column=4, pady=10, padx=20)



        # Création du conteneur qui contiendra les boutons concernant les modifications des utilisateurs + configuration de sa position
        self.bottom_frame = customtkinter.CTkFrame(master=self)
        self.bottom_frame.grid(row=3, column=0, sticky="w", padx=20, pady=20)
        
        
        # Bouton déclenchant la méthode add_user_window + configuration de sa position
        self.add_user = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Ajouter",
                                                command=self.add_user_window) 
        self.add_user.grid(row=0, column=0, pady=10, padx=20)

        # Bouton déclenchant la méthode delete_user_window + configuration de sa position
        self.delete_user = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Supprimer",
                                                command=self.delete_user_window) 
        self.delete_user.grid(row=0, column=1, pady=10, padx=20)

        # Bouton déclenchant la méthode users_info_window + configuration de sa position
        self.info_users = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Plus d'informations",
                                                command=self.users_info_window) 
        self.info_users.grid(row=1, column=0, pady=10, padx=20)

        # Bouton déclenchant la méthode modify_user_window + configuration de sa position
        self.modify_user = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Modifier",
                                                command=self.modify_user_window) 
        self.modify_user.grid(row=1, column=1, pady=10, padx=20)



    # Méthode ouvrant une fenêtre contenant tous les utilisateurs récupérés
    # Après une modification, il est nécessaire d'appuyer sur les onglets pour rafraîchir cette liste
    def list_all(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x300")
        window.title("Liste complète")
        window.grab_set()

        # Récupérer le nom des utilisateurs et les ajoute dans un string
        string_user_list = ''
        for user in user_and_group_listing.users:
            string_user_list += user["name"] + " \n"

        # Affiche tous les utilisateurs ajoutés précedemment à notre string
        self.user_list_all = customtkinter.CTkLabel(window,
                                            text=string_user_list)  
        self.user_list_all.grid(row=0, column=0, pady=10, padx=10)


    # Méthode qui permet de détruire le conteneur (top_frame) où l'on affiche nos utilisateurs 
    # Puis appel la méthode qui permet de créer graphiquement notre liste d'utilisateurs
    def refresh_users(self):
        self.top_frame.grid_forget()
        self.generate_users()
        

    # Méthode ayant pour but de générer graphiquement les utilisateurs que nous souhaitons affichés selon l'onglet dans lequel on se trouve
    def generate_users(self):
        
        # Création du conteneur principal + configuration de sa position
        self.top_frame = customtkinter.CTkFrame(master=self)
        self.top_frame.grid(row=1, column=0, padx=20, pady=20)
        

        # Création des titres du sommet des colonnes + configuration de leur position
        self.user_top_name = customtkinter.CTkLabel(master=self.top_frame,
                                              text="Nom:",
                                              text_font=("Roboto Medium", 14))  
        self.user_top_name.grid(row=0, column=0, pady=10, padx=10)
        self.user_top_admin = customtkinter.CTkLabel(master=self.top_frame,
                                              text="Administrateur:",
                                              text_font=("Roboto Medium", 14))  
        self.user_top_admin.grid(row=0, column=1, pady=10, padx=10)
        self.user_top_account = customtkinter.CTkLabel(master=self.top_frame,
                                              text="Compte:",
                                              text_font=("Roboto Medium", 14))  
        self.user_top_account.grid(row=0, column=2, pady=10, padx=10)
        self.user_top_comment = customtkinter.CTkLabel(master=self.top_frame,
                                              text="Commentaire:",
                                              text_font=("Roboto Medium", 14))  
        self.user_top_comment.grid(row=0, column=3, pady=10, padx=10, sticky="w")


        # Boucle qui va itérer dans notre liste d'utilisateur à afficher (users_to_display)
        for user in user_and_group_listing.users_to_display:

            # Déterminer quel est l'index de l'élément de la liste des utilisateurs à afficher
            index = user_and_group_listing.users_to_display.index(user)

            #Etiquette qui affiche le nom de l'utilisateur
            self.user_name = customtkinter.CTkLabel(master=self.top_frame,
                                            text=user["name"])  
            self.user_name.grid(row=(index+1), column=0, pady=10, padx=10)

            #Etiquette qui affiche le statut admin de l'utilisateur
            self.user_admin = customtkinter.CTkLabel(master=self.top_frame,
                                            text=user_and_group_listing.users_admin_to_display[index])  
            self.user_admin.grid(row=(index+1), column=1, pady=10, padx=10)

            #Etiquette qui affiche le statut du compte de l'utilisateur (activé/désactivé)
            self.user_account = customtkinter.CTkLabel(master=self.top_frame,
                                            text=user_and_group_listing.users_account_to_display[index])  
            self.user_account.grid(row=(index+1), column=2, pady=10, padx=10)

            #Etiquette qui affiche le commentaire associé à l'utilisateur
            self.user_comment = customtkinter.CTkLabel(master=self.top_frame,
                                            text=user["comment"]) 
            self.user_comment.grid(row=(index+1), column=3, pady=10, padx=10, sticky="w")



    # Méthode ouvrant une fenêtre pour rentrer l'utilisateur recherché
    def users_info_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x200")
        window.title("Plus d'informations")
        window.grid_columnconfigure(0, minsize=50)   
        window.grid_columnconfigure(2, minsize=50)   
        window.grab_set()

        # Fonction qui récupère la valeur entrée (un utilisateur) pour renvoyer dans le terminal les informations associées à celui-ci
        def users_info():
            # Récupération de la valeur entrée dans le champ d'entrée 
            username = username_entry.get()
            # Renvoie dans le terminal les informations associées à cet utilisateur
            os.system("net user " + username)
            # Destruction automatique de la fenêtre après l'éxecution de la fonction
            window.destroy()


        # Créer une étiquette pour le champ d'entrée et configure sa position
        username_label = customtkinter.CTkLabel(window, text="Indiquer l'utilisateur recherché")
        username_label.grid(row=0, column=1, pady=10, padx=10)

        # Créer le champ d'entrée et configure sa position
        username_entry = customtkinter.CTkEntry(window)
        username_entry.grid(row=1, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction users_info
        search_button = customtkinter.CTkButton(window, text="Rechercher", command=users_info)
        search_button.grid(row=2, column=1, pady=10, padx=10)



    # Méthode ouvrant une fenêtre pour entrer un utilisateur à créer
    def add_user_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x250")
        window.title("Ajout utilisateur")
        window.grab_set()

        # Fonction qui récupère les données et appel la fonction pour créer un utilisateur 
        def add_user():
            #Vérifie bien que l'utilisateur n'existe pas
            if username_entry.get() not in [user.get("name") for user in user_and_group_listing.users]:
                # Récupération des valeurs entrées dans les champs d'entrée
                username = username_entry.get()
                password = password_entry.get()
                comment = comment_entry.get() 

                # Appel de fonction pour ajouter un utilisateur dans le système
                manager.add_user(username, password, comment)
                # Destruction automatique de la fenêtre après l'éxecution de la fonction
                window.destroy()

            # S'il est trouvé alors on indique que celui-ci existe déjà
            else: 
                warning_label = customtkinter.CTkLabel(window, text="Cet utilisateur existe déjà")
                warning_label.grid(row=4, column=1, pady=10, padx=10)


        # Créer des étiquettes pour les champs d'entrée
        username_label = customtkinter.CTkLabel(window, text="Nom d'utilisateur:")
        password_label = customtkinter.CTkLabel(window, text="Mot de passe:")
        comment_entry = customtkinter.CTkLabel(window, text="Commentaire:")

        # Configuration de la disposition des étiquettes dans le système grid
        username_label.grid(row=0, column=0, pady=10, padx=10)
        password_label.grid(row=1, column=0, pady=10, padx=10)
        comment_entry.grid(row=2, column=0, pady=10, padx=10)


        # Création des champs d'entrée
        username_entry = customtkinter.CTkEntry(window)
        password_entry = customtkinter.CTkEntry(window, show="*")  # show="*" permet de cacher le mot de passe
        comment_entry = customtkinter.CTkEntry(window)

        # Configuration de la disposition des champs d'entrée  dans le système grid
        username_entry.grid(row=0, column=1, pady=10, padx=10)
        password_entry.grid(row=1, column=1, pady=10, padx=10)
        comment_entry.grid(row=2, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction add_user
        add_button = customtkinter.CTkButton(window, text="Ajouter utilisateur", command=add_user)
        add_button.grid(row=3, column=1, pady=10, padx=10)




    # Méthode ouvrant une fenêtre pour rentrer l'utilisateur à supprimer
    def delete_user_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("325x275")
        window.title("Suppression utilisateur")
        window.grab_set()
        window.grid_columnconfigure(0, minsize=50)  
        window.grid_columnconfigure(2, minsize=50)  

        # Fonction qui regarde si l'utilisateur existe et demande la confirmation de bien supprimer l'utilisateur entré
        def del_user_conf():
            # Si l'utilisateur existe, alors demande de confirmation
            if username_entry.get() in [user.get("name") for user in user_and_group_listing.users]:
                user_conf_label = customtkinter.CTkLabel(window, text="Êtes-vous sûr de supprimer\n cet utilisateur  ?")
                user_conf_label.grid(row=3, column=1, pady=25, padx=10)

                # Bouton qui déclenche la fonction del_user 
                user_conf_button = customtkinter.CTkButton(window, text="Oui", command=del_user)
                user_conf_button.grid(row=4, column=1, pady=10, padx=10)

            # Si l'utilisateur entré n'est pas trouvé, renvoie que celui-ci n'existe pas
            else: 
                warning_label = customtkinter.CTkLabel(window, text="Cet utilisateur n'existe pas")
                warning_label.grid(row=3, column=1, pady=25, padx=10)

        # Fonction qui récupère l'utilisateur entré et appel la fonction pour le supprimer du système
        def del_user():

            # Récupération des valeurs entrées dans les champs d'entrée
            username = username_entry.get()
            # Appel de fonction pour supprimer un utilisateur du système
            manager.delete_user(username)
            # Destruction automatique de la fenêtre après l'éxecution de la fonction
            window.destroy()

        # Créer une étiquette pour le champ d'entrée et configure sa position
        username_label = customtkinter.CTkLabel(window, text="Désigner l'utilisateur à supprimer")
        username_label.grid(row=0, column=1, pady=10, padx=10)

        # Créer le champ d'entrée et configure sa position
        username_entry = customtkinter.CTkEntry(window)
        username_entry.grid(row=1, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction del_user_conf
        delete_button = customtkinter.CTkButton(window, text="Supprimer utilisateur", command=del_user_conf)
        delete_button.grid(row=2, column=1, pady=10, padx=10)




    # Méthode ouvrant une fenêtre pour rentrer les modifications à apporter
    def modify_user_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x350")
        window.title("Modifier utilisateur")
        window.grab_set()

        # Fonction qui récupère les données et appel les fonctions pour les modifications des informations de l'utilisateur
        def modify_user():
            # Récupération des valeurs entrées dans les champs d'entrée 
            old_username = old_username_entry.get()
            new_username = new_username_entry.get()
            new_password = new_password_entry.get()
            new_comment = new_comment_entry.get() 
            new_account = new_account_combobox.get()

            # Vérifie si le nom d'utilisateur entré existe bien
            if old_username in [user.get("name") for user in user_and_group_listing.users]:

                # Affectation à une variable log un string qui servira de paramètre à la fonction log_writing se situant dans le fichier manager.py
                # Indique quel utilisateur est modifié dans le fichier log
                log = "Utilisateur modifié:" + old_username
                manager.log_writing(log)

                # Vérifie s'il existe une entrée dans le champs d'entrée mot de passe
                if new_password != '':
                    # Appel de fonction pour changer de mot de passe
                    manager.modify_password_user(old_username, new_password)

                # Vérifie s'il existe une entrée dans le champs d'entrée commentaire
                if new_comment != '':
                    # Appel de fonction pour changer le commentaire
                    manager.modify_comment_user(old_username, new_comment)

                # Détermine quelle valeur se situait dans le menu
                if new_account == "Désactivé":
                    # Appel de fonction pour désactiver l'utilisateur
                    manager.lock_user(old_username)
                    
                elif new_account == "Activé":
                    # Appel de fonction pour activer l'utilisateur
                    manager.unlock_user(old_username)

                # Vérifie s'il existe une entrée dans le champs d'entrée pour changer le nom d'utilisateur
                if new_username != '':
                    # Appel de fonction pour modifier le nom d'utilisateur
                    manager.modify_user(old_username, new_username)

                # Destruction automatique de la fenêtre après l'éxecution de la fonction
                window.destroy()

            # Indique à l'utilisateur que l'utilisateur entré n'existe pas
            else: 
                warning_label = customtkinter.CTkLabel(window, text="Cet utilisateur n'existe pas")
                warning_label.grid(row=6, column=1, pady=10, padx=10)
            

        # Créer des étiquettes pour les champs d'entrée
        old_username_label = customtkinter.CTkLabel(window, text="Utilisateur à modifier:")
        new_username_label = customtkinter.CTkLabel(window, text="Nouveau nom d'utilisateur:")
        new_password_label = customtkinter.CTkLabel(window, text="Nouveau mot de passe:")
        new_comment_label = customtkinter.CTkLabel(window, text="Nouveau commentaire:")
        new_account_state = customtkinter.CTkLabel(window, text="Activé le compte ?")

        # Configuration de la disposition des étiquettes dans le système grid
        old_username_label.grid(row=0, column=0, pady=10, padx=10)
        new_username_label.grid(row=1, column=0, pady=10, padx=10)
        new_password_label.grid(row=2, column=0, pady=10, padx=10)
        new_comment_label.grid(row=3, column=0, pady=10, padx=10)
        new_account_state.grid(row=4, column=0, pady=10, padx=10)


        # Création des champs d'entrée 
        old_username_entry = customtkinter.CTkEntry(window)
        new_username_entry = customtkinter.CTkEntry(window)
        new_password_entry = customtkinter.CTkEntry(window, show="*")  # show="*" permet de cacher le mot de passe
        new_comment_entry = customtkinter.CTkEntry(window)
        new_account_combobox = customtkinter.CTkComboBox(window,
                                     values=["Activé", "Désactivé"])

        # Configuration de la disposition des champs d'entrée  dans le système grid
        old_username_entry.grid(row=0, column=1, pady=10, padx=10)
        new_username_entry.grid(row=1, column=1, pady=10, padx=10)
        new_password_entry.grid(row=2, column=1, pady=10, padx=10)
        new_comment_entry.grid(row=3, column=1, pady=10, padx=10)
        new_account_combobox.grid(row=4, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction modify_user
        modify_button = customtkinter.CTkButton(window, text="Modifier utilisateur", command=modify_user)
        modify_button.grid(row=5, column=1, pady=10, padx=10)
