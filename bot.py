import discord
import cv2
from discord.ext import commands

client = commands.Bot(command_prefix = "~")

@client.command()
async def meme(ctx, img, name):
    image = Image.open(img)
    cv2.putText(image, name,(10,500 offset), font, 1,(0,0,0),2)
    await channel.send(file=discord.File(image))


client.run(token)
