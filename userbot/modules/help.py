# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """For .help command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please specify a valid module name.")
    else:
        head = "**Help for** [UserButt](https://github.com/keselekpermen69/userbutt)"
        head2 = "For more information to use command,"
        head3 = "send `.help <module name>`"
        head4 = "List for all available command below: "
        string = ""
        sep1 = "••••••••••••••••••••••••••••••••••••••••••••••"
        sep2 = "========================================="
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t\t\t||\t\t\t "
        await event.edit("Specify which module do you want help for !!\
                        \n**Usage:** `.help` <module name>\n\n"
                        f"{string}")
