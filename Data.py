#CodeXBotz #mrismanaziz

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
Pengguna Bot
  /start - Start
  /about - about
  /help - Help
  /ping - Check Ping
  /uptime - stats
 
Admin Bot
  /logs - Log
  /users - Users
  /batch - Multi Post
  /broadcast - Brodcast 
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Close", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("about", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
@{} is a bot for saving posts or files that can be accessed via a special link.

  Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
  Re-Code From: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man</a>
"""
