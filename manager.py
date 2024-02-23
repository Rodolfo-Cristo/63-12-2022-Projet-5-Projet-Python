import os
import log_adapter


#Function to write in the 2nd log file
def log_writing(log):
    with open(log_adapter.path2, "a", encoding="utf-8") as f:
        f.write(log_adapter.get_datetime() + log + " \n")
        f.close()


#Utilisateurs
def add_user(username, password, comment):
    # add user
    os.popen("net user " + username + " " + password + " /add" + " /comment:" + comment)
    log = " Utilisateur créé: " + username
    log_writing(log)

def delete_user(username):
    # delete user
    os.popen("net user " + username + " /delete")
    log = " Utilisateur supprimé: " + username
    log_writing(log)


def modify_user(old_username, new_username):
    # modify user
    os.popen("wmic useraccount where name=\"" + old_username + "\" call rename \"" + new_username + "\"")
    log = " Nouveau nom d'utilisateur: " + new_username 
    log_writing(log)


def lock_user(username):
    # Lock an user
    os.popen("net user {} /active:no".format(username))
    log = " L'utilisateur " + username + " est maintenant désactivé"
    log_writing(log)

    
def unlock_user(username):
    # Unlock an user
    os.popen("net user {} /active:yes".format(username))
    log = " L'utilisateur " + username + " est maintenant activé"
    log_writing(log)


def modify_comment_user(username, comment):
    # Change comment of an user
    os.popen("net user " + username + " /comment:" + comment)
    log = " Nouveau commentaire: " + comment
    log_writing(log)


def modify_password_user(username, password):
    # Change password of an user
    os.popen("net user " + username + " " + password)
    log = " Mot de passe changé"
    log_writing(log)




#Groupes

def add_group(group_name, comment):
    # add group
    os.popen("net localgroup " + group_name + " /add")
    os.popen("net localgroup " + group_name + " /comment:" + comment)
    log = " Groupe créé: " + group_name
    log_writing(log)

def delete_group(group_name):
    # delete group
    os.popen("net localgroup " + group_name + " /delete")
    log = " Groupe supprimé: " + group_name
    log_writing(log)

def modify_group(old_group_name, new_group_name):
    # modify group
    os.popen("wmic group where name=\"" + old_group_name + "\" call rename \"" + new_group_name + "\"")
    log = " Nouveau nom de groupe: " + new_group_name
    log_writing(log)

def modify_group_comment(old_group_name, new_comment):
    # modify group comment
    os.popen("net localgroup " + old_group_name + " /comment:" + new_comment)
    log = " Nouveau commentaire: " + new_comment
    log_writing(log)


def add_user_to_group(username, group_name):
    # Ajouter l'utilisateur à un groupe
    os.popen("net localgroup " +  group_name + " " +username + " /add")
    log = " Utilisateur " + username + " ajouté au groupe " + group_name
    log_writing(log)


def remove_user_from_group(username, group_name):
    # Supprimer l'utilisateur d'un groupe
    os.system("net localgroup " +  group_name + " " + username + " /delete")
    log = " Utilisateur " + username + " retiré du groupe " + group_name
    log_writing(log)



