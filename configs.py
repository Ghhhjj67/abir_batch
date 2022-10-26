# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

from dotenv import load_dotenv
load_dotenv()
class Config(object):
    API_ID = int(os.environ.get("API_ID", "8813038"))
    API_HASH = os.environ.get("API_HASH", "780fd96b159baa710dada78ff1621b54")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5773205742:AAFSygtZMc_9ow_miS4sWmn5Rw0vQZMdoOc")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 2083503061))
    PRO_USERS = list({int(x) for x in os.environ.get("PRO_USERS", "0").split()})
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://abcd:abcd@cluster0.od5wfzt.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001884096843"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    FROM_CHANNEL = int(os.environ.get("FROM_CHANNEL", "-1001880691367"))
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001785157194"))
    USERNAME = os.environ.get("USERNAME", "@filmyfunda_movies")
    TAG = os.environ.get("TAG", "_Rᴏʟᴇx_")
