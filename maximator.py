import re

import discord

import config
from jsonSentencesHandler import *

client = discord.Client()


@client.event
async def on_message(message):
    # the bot don't reply to itself
    if message.author == client.user:
        return

    channel = message.channel

    try:

        # feur
        feur = re.search(".*quoi[^A-Za-z0-9]*$", message.content, re.IGNORECASE | re.X)

        if feur is not None:
            msg = get_random_feur()

            await channel.send(msg)

        if message.content.startswith("!mhelp"):
            msg = "T'a cru j'avais des commandes ? Et toc !"

            await channel.send(msg)

        if message.content.startswith("!mgit"):
            await channel.send("https://github.com/Kwaaac/Bot-Maximator")



    except Exception as e:
        print("aie y'a eu une bille: \n", e)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.TOKEN)
