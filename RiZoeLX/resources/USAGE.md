<h1> RiZoeLX - pyRiZoeLX </h1>
<h2 align='center'> Module Name: Users </h2>
<b align='center'> Functions info and usage! </b> 
<h2> <code> get_user() </code> </h2>
<b> Info: </b> <i> Get user without any extra process! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import get_user
from pyrogram import Client, filters
from pyrogram import Message

@Client.on_message(filters.command("user"))
async def start(Client, Message):
   user = await get_user(Client, Message)
   await Message.reply(f"User's Name: {user.first_name} \n User's ID: {user.id}")
```
