import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("16727482"))
API_HASH = os.getenv("55edb5638b3ce1b0dbeb00cc210525f2")
SESSION = os.getenv("AQBV7ePaQ-1KsMyt3nQ4B3r_3OynIIbLh2435b9EVHIr6mlOrBkCj9W3vWzoWst6Qq3OBmrd7lWk2qcEvDdeBBy2hFA2xq6AH-jcdE0o_kAzGzf3mZ6HraLD3h6JQYeZBeJIz8Vlp4xkh5qSpO-Mt4DqYLyYSEY3oJhkW2Wzp3wm2lDsH4OwA7_Ym2kzBLXNh2Spmg1mEoCclcsEa93MTX70lm_6RTv5OoaONtkx_mt_5Tyd95Sq5tp_92lOWgNkrEJ9BF5ZB4xu2IPjwlUQ6iRn-TXB9XShjzVWBrIpodM6vY3Cop6UQQ-eujj2CPvAlelfToTnlIxEDDG-UeHUfYkJAAAAATmGO98A")
HNDLR = os.getenv("HNDLR", "#")
SUDO_USERS = list(map(int, os.getenv("1254750804").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
