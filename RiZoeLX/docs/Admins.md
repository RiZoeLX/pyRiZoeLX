<h1> • pyRiZoeLX </h1>
<h2 align='center'> Module Name: Admins</h2>

<h3><code>ban_user()</code></h3>
<b> Info: </b> <i> Ban user from chat! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import ban_user
from pyrogram import Client, filters
from pyrogram import Message

@Client.on_message(filters.group & filters.command("ban"))
async def ban_(Client, Message):
   await ban_user(Client, Message)
```

<h3><code>unban_user()</code></h3>
<b> Info: </b> <i> Unban user from chat </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import unban_user
from pyrogram import Client, filters
from pyrogram import Message

@Client.on_message(filters.group & filters.command("unban"))
async def unban_(Client, Message):
   await unban_user(Client, Message)
```

<h3><code>promote_user()</code></h3>
<b> Info: </b> <i> Promote user! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import promote_user
from pyrogram import Client, filters
from pyrogram import Message

@Client.on_message(filters.group & filters.command("promote"))
async def promote_(Client, Message):
   await promote_user(Client, Message)
```

<h3><code>demote_user()</code></h3>
<b> Info: </b> <i> Demote user! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import demote_user
from pyrogram import Client, filters
from pyrogram import Message

@Client.on_message(filters.group & filters.command("demote"))
async def demote_(Client, Message):
   await demote_user(Client, Message)
```

<h3><code>mute_user()</code></h3>
<b> Info: </b> <i> Mute user! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import mute_user
from pyrogram import Client, filters
from pyrogram import Message

@Client.on_message(filters.group & filters.command("mute"))
async def mute_(Client, Message):
   await mute_user(Client, Message)
```

<h3><code>unmute_user()</code></h3>
<b> Info: </b> <i> Unmute user! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.funtions import unmute_user
from pyrogram import Client, filters
from pyrogram import Message

@Client.on_message(filters.group & filters.command("unmute"))
async def unmute_(Client, Message):
   await unmute_user(Client, Message)
```
