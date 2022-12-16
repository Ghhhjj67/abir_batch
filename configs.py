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
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5446345385:AAFm_jIJMV2903-cGX6cgyHUWZc9_xvl7Bk")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 5123176772))
    PRO_USERS = list({int(x) for x in os.environ.get("PRO_USERS", "0").split()})
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://file-to-link:file-to-link@fille-to-link.9fm5uz3.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001777759879"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    FROM_CHANNEL = int(os.environ.get("FROM_CHANNEL", "-1001865067204"))
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001541703053"))
    USERNAME = os.environ.get("USERNAME", "")
    TAG = os.environ.get("TAG", "")
    REMOVE_WORD = os.environ.get("REMOVE_WORD", "@Movies4u_team")#multiple word is must be seperated by |
    REMOVE_CAPTION = os.environ.get("REMOVE_CAPTION", "@Movies4u_team")#multiple word is must be seperated by |
