import os
from dotenv import load_dotenv

dotenv_path = '.env'
load_dotenv(dotenv_path=dotenv_path)

from plexapi.myplex import MyPlexAccount

myPlexAccount = MyPlexAccount(os.getenv('PLEX_USERNAME'), os.getenv('PLEX_PASSWORD'))
plexServer = myPlexAccount.resource(os.getenv('PLEX_SERVER')).connect()
library = plexServer.library

# Printing all library section names
for section in library.sections():
    print(section.title)

# Printing all usernames
users = myPlexAccount.users()
for user in users:
    # Ignores the guest user
    if user.username != "":
        print(user.username)

# Updates a friend
myPlexAccount.updateFriend(
    os.getenv('PLEX_USER_TO_CHANGE'),
    plexServer,
    library.sections(),
    allowSync=True,
    allowCameraUpload=False,
)
