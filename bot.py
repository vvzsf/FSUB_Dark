#CodeXBotz #mrismanaziz

import pyromod.listen
import sys

from pyrogram import Client, enums

from config import (
    API_HASH,
    API_ID,
    CHANNEL_DB,
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
    LOGGER,
    BOT_TOKEN,
    WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins"},
            workers=WORKERS,
            bot_token=BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"BOT_TOKEN detected!\n"
                f"  Username: @{self.username}\n\n"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            sys.exit()

        if FORCE_SUB_1:
            try:
                info = await self.get_chat(FORCE_SUB_1)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = info.invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_1 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} "
                    "become Admin at FORCE_SUB_1\n\n"
                )
                sys.exit()
        if FORCE_SUB_2:
            try:
                info = await self.get_chat(FORCE_SUB_2)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_2)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_2 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} "
                    "become Admin at FORCE_SUB_2\n\n"
                )
                sys.exit()
        if FORCE_SUB_3:
            try:
                info = await self.get_chat(FORCE_SUB_3)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = info.invite_link
                self.invitelink3 = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_3 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} "
                    "become Admin at FORCE_SUB_3\n\n"
                )
                sys.exit()
        if FORCE_SUB_4:
            try:
                info = await self.get_chat(FORCE_SUB_4)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_4)
                    link = info.invite_link
                self.invitelink4 = link
                self.LOGGER(__name__).info(
                    "FORCE_SUB_4 Detected!\n"
                    f"  Title: {info.title}\n"
                    f"  Chat ID: {info.id}\n\n"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Make sure @{self.username} "
                    "become Admin at FORCE_SUB_4\n\n"
                )
                sys.exit()


        try:
            db_channel = await self.get_chat(CHANNEL_DB)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Bot Aktif!\n\n")
            await test.delete()
            self.LOGGER(__name__).info(
                "CHANNEL_DB Detected!\n"
                f"  Title: {db_channel.title}\n"
                f"  Chat ID: {db_channel.id}\n\n"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Make sure @{self.username} "
                    "become Admin at FORCE_SUB_DB\n\n"
            )
            sys.exit()

        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            "Active Bot!\n\n"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stop!\n\n")
