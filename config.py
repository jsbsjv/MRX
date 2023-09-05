import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("27340824"))
API_HASH = os.getenv("a17d5851512b2af6b0d97008281f2740")
SESSION = os.getenv("1ApWapzMBu5F7jVD3h0InU01KEXQHFMrMEnA6oEJ0qdMzl9hVtXmfhjIDa4zaHYWkCVV3lhaTHXwHVRPYTHJYi2eG6qMJCRe_1i9ptKV0jWRiBV3za1C1-M7CqU11rIMC6k32Ev7Cmxe6bXmT65WiZCxTN_O6v_1IXuCNxZsZ_t35Rh67rPEwK_E_iTJ9uaQYZWC-xOfwhXs7PZnfT249M0CFvivC2OxOSAlBhSYbH2-LWOVGq-c2HJwlgkJuW-w5j80etgzSqZiw9TQRvMDJxJ0BhwulBiqzeY3nHI328vIewRV-Km71YOYlsONR0Tq8B_JFMe51d9glJnBohDDxHa20Glq-Yzo=")
OWNER_NAME = os.getenv("@EC_60")
CHANNEL = os.getenv("@WWEEHHHH")
PHOTO_CH = os.getenv("PHOTO_CH")
HNDLR = os.getenv("HNDLR", "")
SUDO_USERS = list(map(int, os.getenv("@SC_60").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Musicjepthon"))
call_py = PyTgCalls(bot)
