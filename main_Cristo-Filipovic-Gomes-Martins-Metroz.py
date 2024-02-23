import log_adapter
import ftp_adapter


log_adapter.create_log()

# call all methods used
ftp_adapter.createftp()

ftp_adapter.sendftp("GroupsAndUsers.log")

# create the modified .log file with all modifications done 
with open(log_adapter.path2, "w") as f:
    f.close()

# import the user interface
import UI_main

# send the modified .log file to the ftp
ftp_adapter.sendftp("GroupsAndUsers_modified.log")  