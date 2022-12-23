<h1> • pyRiZoeLX </h1>
<h2 align='center'> Module Name: Users </h2>

<h3><code>get_user()</code></h3>
<b> Info: </b> <i> Get user without any extra process! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import get_user
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("user"))
async def user_(Client, Message):
   user = await get_user(Client, Message)
   await Message.reply(f"User's Name: {user.first_name} \n User's ID: {user.id}")
```

<h3><code>get_user_reason()</code></h3>
<b> Info: </b> <i> Get user and reason/(extra) without any extra process! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import get_user
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("user"))
async def user_(Client, Message):
   user, reason = await get_user_reason(Client, Message)
   await Message.reply(f"User: {user.mention} \nReason: {str(reason)}")
```

<h3><code>get_info()</code></h3>
<b> Info: </b> <i> Get user's info (first name, last name, username, ID etc.) </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import get_info
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("info"))
async def info_(Client, Message):
   await get_info(Client, Message)
```

<h3><code>get_id()</code></h3>
<b> Info: </b> <i> Get user's ID and Chat ID </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import get_id
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("id"))
async def id_(Client, Message):
   await get_id(Client, Message)
```
