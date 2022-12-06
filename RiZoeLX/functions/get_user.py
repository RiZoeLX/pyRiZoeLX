

async def user_and_reason(RiZoeL, message):
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

   return user, reason


async def user_only(RiZoeL, message):
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

   return user
