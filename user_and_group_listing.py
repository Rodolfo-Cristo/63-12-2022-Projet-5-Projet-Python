import win32net
import win32netcon


""" Utilisateurs """

#Variable global pour stocker les utilisateurs
#Rodolfo: Variables liste séparées en 3 blocs: 

#Rodolfo: 1er bloc qui conserve les infos utilisateurs
users = [] #Rodolfo: Contient tous les utilisateurs dans le but de pouvoir les modifier dans l'interface grâce au fichier manager.py
users_to_display = []  #Rodolfo: Une liste qui sert à déterminer quel sous liste (ci-dessous) doit être afficher dans l'UI 
users_1 = [] #Rodolfo série de sous liste pour séparer les utilisateurs dans des onglets différents lors de l'affichage
users_2 = []
users_3 = []
users_4 = []

#Rodolfo: 2ème  bloc qui indique si l'utilisateur est admin pour le renvoyer à l'UI
users_admin = []
users_admin_to_display = []
users_admin_1 = []
users_admin_2 = []
users_admin_3 = []
users_admin_4 = []

#Rodolfo: 3ème bloc qui conserve l'état du compte utilisateur (actvé/désactivé) pour le renvoyer à l'UI
users_account = []
users_account_to_display  = []
users_account_1 = []
users_account_2 = []
users_account_3 = []
users_account_4 = []

#Rodolfo: fonctions qui permet de répartir les utilisateurs dans les sous listes
def add_to_small_users(user):
    if len(users_1) < 7:
        users_1.append(user)
    elif len(users_2) < 7:
        users_2.append(user)
    elif len(users_3) < 7:
        users_3.append(user)
    elif len(users_4) < 7:
        users_4.append(user)

#Rodolfo: fonctions qui permet de répartir le statut admin "oui"/"non" des utilisateurs dans des sous listes
def add_to_small_users_admin(user):
    if len(users_admin_1) < 7:
        users_admin_1.append(user)
    elif len(users_admin_2) < 7:
        users_admin_2.append(user)
    elif len(users_admin_3) < 7:
        users_admin_3.append(user)
    elif len(users_admin_4) < 7:
        users_admin_4.append(user)

#Rodolfo: fonctions qui permet de répartir le statut du compte "Activé"/"Désactivé" des utilisateurs dans des sous listes
def add_to_small_users_account(user):
    if len(users_account_1) < 7:
        users_account_1.append(user)
    elif len(users_account_2) < 7:
        users_account_2.append(user)
    elif len(users_account_3) < 7:
        users_account_3.append(user)
    elif len(users_account_4) < 7:
        users_account_4.append(user)


#Récupérer les infos et stocker dans des listes les utilisateurs à affichés
def create_user_list():
    #vider les listes pour les mises à jour des listes
    users.clear()
    users_to_display.clear()
    users_1.clear()
    users_2.clear()
    users_3.clear()
    users_4.clear()

    users_admin.clear()
    users_admin_to_display.clear()
    users_admin_1.clear()
    users_admin_2.clear()
    users_admin_3.clear()
    users_admin_4.clear()

    users_account.clear()
    users_account_to_display.clear()
    users_account_1.clear()
    users_account_2.clear()
    users_account_3.clear()
    users_account_4.clear()

    #récupération des infos systèmes
    info = win32net.NetUserEnum(None, 1)



    for user in info[0]:
        #Ajout de l'utilisateur à la liste des utilisateurs
        users.append(user)
        add_to_small_users(user) # Rodolfo: appel de la fonction pour répartir les utilisateurs

        #Ajout du statut admin à la liste admin
        if user["priv"] == 2:
            users_admin.append("Oui")
            add_to_small_users_admin("Oui") # Rodolfo: appel de la fonction pour récupérer le statut admin de l'user
        else: 
            users_admin.append("Non")
            add_to_small_users_admin("Non") 

        #Ajout du statut du compte(activé/désactivé) à la liste account
        if user["flags"] & win32netcon.UF_ACCOUNTDISABLE:
            users_account.append("Désactivé")
            add_to_small_users_account("Désactivé")# Rodolfo: appel de la fonction pour récupérer le statut du compte de l'user
        else:
            users_account.append("Activé")
            add_to_small_users_account("Activé")


#Rodolfo: fonction qui détermine quel sous liste doit être affiché dans l'UI
#Rodolfo: permet aussi de créer/update les listes générales: users, users_admin, users_account pour les modif système
def user_display(user_x, users_admin_x, users_account_x):
    #Rodolfo: Modifications des variables global
    global users_to_display
    global users_admin_to_display
    global users_account_to_display
    create_user_list() #Rodolfo: Récupération des infos systèmes
    users_to_display = user_x
    users_admin_to_display = users_admin_x
    users_account_to_display = users_account_x




""" Groupes """


#Rodolfo: le code ci-dessous(destiné aux groupes) reprend la même architecture et logique que le code ci-dessus(destiné aux users)
#Variable global pour stocker les groupes
groups = []
groups_to_display = []
groups_1 = []
groups_2 = []
groups_3 = []
groups_4 = []

groups_nbr_users = []
groups_nbr_users_to_display  = []
groups_nbr_users_1 = []
groups_nbr_users_2 = []
groups_nbr_users_3 = []
groups_nbr_users_4 = []


#Rodolfo: fonctions pour séparer les utilisateurs dans des sous listes
def add_to_small_groups(group):
    if len(groups_1) < 7:
        groups_1.append(group)
    elif len(groups_2) < 7:
        groups_2.append(group)
    elif len(groups_3) < 7:
        groups_1.append(group)
    elif len(groups_4) < 7:
        groups_3.append(group)

def add_to_small_groups_nbr(group):
    if len(groups_nbr_users_1) < 7:
        groups_nbr_users_1.append(group)
    elif len(groups_nbr_users_2) < 7:
        groups_nbr_users_2.append(group)
    elif len(groups_nbr_users_3) < 7:
        groups_nbr_users_3.append(group)
    elif len(groups_nbr_users_4) < 7:
        groups_nbr_users_4.append(group)


#Récupérer les infos et stocker dans des listes les groupes à affichés
def create_group_list():
    #vider les listes pour les mises à jour des listes
    groups.clear()
    groups_to_display.clear()
    groups_1.clear()
    groups_2.clear()
    groups_3.clear()
    groups_4.clear()

    groups_nbr_users.clear()
    groups_nbr_users_to_display.clear()
    groups_nbr_users_1.clear()
    groups_nbr_users_2.clear()
    groups_nbr_users_3.clear()
    groups_nbr_users_4.clear()

    #récupération des infos systèmes concernant les groupes
    info = win32net.NetLocalGroupEnum(None, 1)

    for group in info[0]:
        #Ajout du groupe à la liste des groupes
        groups.append(group)
        add_to_small_groups(group)


    #Renvoyer dans une liste la quantité d'utilisateur appartenant à un groupe
    info = [group for group in info if group]
    for group in info[:-1]:
        for names in group :
            name = names["name"]

            # Get the members of the group
            members, total, resume_handle = win32net.NetLocalGroupGetMembers(None, name, 0)
            groups_nbr_users.append(total)
            add_to_small_groups_nbr(total)

#Rodolfo: fonction qui détermine quel sous liste doit être affiché dans l'UI
#Rodolfo: permet aussi de créer/update les listes générales: groups, groups_nbr_users
def group_display(group_x, groups_nbr_users_x):
    global groups_to_display
    global groups_nbr_users_to_display
    create_group_list()
    groups_to_display = group_x
    groups_nbr_users_to_display = groups_nbr_users_x
