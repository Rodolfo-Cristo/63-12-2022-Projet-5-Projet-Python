from email.message import EmailMessage
import ssl
import smtplib
import json
import log_adapter

#passe en argument le mail_receiver
def mail_send_log(email_receiver):
    #ouvrir le fichier JSON et charger les identifiants dans une variable
    with open('Config/connection.json') as f :
        password = json.load(f)
    with open(log_adapter.path2, 'r') as g :
        content = g.read()


    #recuperer les valeurs de chaque identifiant
    email_sender = password["email_sender"]
    email_password = password["email_password"]


    #contenu de l'email
    subject = 'Vos modifications des Users et des Groups'
    body = """
    Bonjour,

    Veuillez trouver ci-joint votre nouveau fichier de log comprenant les modifications que vous avez apportÃ©es.

    Cordialement, le groupe du projet 5.
    """

    #parametres de l'email
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    em.add_attachment(content, filename=log_adapter.path2)

    #connection au SMTP Gmail, envoi de l'email et deconnection du serveur
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp :
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        smtp.quit()
