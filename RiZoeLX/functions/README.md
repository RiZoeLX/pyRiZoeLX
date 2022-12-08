<h2> pyRiZoeLX - RiZoeLX </h2>

<h3> Example. </h3>

``` python
from RiZoeLX.functions import ban_user
from pyrogram import Client, filters 
from pyrogram import Message


@Client.on_message(filters.command("ban"))
async def ban_(client, message):
   await ban_user(client, message)
```

<h3 align="center"> Functions available! </h3>
<b> Function name: users </b> <br>

* <code>get_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/resources/USERS_USAGE.md#get_user)
* <code>get_user_reason()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/resources/USERS_USAGE.md#get_user_reason)
