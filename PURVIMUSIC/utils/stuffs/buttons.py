from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/bots_update_all"),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/+AzKGhJreNmhiZTll")
    ],
    [
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG"),
        InlineKeyboardButton("˹ ʙᴧᴄᴋ ˼", callback_data=f"settingsback_helper")
    ]
    ]
