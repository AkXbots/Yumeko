# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/NekoRobot/{config}", "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 14980683  # integer value, dont use ""
    API_HASH = "5bc2e9cd58092119e741c1f2b545c1bf"
    TOKEN = "5722771565:AAGif5G3SyWr7PB0vQ9yGL9WiXJbpNR604c"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    STRING_SESSION = ""
    MONGO_DB = "Shikimori"
    TEMP_DOWNLOAD_DIRECTORY= "./"
    MONGO_DB_URI = "mongodb+srv://eren:eren@cluster0.aor5rcv.mongodb.net/?retryWrites=true&w=majority"
    OWNER_ID = 5667156680  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "HSSLevii"
    HELP_IMG = "https://telegra.ph/file/717e1127686f864b5793c.jpg"
    SUPPORT_CHAT = "ZeroTwoMusic"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001801733203
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001609507640
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://pdepdgek:YLC10ZEJAjCC23wVGoNaL2qPsKMcsO6x@lucky.db.elephantsql.com/pdepdgek"  # needed for any database modules
    DB_URL = "postgres://bfkskrbbdynjrg:834c5e7774030cb4c00bea8049d32b96d555ae0b3078a751b243adc31e3d5ed5@ec2-3-89-230-115.compute-1.amazonaws.com:5432/dfp627imqb2maa"
    REDIS_URL = "redis://default:6vsajwd6wq3lNI7T3zMIpltTrU040DJC@redis-19248.c16.us-east-1-3.ec2.cloud.redislabs.com:19248"
    LOAD = []
    ARQ_API_KEY = "arq.hamker.dev"
    ARQ_API_KEY = "UMPYGF-MVNLVW-RTNXKA-FJWOUH-ARQ"
    ERROR_LOGS = -1001846183276
    BOT_NAME = "nezuko"
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    REM_BG_API_KEY = "PxCe5v4ZX3RmoQnPdDzf2TTz"
    SPAMWATCH_API = "QsrtejDpiLrvimOWSQeq6hpLNyMI_RIA_TfKExdSnBKE20I2gIXeDxBxYC76kLE6"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

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
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "VQ45LFKYPMJ2LKIU"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "65G8ZKE6050P"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "SOME1HING_privet_990022"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True  # Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
