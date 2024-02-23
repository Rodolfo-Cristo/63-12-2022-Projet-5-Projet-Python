import customtkinter #Version  == 4.6.3
import UI_users
import UI_groups
import email_projet

# Configuration de l'apparence de la fenêtre (couleur de la fenêtre, couleurs des boutons)
customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("blue")  

# Création de la fenêtre principale
class Menu(customtkinter.CTk):

    # Constructeur
    def __init__(self):
        super().__init__()


        self.title("Projet python") # Titre de la fenêtre
        self.geometry(f"{1280}x{800}") # Taille de la fenêtre au lancement
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Appel la méthode on_closing() lors de la fermeture de la fenêtre

        # Crée 2 Frames qui serviront de conteneur

        # Configuration de la disposition en grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Configuration de la Frame gauche qui va nous permettre de naviguer entre nos pages
        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        # Configuration de la Frame droite, là où l'on va afficher nos informations
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


        # Frame gauche

        # Configuration de le disposition à l'intérieur de notre Frame gauche
        # Ligne vide qui serviront à espacer nos éléments
        self.frame_left.grid_rowconfigure(0, minsize=10)   
        self.frame_left.grid_rowconfigure(5, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)    
        self.frame_left.grid_rowconfigure(11, minsize=10)  

        # Bouton qui appel la méthode permettant de changer notre Frame gauche et qui nous renvoie vers les utilisateurs
        self.list_users = customtkinter.CTkButton(master=self.frame_left,
                                                text="Utilisateurs",
                                                command= lambda : self.show_frame(UI_users.UsersPage))
        self.list_users.grid(row=2, column=0, pady=10, padx=20)

        # Bouton qui appel la méthode permettant de changer notre Frame gauche et qui nous renvoie vers les groupes
        self.list_groups = customtkinter.CTkButton(master=self.frame_left,
                                                text="Groupes",
                                                command= lambda : self.show_frame(UI_groups.GroupsPage))
        self.list_groups.grid(row=3, column=0, pady=10, padx=20)

        # Etiquette servant d'indication au menu ci-dessous
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Thème:")
        self.label_mode.grid(row=8, column=0, pady=0, padx=20, sticky="w")

        # Menu qui nous permet de changer l'apparence de la fenêtre (couleur de la fenêtre)
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Dark", "Light", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        # Bouton qui appel la méthode ouvrant la fenêtre permettant d'inscrire le mail à qui envoyer le fichier log contenant les modifications
        self.terminer = customtkinter.CTkButton(master=self.frame_left,
                                                text="Terminer et envoyer",
                                                border_width=2,
                                                command=self.send_log_window) 
        self.terminer.grid(row=10, column=0, pady=10, padx=20)



        # Frame droite

        self.frames = {}

        # Initialise la Frame de l'objet de UsersPage et GroupsPage provenant respectivement des fichiers UI_users.py et UI_groups.py dans une boucle 
        for F in (UI_users.UsersPage, UI_groups.GroupsPage):
            frame = F(self.frame_right, self)
  
            self.frames[F] = frame
  
            # Place la Frame droite de manière à se coller sur tous les côté de sa cellule grid
            frame.grid(row = 0, column = 0, sticky ="nsew")

        # Indique la Frame droite par défaut à afficher lors de l'ouverture initial de l'interface
        self.show_frame(UI_users.UsersPage)


    # Méthode qui permet de créé une fenêtre  
    # Permet de rentrer l'e-mail du destinataire à qui envoyer le fichier log contenant les modifications
    def send_log_window(self):

    # Note: Cette structure de fenêtre est reprise à chaque fois que l'on crée une fenêtre
        window = customtkinter.CTkToplevel(self)
        # Taille de la fenêtre à l'ouverture
        window.geometry("300x200")
        # Titre de la fenêtre
        window.title("Envoi")
        # Configuration de l'espace dans la fenêtre
        window.grid_columnconfigure(0, minsize=50)   
        window.grid_columnconfigure(2, minsize=50)   
        # empêcher l'interaction avec la menu principal lorsque la fenêtre est ouverte
        window.grab_set()

        # Envoie le fichier log à l'adresse entrée
        def send_log():
            # Récupère le mail donné dans le champ d'entrée
            mail = mail_entry.get()
            # Appel la fonction mail_send_log du fichier email_projet de Marko + passage en paramètre du mail du destinataire
            email_projet.mail_send_log(mail)
            # Destruction automatique de la fenêtre après l'éxecution de la fonction
            window.destroy()

        # Etiquette qui indique quoi rentrer dans le champ à l'utilisateur
        mail_label = customtkinter.CTkLabel(window,
                                            text="Indiquer l'e-mail du destinataire")
        mail_label.grid(row=0, column=1, pady=10, padx=10)

        # Champ d'entrée pour rentrer le mail du destinataire
        mail_entry = customtkinter.CTkEntry(window)
        mail_entry.grid(row=1, column=1, pady=10, padx=10)

        # Bouton déclenchant la fonction send_log ci-dessus
        search_button = customtkinter.CTkButton(window,
                                                text="Envoyer",
                                                command=send_log)
        search_button.grid(row=2, column=1, pady=10, padx=10)

    # Méthode qui permet d'afficher une Frame spécifique (l'argument cont)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # Méthode qui permet de changer le background de l'interface
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Méthode qui détruit la fenêtre lorsqu'on la ferme
    def on_closing(self, event=0):
        self.destroy()




# Lancement de l'interface
Menu().mainloop()

"""
Note, on ne déclare pas :
if __name__ == "__main__":
    Menu().mainloop()
dans le but de pouvoir lancer l'interface directement lorsqu'elle est importée dans main.py

"""





    
