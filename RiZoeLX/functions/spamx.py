"""
   © RiZoeLX - SpamX
   functions of RiZoeLX/SpamX
"""

from RiZoeLX import *
from RiZoeLX.data import *
import random, asyncio 
from . import delete_reply


""" Get User with Reason! """
async def get_user_reason(RiZoeL, message, Owner, Sudos):
   args = ("".join(message.text.split(maxsplit=1)[1:])).split(" ", 2)
   if len(args) > 0:
      try:
         user = await RiZoeL.get_users(args[0])
      except Exception as error:
         await message.reply_text(str(error))
         return
      reason = args[1]
      if not reason:
         reason = None
   elif message.reply_to_message:
      try:
         user = await RiZoeL.get_users(message.reply_to_message.from_user.id)
      except Exception as error:
         user = message.reply_to_message.from_user
      reason = args[0]
      if not reason:
         reason = None
   else:
      await message.reply_text("You need to specify an user!")
      return

   if int(user.id) in Devs:
      await message.reply_text(f"{user.mention} is Owner/Dev of @RiZoeLX")
      return
   if int(user.id) == Owner:
      await message.reply_text(f"{user.mention} is owner of these bots!")
      return
   if int(user.id) in Sudos:
      if message.from_user.id != Owner:
        await message.reply_text(f"{user.mention} is Sudo User!")
        return

   return user, reason

async def get_user(RiZoeL, message, Owner, Sudos):
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

   if int(user.id) in Devs:
      await message.reply_text(f"{user.mention} is Owner/Dev of @RiZoeLX")
      return
   if int(user.id) == Owner:
      await message.reply_text(f"{user.mention} is owner of these bots!")
      return
   if int(user.id) in Sudos:
      if message.from_user.id != Owner:
        await message.reply_text(f"{user.mention} is Sudo User!")
        return

   return user

"""Spam functions"""
async def start_raid(RiZoeL, message, counts, user):
   chat = message.chat
   if chat.id in res_grps:
      await message.reply_text("**Sorry!** I can't raid here.")
      return
   if int(user.id) in Devs:
      await e.reply_text("I can't raid on @RiZoeLX's Owner")
      return
   for i in range(counts):
      raid = random.choice(raids.raid)
      await RiZoeL.send_message(chat.id, f"{user.mention} {raid}")
      await asyncio.sleep(0.3) 

async def start_spam(RiZoeL, message, counts, spam_text):
   chat = message.chat
   if chat.id in res_grps:
      await message.reply_text("**Sorry!** I can't spam here.")
      return
   if re.search(res_devs.lower(), spam_text.lower()):
      await message.reply_text(usage)("**Error!**")
      return
   for i in range(counts):
      await RiZoeL.send_message(chat.id, f"{spam_text} \n\n #{message.from_user.first_name} \n #SpamX -")
      await asyncio.sleep(0.3)
      
async def start_dspam(RiZoeL, message, counts, delay, spam_text):
   chat = message.chat
   if chat.id in res_grps:
      await message.reply_text("**Sorry!** I can't spam here.")
      return
   if re.search(res_devs.lower(), spam_text.lower()):
      await message.reply_text(usage)("**Error!**")
      return
   for i in range(counts):
      await RiZoeL.send_message(chat.id, f"{spam_text} \n\n #{message.from_user.first_name} \n #SpamX -")
      await asyncio.sleep(delay)

async def start_pspam(RiZoeL, message, counts):
   chat = message.chat
   if chat.id in res_grps:
      await message.reply_text("**Sorry!** I can't spam here.")
      return
   for i in range(counts):
      prn = random.choice(plinks)
      if ".jpg" in prn or ".png" in prn:
        await RiZoeL.send_photo(chat.id, prn)
        await asyncio.sleep(0.4)
      if ".mp4" in prn or ".MP4," in prn:
        await RiZoeL.send_video(chat.id, prn)
        await asyncio.sleep(0.4)

""" Global Functions"""
async def start_gban(RiZoeL, message, user, reason):
    try:    
       x = await message.reply_text("Gbanning...")
       common = await RiZoeL.get_common_chats(user.id)
       done = 0
       fuck = 0
       if not common:
          await delete_reply(message, x, f"User {user.mention} got no common chats with the specified one.")
          return
       for cht in common:  
         try:
           await RiZoeL.ban_chat_member(cht.id, user.id)
           done += 1
         except:
           fuck += 1
       if len(done) > 0:
          await delete_reply(message, x, f"User Gbanned ✓ \n\n User: {user.mention} \n Banned in `{done}` chats \n Failed in `{fuck}` chats")
       else:
          await delete_reply(message, x, f"user {user.mention} added in GBAN list!")

    except Exception as a:
      await message.reply_text(str(a))
      pass

async def start_gban(RiZoeL, message, user):      
    try:
       x = await message.reply_text("Gbanning...")
       common = await RiZoeL.get_common_chats(user.id)
       done = 0
       fuck = 0
       if not common:
         await delete_reply(message, x, f"User {user.mention} got no common chats with the specified one.")
         return
       for cht in common:  
         try:
           await RiZoeL.unban_chat_member(cht.id, user.id)
           done += 1
         except:
           fuck += 1
       if len(done) > 0:
         await delete_reply(message, x, f"User Ungbanned ✓ \n\n User: {user.mention} \n Unbanned in `{done}` chats \n Failed in `{fuck}` chats")
       else:
         await delete_reply(message, x, f"user {user.mention} added in UNGBAN list!")

    except Exception as a:
      await message.reply_text(str(a))
      pass


async def start_gpromote(RiZoeL, message, user):
   x = await message.reply_text("promoting globally...")
   common = await RiZoeL.get_common_chats(user.id)
   chat_len = len(common)
   if not common:
      await delete_reply(message, x, f"User {user.mention} got no common chats with the specified one.")
      return
   for cht in common:  
      try:
         await RiZoeL.promote_chat_member(cht.id, user.id, 
              can_change_info=True,
              can_manage_video_chats=True,
              can_delete_messages=True,
              can_restrict_members=True,
              can_invite_users=True,
              can_pin_messages=True,
              )
         done += 1
      except:
         fuck += 1
   if len(done) > 0:
      await delete_reply(message, x, f"User Globally Promoted ✓ \n\n User: {user.mention} \n total common chats: `{chat_len}` \n Promoted in `{done}` chats \n Failed in `{fuck}` chats")
   else:
      await delete_reply(message, x, "I don't have sufficient rights!!")


async def start_gdemote(RiZoeL, message, user):
   x = await message.reply_text("demoting globally...")
   common = await RiZoeL.get_common_chats(user.id)
   chat_len = len(common)
   if not common:
      await delete_reply(message, x, (f"User {user.mention} got no common chats with the specified one.")
      return
   for cht in common:  
      try:
         await RiZoeL.promote_chat_member(cht.id, user.id, 
              can_change_info=False,
              can_manage_video_chats=False,
              can_delete_messages=False,
              can_restrict_members=False,
              can_invite_users=False,
              can_pin_messages=False,
              )
         done += 1
      except:
         fuck += 1
   if len(done) > 0:
      await delete_reply(message, x, f"User Globally demoted ✓ \n\n User: {user.mention} \n total common chats: `{chat_len}` \n Promoted in `{done}` chats \n Failed in `{fuck}` chats")
   else:
      await delete_reply(message, x, "I don't have sufficient rights!!")
         

async def start_banall(RiZoeL, message):
   try:
      chat = message.chat
      x = RiZoeL.send_message("Hey it's SpamX!")
      done = 0
      failed = 0
      async for u in RiZoeL.get_chat_members(chat.id):
         user = u.user
         try:
           await RiZoeL.ban_chat_member(chat.id, user.id)
           done += 1
         except Exception as err:
           print(f"pyRiZoeLX - [INFO]: {str(err)}")
           failed += 1
      try:
         await x.edit_text(f"Members Banned ✓ \n\n Banned {done} users\n failed {failed}")
      except:
          await x.delete()
          await RiZoeL.send_message(chat.id, f"Members Banned ✓ \n\n Banned {done} users\n failed {failed}")
   except Exception as error:
      await message.reply_text(str(error))


def start_spamX(RiZoeLX, type):
    if type == "token":
      try:
         RiZoeLX.start()
         x = RiZoeLX.get_me()
         print(f"pyRiZoeLX - [INFO]: @{x.username} started ✓")
      except:
         RiZoeLX.start()
         print(f"pyRiZoeLX - [INFO]: Bot started ✓")
    else:
      try:
         RiZoeLX.start()
         try:
           RiZoeLX.join_chat("RiZoeLX")
           RiZoeLX.join_chat("DNHxHELL")
         except:
           pass
         x = RiZoeLX.get_me()
         print(f"pyRiZoeLX - [INFO]: @{x.first_name} started ✓")
      except:
         RiZoeLX.start()
         try:
           RiZoeLX.join_chat("RiZoeLX")
           RiZoeLX.join_chat("DNHxHELL")
         except:
           pass
         print(f"pyRiZoeLX - [INFO]: Client started ✓")
