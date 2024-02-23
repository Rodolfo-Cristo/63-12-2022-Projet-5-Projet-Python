import customtkinter
import os
import user_and_group_listing
import manager


# Création de la Frame droite concernant les groupes
class GroupsPage(customtkinter.CTkFrame):

    # Constructeur
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        # appel de la fonction group_display se trouvant dans le module user_and_group_listing
        # passage des listes XXXXX_1 du module user_and_group_listing en arguments dans la fonction
        # pour lors de l'appel de la méthode ci-dessous, on est quelque chose à afficher par défaut quand on ouvre la page des groupes 
        user_and_group_listing.group_display(user_and_group_listing.groups_1, user_and_group_listing.groups_nbr_users_1)

        # Appel de la méthode ayant pour but de générer graphiquement les groupes
        self.generate_groups()


        # Création du conteneur qui contiendra les boutons des Onglets + configuration de sa disposition
        self.tab_frame = customtkinter.CTkFrame(master=self)
        self.tab_frame.grid(row=2, column=0, sticky="w", padx=20, pady=20)


        # Création des boutons qui déclencheront l'actualisation de l'interface graphique grâce au passage des arguments dans la fonction group_display
        # Selon les arguments passés, on affiche une de nos sous liste provenant du module user_and_group_listing
        # + configuration de leur position
        tab_button_1 = customtkinter.CTkButton(master=self.tab_frame,
                                            text="Onglet 1",
                                            command= lambda : [user_and_group_listing.group_display(user_and_group_listing.groups_1, user_and_group_listing.groups_nbr_users_1), self.refresh_groups()])
        tab_button_1.grid(row=0, column=0, pady=10, padx=10)

        tab_button_2 = customtkinter.CTkButton(master=self.tab_frame,
                                             text="Onglet 2",
                                             command= lambda : [user_and_group_listing.group_display(user_and_group_listing.groups_2, user_and_group_listing.groups_nbr_users_2), self.refresh_groups()])
        tab_button_2.grid(row=0, column=1, pady=10, padx=10)

        tab_button_3 = customtkinter.CTkButton(master=self.tab_frame,
                                             text="Onglet 3",
                                             command= lambda : [user_and_group_listing.group_display(user_and_group_listing.groups_3, user_and_group_listing.groups_nbr_users_3), self.refresh_groups()])
        tab_button_3.grid(row=0, column=2, pady=10, padx=10)

        tab_button_4 = customtkinter.CTkButton(master=self.tab_frame,
                                             text="Onglet 4",
                                             command= lambda : [user_and_group_listing.group_display(user_and_group_listing.groups_4, user_and_group_listing.groups_nbr_users_4), self.refresh_groups()])
        tab_button_4.grid(row=0, column=3, pady=10, padx=10)


        # Bouton déclenchant la méthode list_all qui affiche tous les groupes dans 1 fenêtre + configuration de sa position
        self.refresh_button = customtkinter.CTkButton(master=self.tab_frame,
                                                text="Afficher la liste complète",
                                                command=self.list_all) 
        self.refresh_button.grid(row=0, column=4, pady=10, padx=20)

        # Création du conteneur qui contiendra les boutons concernant les modifications des groupes + configuration de sa position
        self.bottom_frame = customtkinter.CTkFrame(master=self)
        self.bottom_frame.grid(row=4, column=0, sticky="w", padx=20, pady=20)

        
        # Bouton déclenchant la méthode add_group_window + configuration de sa position
        self.add_group = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Ajouter",
                                                command=self.add_group_window) 
        self.add_group.grid(row=0, column=0, pady=10, padx=20)

        # Bouton déclenchant la méthode delete_group_window + configuration de sa position
        self.delete_group = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Supprimer",
                                                command=self.delete_group_window) 
        self.delete_group.grid(row=0, column=1, pady=10, padx=20)

        # Bouton déclenchant la méthode groups_info_window + configuration de sa position
        self.info_groups = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Plus d'informations",
                                                command=self.groups_info_window) 
        self.info_groups.grid(row=1, column=0, pady=10, padx=20)

        # Bouton déclenchant la méthode modify_group_window + configuration de sa position
        self.modify_group = customtkinter.CTkButton(master=self.bottom_frame,
                                                text="Modifier",
                                                command=self.modify_group_window) 
        self.modify_group.grid(row=1, column=1, pady=10, padx=20)


    # Méthode ouvrant une fenêtre contenant tous les groupes récupérés
    # Après une modification, il est nécessaire d'appuyer sur les onglets pour rafraîchir cette liste
    def list_all(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x300")
        window.title("Liste complète")
        window.grab_set()

        # Récupérer le nom des groupes et les ajoute dans un string
        string_group_list = ''
        for group in user_and_group_listing.groups:
            string_group_list += group["name"] + " \n"

        # Affiche tous les groupes ajoutés précedemment à notre string
        self.group_list_all = customtkinter.CTkLabel(window,
                                            text=string_group_list)  
        self.group_list_all.grid(row=0, column=0, pady=10, padx=10)


    # Méthode qui permet de détruire le conteneur (top_frame) où l'on affiche nos groupes 
    # Puis appel la méthode qui permet de créer graphiquement notre liste de groupes
    def refresh_groups(self):
        self.top_frame.grid_forget()
        self.generate_groups()
        

    # Méthode ayant pour but de générer graphiquement les groupes que nous souhaitons affichés selon l'onglet dans lequel on se trouve
    def generate_groups(self):

        # Création du conteneur principal + configuration de sa position
        self.top_frame = customtkinter.CTkFrame(master=self)
        self.top_frame.grid(row=1, column=0, padx=20, pady=20)
        
        # Création des titres du sommet des colonnes + configuration de leur position
        self.group_top_name = customtkinter.CTkLabel(master=self.top_frame,
                                              text="Nom:",
                                              text_font=("Roboto Medium", 14))  
        self.group_top_name.grid(row=0, column=0, pady=10, padx=10)
        self.group_top_admin = customtkinter.CTkLabel(master=self.top_frame,
                                              text="Quantité d'utilisateurs:",
                                              text_font=("Roboto Medium", 14))  
        self.group_top_admin.grid(row=0, column=1, pady=10, padx=10)
        self.group_top_comment = customtkinter.CTkLabel(master=self.top_frame,
                                              text="Commentaire:",
                                              text_font=("Roboto Medium", 14))  
        self.group_top_comment.grid(row=0, column=2, pady=10, padx=10, sticky="w")


        # Boucle qui va itérer dans notre liste de groupes à afficher (groups_to_display) à afficher
        for group in user_and_group_listing.groups_to_display:

            # Déterminer quel est l'index de l'élément de la liste des groupes à afficher
            index = user_and_group_listing.groups_to_display.index(group)

            #Etiquette qui affiche le nom du groupe
            self.group_name = customtkinter.CTkLabel(master=self.top_frame,
                                            text=group["name"])  
            self.group_name.grid(row=(index+1), column=0, pady=10, padx=10)

            #Etiquette qui affiche la quantité d'utilisateurs contenues dans le groupe
            self.group_admin = customtkinter.CTkLabel(master=self.top_frame,
                                            text=user_and_group_listing.groups_nbr_users_to_display[index])  
            self.group_admin.grid(row=(index+1), column=1, pady=10, padx=10)

            #Etiquette qui affiche le commentaire associé au groupe
            self.group_comment = customtkinter.CTkLabel(master=self.top_frame,
                                            text=group["comment"]) 
            self.group_comment.grid(row=(index+1), column=2, pady=10, padx=10, sticky="w")


    # Méthode ouvrant une fenêtre pour rentrer le groupe recherché
    def groups_info_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x200")
        window.title("Plus d'informations")
        window.grid_columnconfigure(0, minsize=50)   
        window.grid_columnconfigure(2, minsize=50)   
        window.grab_set()

        # Fonction qui récupère la valeur entrée (un groupe) pour renvoyer dans le terminal les informations associées à celui-ci
        def groups_info():
            # Récupération de la valeur entrée dans le champ d'entrée 
            group = group_entry.get()
            # Renvoie dans le terminal les informations associées à ce groupe
            os.system("net localgroup " + group)
            # Destruction automatique de la fenêtre après l'éxecution de la fonction
            window.destroy()


        # Créer une étiquette pour le champ d'entrée et configure sa position
        group_label = customtkinter.CTkLabel(window, text="Indiquer le groupe recherché")
        group_label.grid(row=0, column=1, pady=10, padx=10)

        # Créer le champ d'entrée et configure sa position
        group_entry = customtkinter.CTkEntry(window)
        group_entry.grid(row=1, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction groups_info
        search_button = customtkinter.CTkButton(window, text="Rechercher", command=groups_info)
        search_button.grid(row=2, column=1, pady=10, padx=10)



    # Méthode ouvrant une fenêtre pour entrer un groupe à créer
    def add_group_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x250")
        window.title("Ajout groupe")
        window.grab_set()

        # Fonction qui récupère les données et appel la fonction pour créer un groupe 
        def add_group():
            #Vérifie bien que le groupe n'existe pas
            if groupname_entry.get() not in [group.get("name") for group in user_and_group_listing.groups]:
                # Récupération des valeurs entrées dans les champs d'entrée
                groupname = groupname_entry.get()
                comment = group_comment_entry.get() 

                # Appel de fonction pour ajouter un groupe dans le système
                manager.add_group(groupname, comment)
                # Destruction automatique de la fenêtre après l'éxecution de la fonction
                window.destroy()

            # S'il est trouvé alors on indique que celui-ci existe déjà
            else: 
                warning_label = customtkinter.CTkLabel(window, text="Ce groupe existe déjà")
                warning_label.grid(row=3, column=1, pady=10, padx=10)


        # Créer des étiquettes pour les champs d'entrée
        groupname_label = customtkinter.CTkLabel(window, text="Nom du groupe:")
        comment_entry = customtkinter.CTkLabel(window, text="Commentaire:")

        # Configuration de la disposition des étiquettes dans le système grid
        groupname_label.grid(row=0, column=0, pady=10, padx=10)
        comment_entry.grid(row=1, column=0, pady=10, padx=10)

        # Création des champs d'entrée
        groupname_entry = customtkinter.CTkEntry(window)
        group_comment_entry = customtkinter.CTkEntry(window)

        # Configuration de la disposition des champs d'entrée  dans le système grid
        groupname_entry.grid(row=0, column=1, pady=10, padx=10)
        group_comment_entry.grid(row=1, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction add_group
        add_button = customtkinter.CTkButton(window, text="Créer groupe", command=add_group)
        add_button.grid(row=2, column=1, pady=10, padx=10)



    # Méthode ouvrant une fenêtre pour rentrer le groupe à supprimer
    def delete_group_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("325x275")
        window.title("Suppression groupe")
        window.grab_set()
        window.grid_columnconfigure(0, minsize=50)   # empty row with minsize as spacing
        window.grid_columnconfigure(2, minsize=50)   # empty row with minsize as spacing

        # Fonction qui regarde si le groupe existe et demande la confirmation de bien supprimer le groupe entré
        def del_group_conf():
            # Si le groupe existe, alors demande de confirmation
            if groupname_entry.get() in [group.get("name") for group in user_and_group_listing.groups]:
                group_conf_label = customtkinter.CTkLabel(window, text="Êtes-vous sûr de supprimer\n ce groupe  ?")
                group_conf_label.grid(row=3, column=1, pady=25, padx=10)

                # Bouton qui déclenche la fonction del_group 
                group_conf_button = customtkinter.CTkButton(window, text="Oui", command=del_group)
                group_conf_button.grid(row=4, column=1, pady=10, padx=10)

            # Si le groupe entré n'est pas trouvé, renvoie que celui-ci n'existe pas    
            else: 
                warning_label = customtkinter.CTkLabel(window, text="Ce groupe n'existe pas")
                warning_label.grid(row=3, column=1, pady=25, padx=10)

        # Fonction qui récupère le groupe entré et appel la fonction pour le supprimer du système
        def del_group():

            # Récupération des valeurs entrées dans les champs d'entrée
            groupname = groupname_entry.get()
            # Appel de fonction pour supprimer un groupe du système
            manager.delete_group(groupname)
            # Destruction automatique de la fenêtre après l'éxecution de la fonction
            window.destroy()
            
        # Créer une étiquette pour le champ d'entrée et configure sa position
        groupname_label = customtkinter.CTkLabel(window, text="Désigner le groupe à supprimer")
        groupname_label.grid(row=0, column=1, pady=10, padx=10)

        # Créer le champ d'entrée et configure sa position
        groupname_entry = customtkinter.CTkEntry(window)
        groupname_entry.grid(row=1, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction del_user_conf
        delete_button = customtkinter.CTkButton(window, text="Supprimer groupe", command=del_group_conf)
        delete_button.grid(row=2, column=1, pady=10, padx=10)




    # Méthode ouvrant une fenêtre pour rentrer les modifications à apporter
    def modify_group_window(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x350")
        window.title("Modifier groupe")
        window.grab_set()

        # Fonction qui récupère les données et appel les fonctions pour les modifications des informations du groupe
        def modify_group():
            # Récupération des valeurs entrées dans les champs d'entrée 
            old_groupname = old_groupname_entry.get()
            new_groupname = new_groupname_entry.get()
            new_comment_group = new_comment_group_entry.get() 
            new_user = new_user_entry.get()
            remove_user = remove_user_entry.get()

            # Vérifie si le nom du groupe entré existe bien
            if old_groupname in [group.get("name") for group in user_and_group_listing.groups]:

                # Affectation à une variable log un string qui servira de paramètre à la fonction log_writing se situant dans le fichier manager.py
                # Indique quel groupe est modifié dans le fichier log
                log = "Groupe modifié:" + old_groupname
                manager.log_writing(log)

                # Vérifie s'il existe une entrée dans le champs d'entrée commentaire
                if new_comment_group != '':
                    # Appel de fonction pour changer le commentaire
                    manager.modify_group_comment(old_groupname, new_comment_group)

                # Vérifie s'il existe une entrée dans le champs d'entrée new_user
                if new_user != '':
                    # Appel de fonction pour ajouter un utilisateur dans un groupe
                    manager.add_user_to_group(new_user, old_groupname)

                # Vérifie s'il existe une entrée dans le champs d'entrée remove_user
                if remove_user != '':
                    # Appel de fonction pour enlever un utilisateur d' un groupe
                    manager.remove_user_from_group(remove_user, old_groupname)

                # Vérifie s'il existe une entrée dans le champs d'entrée pour changer le nom du groupe
                if new_groupname != '':
                    # Appel de fonction pour modifier le nom d'un groupe
                    manager.modify_group(old_groupname, new_groupname)

                # Destruction automatique de la fenêtre après l'éxecution de la fonction
                window.destroy()

            # Indique à l'utilisateur que le groupe entré n'existe pas
            else: 
                warning_label = customtkinter.CTkLabel(window, text="Ce groupe n'existe pas")
                warning_label.grid(row=6, column=1, pady=10, padx=10)
            

        # Créer des étiquettes pour les champs d'entrée
        old_groupname_label = customtkinter.CTkLabel(window, text="Groupe à modifier:")
        new_groupname_label = customtkinter.CTkLabel(window, text="Nouveau nom de groupe:")
        new_comment_group_label = customtkinter.CTkLabel(window, text="Nouveau commentaire:")
        new_user_label = customtkinter.CTkLabel(window, text="Ajouter un utilisateur:")
        remove_user_state = customtkinter.CTkLabel(window, text="Retirer un utilisateur:")

        # Configuration de la disposition des étiquettes dans le système grid
        old_groupname_label.grid(row=0, column=0, pady=10, padx=10)
        new_groupname_label.grid(row=1, column=0, pady=10, padx=10)
        new_comment_group_label.grid(row=2, column=0, pady=10, padx=10)
        new_user_label.grid(row=3, column=0, pady=10, padx=10)
        remove_user_state.grid(row=4, column=0, pady=10, padx=10)

        # Création des champs d'entrée 
        old_groupname_entry = customtkinter.CTkEntry(window)
        new_groupname_entry = customtkinter.CTkEntry(window)
        new_comment_group_entry = customtkinter.CTkEntry(window)
        new_user_entry = customtkinter.CTkEntry(window)  
        remove_user_entry = customtkinter.CTkEntry(window)

        # Configuration de la disposition des champs d'entrée  dans le système grid
        old_groupname_entry.grid(row=0, column=1, pady=10, padx=10)
        new_groupname_entry.grid(row=1, column=1, pady=10, padx=10)
        new_comment_group_entry.grid(row=2, column=1, pady=10, padx=10)
        new_user_entry.grid(row=3, column=1, pady=10, padx=10)
        remove_user_entry.grid(row=4, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction modify_group
        modify_button = customtkinter.CTkButton(window, text="Modifier groupe", command=modify_group)
        modify_button.grid(row=5, column=1, pady=10, padx=10)

