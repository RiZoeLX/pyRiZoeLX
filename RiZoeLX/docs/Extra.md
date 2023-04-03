<h1> • pyRiZoeLX </h1>
<h2 align='center'> Module Name: Admins</h2>

<h3><code>broadcast_()</code></h3>
<b> Note: </b> <i> For IDs only! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import broadcast_
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("broadcast"))
async def broadcast(Client, Message):
   await broadcast_(Client, Message)
```

<h3><code>purge_()</code></h3>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import purge_
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.group & filters.command("purge"))
async def purge(Client, Message):
   await purge_(Client, Message)
```

<h3><code>srape()</code></h3>
<b> Info: </b> <i> Scrape users from chat, to chat! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import srape
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.group & filters.command("scrape"))
async def sraper_(Client, Message):
   from_group = "@DNHxHELL"
   to_group = "@ChatSutta"
   await srape(Client, Message, to_group, from_group)
```

<h3><code>custom_welcome()</code></h3>
<b> Info: </b> <i> Custom welcome message for new users! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import custom_welcome
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.new_chat_members)
async def _welcome(Client, Message):
   await custom_welcome(Client, Message)
```

<h3><code>makelist_()</code></h3>
<b> Info: </b> <i> Make list </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import makelist_

ids = "1111111111 2222222222 3333333333"
Users = makelist_(ids)
""" Output: Users = [1111111111, 2222222222, 3333333333] """
```

<h3><code>start_banall()</code></h3>
<b> Info: </b> <i> Ban all group members </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.group & filters.command("banall"))
async def banall_members(Client, Message):
   await start_banall(Client, Message)
```

----

<h3> Red7 - Watchers </h3>
<h4><code>Red7_Watch()</code></h4>
<b> Library: </b> Pyrogram

``` python 
from RiZoeLX.functions import Red7_Watch
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.all)
async def TeamRed7(Client, Message):
   await Red7_Watch(Client, Message)
```

<h4><code>Red7_Watch_telethon()</code></h4>
<b> Library: </b> Pyrogram

``` python 
from RiZoeLX.functions import Red7_Watch_telethon
from .. import bot
from telethon import events

@bot.on(events.NewMessage(incoming=True))
async def TeamRed7(message):
   await Red7_Watch_telethon(bot, message)
```
 
