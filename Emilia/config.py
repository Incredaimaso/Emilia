import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "ccbc3f662735abfa604ef6309ba76e67" # API_HASH from my.telegram.org
    API_ID = 22403100 # API_ID from my.telegram.org

    BOT_ID = 7784846976 # BOT_ID
    BOT_USERNAME = "AiHoshinoRbot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://sumitsajwan135:gameno01@cluster0.ja0i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "AnimeFantasyG" # Support Chat Username
    UPDATE_CHANNEL = "Piras_Official" # Update Channel Username
    START_PIC = "https://i.ibb.co/xtRNdRfv/a58ad309dec24355d46364036ab9d107.jpg" # Start Image
    DEV_USERS = [7950514048] # Dev Users
    TOKEN = "7784846976:AAF3_Xw4BWrakgKTJlKUGS8uUVh3MvaISvs" # Bot Token from @BotFather
    CLONE_LIMIT = 50 # Number of clones your bot can make

    EVENT_LOGS = -1002432275758 # Event Logs Chat ID
    OWNER_ID = 7950514048 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "𝗔𝗶 𝗛𝗼𝘀𝗵𝗶𝗻𝗼" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
