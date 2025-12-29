import discord
import time
import asyncio



from discord.ext import commands



from discord.utils import get





intents = discord.Intents.all()



bot = commands.Bot(".", intents=intents)




@bot.command()
async def pat(ctx):
    PROP = [PROPAGANDAS
    ]  # propagandas
    MIN = [MINUTOS] # seconds
    channel = bot.get_channel(ID_DO_CANAL)
    if channel is None:
        print("Channel not found.")
        return  # Exit the function if the channel is not found
    last_message = None
    i = 0
    oi = 0
    for prop in range(len(PROP)):
        while i < len(PROP):
            message = await channel.send(PROP[i])

            if i == 2:
                i = 0
            else:
                i += 1
            if last_message:
                await last_message.delete()
            for min in range(len(MIN)):
                while oi < len(MIN):
                    await asyncio.sleep(MIN[min] * 60)  # Convert seconds to minutes
                    if oi == 2:
                        oi = 0
                    else:
                        oi += 1
            
            last_message = message
        last_message = message


    if last_message:
        await last_message.delete()

