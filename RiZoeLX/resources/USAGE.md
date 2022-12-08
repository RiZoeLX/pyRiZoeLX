<h2> RiZoeLX - pyRiZoeLX </h2>

<h4 align='center'> Import; </h4>

``` python
from RiZoeLX.functions import <functions name>
```

<h3> Modules info and usage; </h3> 
<b> Name: </b> <code> get_user() </code> <br>
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
