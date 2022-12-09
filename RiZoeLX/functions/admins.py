"""
    © RiZoeLX
"""

import random
from RiZoeLX.data import admin_tags
from . import get_user_reason, get_user

#Errors
from pyrogram.errors import (ChatAdminRequired, RightForbidden, RPCError, UserNotParticipant)


async def ban_user(RiZoeL, message):
   user, reason = await get_user_reason(RiZoeL, message)
   try:
      await RiZoeL.ban_chat_member(message.chat.id, user.id)
   except ChatAdminRequired:
      await message.reply_text("I'm not admin or I don't have rights.")
      return
   except RightForbidden:
      await message.reply_text("I don't have enough rights to ban this user.")
      return 
   except UserNotParticipant:
      await message.reply_text("How can I mute a user who is not a part of this chat?")
      return 
   except RPCError as eror:
      await message.reply_text(str(eror))
      return 

   if reason:
      await message.reply_text(f"Banned {user.mention}! \nReason: {reason}")
   else:
      await message.reply_text(f"Banned {user.mention}!")

async def unban_user(RiZoeL, message):
   user, reason = await get_user_reason(RiZoeL, message)
   try:
      await RiZoeL.unban_chat_member(message.chat.id, user.id)
   except ChatAdminRequired:
      await message.reply_text("I'm not admin or I don't have rights.")
      return
   except RightForbidden:
      await message.reply_text("I don't have enough rights to ban this user.")
      return 
   except UserNotParticipant:
      await message.reply_text("How can I mute a user who is not a part of this chat?")
      return 
   except RPCError as eror:
      await message.reply_text(str(eror))
      return 

   if reason:
      await message.reply_text(f"Unbanned {user.mention}! \nReason: {reason}")
   else:
      await message.reply_text(f"Unbanned {user.mention}!")

async def promote_user(RiZoeL, message):
  chat = message.chat.id
  user, tag = await get_user_reason(RiZoeL, message)
  if tag:
    admin_tag = tag
  else:
    if user.is_bot:
      admin_tag = random.choice(bot_tags)
    else:
      admin_tag = random.choice(admin_tags)
  try:
     await RiZoeL.promote_chat_member(chat.id, user.id,
            can_change_info=False,
            can_post_messages=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_restrict_members=False,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
            )
     await RiZoeL.set_administrator_title(chat.id, user.id, admin_tag)
     await message.reply_text(f"Promoted {user.mention}!")
  except ChatAdminRequired:
     await message.reply_text("I'm not admin or I don't have rights.")
  except RightForbidden:
     await message.reply_text("I don't have enough rights to ban this user.")
  except UserNotParticipant:
     await message.reply_text("How can I mute a user who is not a part of this chat?")
  except RPCError as eror:
     await message.reply_text(str(eror))

async def promote_user(RiZoeL, message):
  chat = message.chat.id
  user = await get_user(RiZoeL, message)
  try:
     await RiZoeL.promote_chat_member(chat.id, user.id,
            is_anonymous=False,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
            )
     await message.reply_text(f"Demoted {user.mention}!")
  except ChatAdminRequired:
     await message.reply_text("I'm not admin or I don't have rights.")
  except RightForbidden:
     await message.reply_text("I don't have enough rights to ban this user.")
  except UserNotParticipant:
     await message.reply_text("How can I mute a user who is not a part of this chat?")
  except RPCError as eror:
     await message.reply_text(str(eror))


from pyrogram.types import ChatPermissions

async def mute_user(RiZoeL, message):
   user, reason = await get_user_reason(RiZoeL, message)
   try:
      await RiZoeL.restrict_chat_member(message.chat.id, user.id, ChatPermissions())
   except ChatAdminRequired:
      await message.reply_text("I'm not admin or I don't have rights.")
      return
   except RightForbidden:
      await message.reply_text("I don't have enough rights to ban this user.")
      return 
   except UserNotParticipant:
      await message.reply_text("How can I mute a user who is not a part of this chat?")
      return 
   except RPCError as eror:
      await message.reply_text(str(eror))
      return
   if reason:
      await message.reply_text(f"Muted {user.mention}! \nReason: {reason}")
   else:
      await message.reply_text(f"Muted {user.mention}!")

async def unmute_user(RiZoeL, message):
   user, reason = await get_user_reason(RiZoeL, message)
   try:
      await message.chat.unban_member(user.id) 
   except ChatAdminRequired:
      await message.reply_text("I'm not admin or I don't have rights.")
      return
   except RightForbidden:
      await message.reply_text("I don't have enough rights to ban this user.")
      return 
   except UserNotParticipant:
      await message.reply_text("How can I mute a user who is not a part of this chat?")
      return 
   except RPCError as eror:
      await message.reply_text(str(eror))
      return
   if reason:
      await message.reply_text(f"Unuted {user.mention}! \nReason: {reason}")
   else:
      await message.reply_text(f"Unuted {user.mention}!")
  
