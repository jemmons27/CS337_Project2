# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "Recipes!"

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    print(message.content)

    if message.content == '99!':
        print("HI")
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run("MTMwOTI1OTExMDc5Mjk1MzkxNw.G_y_P-.ZOFqU-eQqXZzgZcDU_kHh8jr_db9L5xYI50--Y")