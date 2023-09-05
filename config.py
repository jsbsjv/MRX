import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = i))
API_HA
CHANNEL = os.getenv("@WWEEHHHH")
PHOTO_CH = os.getenv("PHOTO_CH")
HNDLR = os.getenv("HNDLR", 
contact_filter =
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Musicjepthon"))
call_py = PyTgCalls(bot)
