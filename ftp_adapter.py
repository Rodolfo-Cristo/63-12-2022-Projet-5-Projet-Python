import ftplib
import json

# method to connect to server and create ftp path
def createftp():
    with open('Config/connection.json') as f:
        data = json.load(f)

    # FTP server details
    FTP_SERVER = data['host']
    FTP_USERNAME = data['username']
    FTP_PASSWORD = data['password']

    # connect to FTP server
    ftp = ftplib.FTP(FTP_SERVER)
    ftp.login(FTP_USERNAME, FTP_PASSWORD)

    directories = ftp.nlst()
    
    # check if directories exist so then delete already existing logs
    if "6312_Python_2022" in directories:
        for file in ftp.nlst("6312_Python_2022/Proj5_Group9_Win"):
            if file != "6312_Python_2022/Proj5_Group9_Win/." and file != "6312_Python_2022/Proj5_Group9_Win/..":
                ftp.delete(file)
    else:
        #create the directories
        ftp.mkd("6312_Python_2022") 
        ftp.cwd("/6312_Python_2022")
        ftp.mkd("Proj5_Group9_Win") 

    # Close the FTP connection
    ftp.quit()
    
# method to send .log file to ftp
def sendftp(filename_ftp):
    with open('Config/connection.json') as f:
        data = json.load(f)

    # FTP server details    
    FTP_SERVER = data['host']
    FTP_USERNAME = data['username']
    FTP_PASSWORD = data['password']

    # Connect to FTP server
    ftp = ftplib.FTP(FTP_SERVER)
    ftp.login(FTP_USERNAME, FTP_PASSWORD)

    # get in the directory
    ftp.cwd("/6312_Python_2022/Proj5_Group9_Win")

    # Send the log files to the FTP server
    with open(filename_ftp, 'rb') as f:
        ftp.storlines('STOR ' + filename_ftp, f)

    # Close the FTP connection
    ftp.quit()