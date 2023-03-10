# (c) @AbirHasan2005
from bot.keep_alive import keep_alive
from typing import Union
from pyromod import listen
from pyrogram import Client as RawClient
from pyrogram.storage import Storage
from configs import Config
from bot.core.new import New
from bot.core.db.database import db
LOGGER = Config.LOGGER
log = LOGGER.getLogger(__name__)


class Client(RawClient, New):
    """ Custom Bot Class """

    def __init__(self, session_name: Union[str, Storage] = "RenameBot"):
        super().__init__(
            session_name,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="bot/plugins"
            )
        )

    async def start(self):
        await super().start()
        if not await db.get_bot_stats():
            await db.create_stats()
        log.info("Bot Started!")
        #keep_alive()

    async def stop(self, *args):
        await super().stop()
        log.info("Bot Stopped!")
