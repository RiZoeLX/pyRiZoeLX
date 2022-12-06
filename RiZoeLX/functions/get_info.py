

"""
   Pyrogram Module [Info lf individual user]
   
   from RiZoeL.functions import get_info
   await get_info(bot, message)
"""

from RiZoeLX import *

async def get_info(RiZoeL, message):
   args = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 1)
   if args:
      try:
         user = await RiZoeL.get_users(args[0])
      except Exception as error:
         await message.reply_text(str(error))
         return
   elif message.reply_to_message:
      try:
         user = await RiZoeL.get_users(message.reply_to_message.from_user.id)
      except Exception as error:
         user = message.reply_to_message.from_user
   else:
      await message.reply_text("You need to specify an user!")
      return

   info = "User Info! \n\n"
   info += f"First Name: {user.first_name} \n"
   if user.last_name:
     info += f"Last Name: {user.last_name} \n"
   info += f"User ID: {user.id} \n"
   if user.username:
     info += f"Username: @{user.username} \n"
   info += f"permit link: {} \n"
   if int(user.id) in Devs:
     info += f"Owner of @RiZoeLX 🔱\n"
   await message.reply_text(info, disable_web_page_preview=True)


"""
   Pyrogram Module [Info lf individual user]
   
   from RiZoeL.functions import get_id
   await get_id(bot, message)
"""
async def get_id(RiZoeL, message):
   args = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 1)
   if args:
      try:
         user = await RiZoeL.get_users(args[0])
      except Exception as error:
         await message.reply_text(str(error))
         return
   elif message.reply_to_message:
      try:
         user = await RiZoeL.get_users(message.reply_to_message.from_user.id)
      except Exception as error:
         user = message.reply_to_message.from_user
   else:
      try:
         user = await RiZoeL.get_users(message.from_user.id)
      except Exception as error:
         user = message.from_user
   chat = message.chat
   reply_msg = f"{user.first_name}'s ID: {user.id} \n"
   reply_msg += f"{chat.title}'s ID: {chat.id}"
   await message.reply_text(reply_msg)