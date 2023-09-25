import json
import os


def get_user_list(config, key):
    with open("{}/NekoRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "22111689"
    API_HASH = "245005e2737bf35431cc035328a20860"
    TOKEN = "6596295603:AAE0I2x0M61hdcLd5WbqC7xyBRCsswe4M3Q"
    OWNER_ID = "6526659607"
    OWNER_USERNAME = "Velin"
    SUPPORT_CHAT = "pegasusfederation2"
    JOIN_LOGGER = -1001960654405
    EVENT_LOGS = -1001960654405

    SQLALCHEMY_DATABASE_URI = "postgres://deujfgcn:c2IPY0hiXm6oLW1Yg-G136bMG48XV4RQ@floppy.db.elephantsql.com/deujfgcn"
    MONGO_DB_URI = "mongodb+srv://<velinxd>:<xloaderhell>@cluster0.2pjepfq.mongodb.net/"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = ""
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
   # ARQ_API_KEY = None
   #ARQ_API_URL = None
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
