<h2> pyRiZoeLX - RiZoeLX </h2>

<h3> Example. </h3>

``` python
from RiZoeLX.functions import ban_user
from pyrogram import Client, filters 
from pyrogram.types import Message


@Client.on_message(filters.command("ban"))
async def ban_(client, message):
   await ban_user(client, message)
```

<h3 align="center"> Functions available! </h3>
<b> Function name: </b><i>Users</i><br>

* <code>get_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Users.md#get_user)
* <code>get_user_reason()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Users.md#get_user_reason)
* <code>get_info()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Users.md#get_info)
* <code>get_id()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Users.md#get_id)

----

<b> Function name: </b><i>Admins</i><br>

* <code>ban_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Admins.md#ban_user)
* <code>unban_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Admins.md#unban_user)
* <code>promote_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Admins.md#promote_user)
* <code>demote_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Admins.md#demote_user)
* <code>mute_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Admins.md#mute_user)
* <code>unmute_user()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Admins.md#unmute_user)

----

<b> Function name: </b><i>Filters</i><br>

* <code>sudo_filter()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Filters.md#sudo_filter)
* <code>me_filter()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Filters.md#me_filter)
* <code>private_filter()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Filters.md#private_filter)
* <code>group_filter()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Filters.md#group_filter)
* <code>media_filter()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Filters.md#media_filter)

----

<b> Remaining Functions </b><br>

* <code>broadcast_()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#broadcast_)
* <code>purge_()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#purge_)
* <code>srape()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#srape)
* <code>custom_welcome()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#custom_welcome)
* <code>makelist_()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#makelist_)
* <code>start_banall()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#start_banall)

----

<b> Watchers </b><br>
* <code>Red7_Watch()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#Red7_Watch) `Pyrogram`
* <code>Red7_Watch_telethon()</code> - For usage [click here.](https://github.com/RiZoeLX/pyRiZoeLX/blob/main/RiZoeLX/docs/Extra.md#Red7_Watch_telethon) `Telethon`
 

