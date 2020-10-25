# Base for discord.py
import discord
from discord.ext import commands

# Database
import pymongo
from pymongo import MongoClient

# We might need these
import requests
import random
import time
import os
import sys

# Draw onto image
from cv2 import cv2
import PIL
from PIL import ImageFont, Image, ImageDraw


client = commands.Bot(command_prefix = ';', activity = discord.Game("Starting Bot"), status='online')
client.remove_command('help')

# Need key and can access database from there
cluster = MongoClient(key)
db = cluster["ubh"]
ubh = db["ubh1"]

# Custom function to get database items in a list
def db_get(db, k1, k2, item):
    ls = []
    lx = db.find({k1:k2})
    for b in lx:
        ls.append(b[item])
    return ls

# Simple on 
@client.event
async def on_ready():
    print('Bot Ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="Yes", url='Somethinghere'))


# Example of text onto image
@client.command()
async def spic(ctx, *args):
    img = np.zeros((150, 1024, 3), np.uint8)
    img[:] = 0, 0, 0
    cv2.putText(img, " ".join(args[0:50]), (0, 100), cv2.FONT_HERSHEY_SIMPLEX,4,(256,150,0), 3)
    cv2.imwrite('send1.png', img)
    f = discord.File("send1.png", filename="send1.png")
    await ctx.send(file=f)
    os.remove('send1.png')
    await ctx.message.delete()

# Format for meme generation
# args[0] == command
# args[1] == meme name
# args[2] == meme url
# args[3:30] == meme content, seperated by | for top/bottom


@client.command()
async def meme(ctx, *args):
	m = args[0]

	if m == 'add':
		if args[1]:
			# stuff
			# 2nd args for name of meme
			pass # adds image (link) to db
	elif m == 'remove':
		if args[1]:
			# stuff
			pass
	elif m == ''

@client.command()
async def pmeme(ctx):
    redditMemeJSONReseponse = requests.get(
        url='https://www.reddit.com/r/programmerhumor/new.json', 
        headers={'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari'}
        )

    memeResponseData = [ ]

    for post in redditMemeJSONReseponse.json()['data']['children']:
        author = post['data']['author']
        title = post['data']['title']
        imageurl = post['data']['url']
        if '.png' in imageurl or '.gif' in imageurl or '.jpg' in imageurl or '.jpeg' in imageurl:
            memeResponseData.append([author, title, imageurl])

    randomMeme = random.choice(memeResponseData)

    embed=discord.Embed(title=randomMeme[1], description=f'u/{randomMeme[0]}', color=0x0C0CCC).set_image(url=randomMeme[2])
    await ctx.channel.send(embed=embed)

client.run(token)