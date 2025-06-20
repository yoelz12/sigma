import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "1177196639").split()))

API_ID = int(os.getenv("API_ID", "26524260"))

API_HASH = os.getenv("API_HASH", "3153008964f2b934e7f45a1ba6d1a9fb")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7931871162:AAHMFTFfldJzcVjpXmIpTOQZ1BtURh-eoUU")

OWNER_ID = int(os.getenv("OWNER_ID", "1177196639"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aortulsk:KxCX5EQdssavL4dm@cluster0.qsywpr2.mongodb.net/")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4831032038"))
