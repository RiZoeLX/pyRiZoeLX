from .admins import *
from .get_info import *
from .get_user import *
from .list import *
from .scraper import *
from .spamx import * 


""" Edit Or Reply Function """
async def delete_reply(message, editor, text):
   try:
     await editor.edit_text(text)
   except:
     await editor.delete()
     await message.reply_text(text)
