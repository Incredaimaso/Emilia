import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "ccbc3f662735abfa604ef6309ba76e67" # API_HASH from my.telegram.org
    API_ID = 22403100 # API_ID from my.telegram.org

    BOT_ID = 7942335745 # BOT_ID
    BOT_USERNAME = "KatsuOneBot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://sumitsajwan135:gameno01@cluster0.ja0i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "AnimeFantasyG" # Support Chat Username
    UPDATE_CHANNEL = "Piras_Official" # Update Channel Username
    START_PIC = "https://i.ibb.co/4nwHCkbN/e3bc141e08f96d52299f25f1700e5ff0.jpg" # Start Image
    DEV_USERS = [7950514048] # Dev Users
    TOKEN = "7942335745:AAGFVnS-sEK-y1ZSL1Bsk8CtqTH4Pp7mb_U" # Bot Token from @BotFather
    CLONE_LIMIT = 5 # Number of clones your bot can make

    EVENT_LOGS = -1002432275758 # Event Logs Chat ID
    OWNER_ID = 7950514048 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "𝗕𝗼𝘁 𝗞𝗮𝘁𝘀𝘂" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
