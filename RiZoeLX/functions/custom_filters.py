""" RiZoeLX 2022 © pyRiZoeLX """

from pyrogram import filters

def sudo_filter(Sudos, cmd):
   return filters.user(Sudos) & filters.command(cmd)
