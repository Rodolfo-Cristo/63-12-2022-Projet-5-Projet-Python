import datetime
import pathlib
import win32net
import win32security

# file path to open and create a .log file
path = str(pathlib.Path.cwd()) + "\GroupsAndUsers.log"
path2 = str(pathlib.Path.cwd()) + "\GroupsAndUsers_modified.log"

# get date and time
def get_datetime():
    # date format
    date_time = datetime.datetime.now()
    string_date = date_time.strftime("%d %B %Y, %H:%M:%S ")

    return string_date

# fonction to write data in the .log file in the actual folder
def create_log():

    # create and open the .log file in the actual folder with the "write" mode
    with open(path, "w", encoding="utf-8") as f:

        # write date and time of execution
        f.write(get_datetime() + "\n")

        groups = win32net.NetLocalGroupEnum(None, 0)

        # filter out empty or null elements from the list
        groups = [group for group in groups if group]

        # iterate through each group
        for group in groups[:-1]:
            for names in group :
                name = names["name"]
            # get the name of the group

                f.write(f"Group name: {name} \n")

                # get the members of the group
                members = win32net.NetLocalGroupGetMembers(None, name, 0)
                for member in members[:-2]:
                    for sids in member :
                    # get the sid of the user
                        sid = sids["sid"]
                        # convert the sid to a username
                        username, domain, type = win32security.LookupAccountSid(None, sid)
                        f.write(f"User:       {username} \n")

        # close file
        f.close()


