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
    API_ID = int(os.environ.get("API_ID", "18860540"))
    API_HASH = os.environ.get("API_HASH", "22dd2ad1706199438ab3474e85c9afab")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5964736220:AAE0XLloB3IuObZtyi3EN5M1EKKiEAv4bBw")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 5123176772))
    PRO_USERS = list({int(x) for x in os.environ.get("PRO_USERS", "0").split()})
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://abc:abc@cluster01.98xu6iz.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001718574234"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    FROM_CHANNEL = int(os.environ.get("FROM_CHANNEL", "-1001718574234"))
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001541703053"))
    CH_USERNAME = os.environ.get("CH_USERNAME", "@seaofallmovies")
    TAG = os.environ.get("TAG", "💥Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ💥 ❤️ @seaofallmovies❤️")
    REMOVE_WORD = os.environ.get("REMOVE_WORD", "💥Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ💥❤️ @BuLMoviee ❤️|💥Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ💥❤️ @SIDHUU5911 ❤️|@BuLMoviee Join Us On Telegram|Join Us On Telegram|@JESSEVERSE|@Jesseverse|@BuLMoviee_Join_Us_On_Telegram_|@BuLMoviee")#multiple word is must be seperated by |
    REMOVE_CAPTION = os.environ.get("REMOVE_CAPTION", "💥Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ💥❤️ @BuLMoviee ❤️|💥Join Us Oɴ Tᴇʟᴇɢʀᴀᴍ💥❤️ @SIDHUU5911 ❤️|@BuLMoviee Join Us On Telegram|Join Us On Telegram|@JESSEVERSE|@Jesseverse|@BuLMoviee_Join_Us_On_Telegram_|@BuLMoviee")#multiple word is must be seperated by |
    DP_PASTE = os.environ.get("DP_PASTE",True)#do True if u want paste ur thumnail on video default thumbnail
