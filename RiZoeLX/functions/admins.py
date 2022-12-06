"""
    © RiZoeLX
"""

import random
from RiZoeLX.data import admin_tags
from . import user_and_reason, user_only

async def ban_user(RiZoeL, message):
   user, reason = await user_and_reason(RiZoeL, message)
   if reason:
     try:
        await RiZoeL.ban_chat_member(message.chat.id, user.id)
        await message.reply_text(f"Banned {user.mention}! \nReason: {reason}")
     except Exception as eror:
        await message.reply_text(str(eror))
   else:
     try:
       await RiZoeL.ban_chat_member(message.chat.id, user.id)
       await message.reply_text(f"Banned {user.mention}!")
     except Exception as eror:
       await message.reply_text(str(eror))

async def unban_user(RiZoeL, message):
   user, reason = await user_and_reason(RiZoeL, message)
   if reason:
     try:
       await RiZoeL.unban_chat_member(message.chat.id, user.id)
       await message.reply_text(f"Unbanned {user.mention}! \nReason: {reason}")
     except Exception as eror:
       await message.reply_text(str(eror))
   else:
     try:
       await RiZoeL.unban_chat_member(message.chat.id, user.id)
       await message.reply_text(f"Unbanned {user.mention}!")
     except Exception as eror:
       await message.reply_text(str(eror))

async def promote_user(RiZoeL, message):
  chat = message.chat.id
  user, tag = await user_and_reason(RiZoeL, message)
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
  except Exception as eror:
     await message.reply_text(str(eror))

async def promote_user(RiZoeL, message):
  chat = message.chat.id
  user = await user_only(RiZoeL, message)
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
  except Exception as eror:
     await message.reply_text(str(eror))
