<h1> • pyRiZoeLX </h1>
<h2 align='center'> Module Name: Custom Filters </h2>

<h3><code>sudo_filter()</code></h3>
<b> Info: </b> <i> Defined Sudosers filter! </i> <br>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import sudo_filter 
from pyrogram import Client

Sudo_users = [1111111111, 1111111111]

@Client.on_message(sudo_filter(Sudo_users, "hi"))
async def Sudo_():
   print("Hey Sudoser")
```

<h3><code>me_filter()</code></h3>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import me_filter 
from pyrogram import Client

@Client.on_message(me_filter("hi"))
async def me_():
   print("Yes!")
```

<h3><code>private_filter()</code></h3>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import private_filter 
from pyrogram import Client

@Client.on_message(private_filter("hi"))
async def private_():
   print("Hello")
```

<h3><code>group_filter()</code></h3>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import group_filter 
from pyrogram import Client

@Client.on_message(group_filter("hi"))
async def group_():
   print("Hello")
```

<h3><code>media_filter()</code></h3>
<b> usage: </b> 

``` python 
from RiZoeLX.functions import media_filter 
from pyrogram import Client

@Client.on_message(media_filter())
async def media_():
   print("Triggered Media!")
```
