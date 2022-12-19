"""
This file creates Assistant's client.
"""
from pyrogram import Client
from pyrogram.errors import FloodWait
from deadly.core import Core
import config





class Bot(Core, Client):
    """ Assistant (Laky) """
    def __init__(self):
        super().__init__(
            name="Nora",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN
	)
        try:
            self.start()
            self.me = self.get_chat("me")
            self.id = self.me.id
            self.dc_id = self.me.dc_id
            self.name = self.me.first_name
            self.username = f"@{self.me.username}"
            self.bio = self.me.bio if self.me.bio else ""
            self.pic = self.download_media(self.me.photo.big_file_id) if self.me.photo else None
            self.is_bot = True
            self.stop()
        except FloodWait as e:
            pass

        self.__class__.__module__ = "pyrogram.client"
