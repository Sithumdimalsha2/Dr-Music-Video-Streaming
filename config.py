from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Give_Me_Heart")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Shayri_Music_Lovers")
BOT_USERNAME = getenv("BOT_USERNAME")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/b37bf4913fd832576331b.png")
THUMB_IMG = getenv("THUMB_IMG", "https://te.legra.ph/file/b37bf4913fd832576331b.png")
BOT_IMG = getenv("BOT_IMG", "https://te.legra.ph/file/b37bf4913fd832576331b.png")
AUD_IMG = getenv("AUD_IMG", "https://te.legra.ph/file/d044fc193e29db59c58ad.png")
QUE_IMG = getenv("QUE_IMG", "https://te.legra.ph/file/d044fc193e29db59c58ad.png")

admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

OWNER_ID = int(getenv("OWNER_ID"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
