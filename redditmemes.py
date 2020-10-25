import requests
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$', activity = discord.Game("Starting Bot"), status='online')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot Ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Memes"))

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

@client.command()
async def meme(ctx, subreddit):
    if (subreddit == None):
        subreddit = 'programmerhumor'
    redditMemeJSONReseponse = requests.get(
        url=f'https://www.reddit.com/r/{subreddit}/new.json', 
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