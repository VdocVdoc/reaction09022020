import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil
import sqlite3
from os import system
import random
import json
import asyncio
import urllib.parse, urllib.request, re
import praw
import requests, json 
import weather_forecast as wf
import time;
import datetime
from datetime import date
from datetime import datetime
import requests
import pytz
import asyncio

TOKEN = 'YOUR TOKEN'
get_prefix = '.'

bot = commands.Bot(command_prefix=get_prefix , case_insensitive=True)


"""@bot.event
async def on_raw_reaction_add(payload):
    
"""
'''

@bot.command()
async def cool(ctx):
    user = ctx.author
    embed = discord.Embed(
            colour=0xF300FF)
    embed.set_author(name="Work Tracking")
    embed.add_field(name="Stuff", value="If you react with :space_invader: you are cool", inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji="☣️")
    def check(reaction, user):
        user == ctx.author and reaction.emoji == "emoji_name"
        return
    await bot.wait_for("reaction_add", check=check)
    reaction, user = await bot.wait_for("reaction_add", check=check)
    if check == True:
        await ctx.send(f"{ctx.author} is op")
        
        '''
 
"""
@bot.command()
async def cool(ctx):
    embed = discord.Embed(
            colour=0xF300FF)
    embed.set_author(name="Work Tracking")
    embed.add_field(name="Stuff", value="If you react with :space_invader: you are cool", inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji="☣️")
    def check(reaction, user):
        user == ctx.author and  str(reaction.emoji) == "emoji_name"
        return 
    try:
        reaction, user = await bot.wait_for('reaction_add', check=check)
    except TimeoutError:
        await bot_message.clear_reactions()
        return
    else:
        await ctx.send(f"{ctx.author} is op")
"""


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='.help'))
    print("Logged in as: " + bot.user.name + "\n-------------------")


@bot.command()
async def cool(ctx):
    embed = discord.Embed(
            colour=0xF300FF)
    embed.set_author(name="Work Tracking")
    embed.add_field(name="Stuff", value="If you react with :space_invader: you are cool", inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(emoji="☣️")
    
@bot.event
async def on_reaction_add(reaction , user):
    channel = bot.get_channel("738092136423227506")
    if reaction.emoji == "☣️":
        await bot.send_message(channel, "Hello")







'''
@bot.command()
@commands.command()
async def test(self, ctx):
    author = ctx.author
    message = await ctx.send('test')

    emote = '☣️'

    for e in emote:
        await message.add_reaction(e)

    def check(reaction, user):
        return (reaction.message.id == message.id) and (user.id == ctx.author.id) and (str(reaction) in emote)

    try:
        reaction, user = await self.client.wait_for('reaction_add', check=check, timeout=60)
    except asyncio.TimeoutError:
        await ctx.send("Timed out")
        return
    if str(reaction) == '☣️':
        await ctx.send('some stuff')


'''


    

'''
@bot.command(pass_context=True)
async def jacky(ctx):
    colours = random.choice([0xF300FF , 0x00FF16 , 0x001AFF , 0xFF0017 , 0x333333])
    embed = discord.Embed(
            colour=colours)
    url = ["https://cdn.discordapp.com/attachments/732703828423606292/750817306212303018/image0.png" , "https://cdn.discordapp.com/attachments/732703828423606292/750817376739655731/image0.png" , "https://cdn.discordapp.com/attachments/732703828423606292/750817494478094436/image0.png"]
    embed.set_author(name="Jacky, for you sir")
    embed.set_image(url=f"{random.choice(url)}")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def frezzy(ctx):
    colours = random.choice([0xF300FF , 0x00FF16 , 0x001AFF , 0xFF0017 , 0x333333])
    embed = discord.Embed(
            colour=colours)
    url = ["https://cdn.discordapp.com/attachments/736638821743198238/750470489608159344/image0.png" , "https://cdn.discordapp.com/attachments/732703828423606292/750819134736171028/image0.png"]
    embed.set_author(name="Frezzy, here ya go")
    embed.set_image(url=f"{random.choice(url)}")
    await ctx.send(embed=embed)

'''
bot.run(TOKEN)
