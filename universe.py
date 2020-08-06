import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

client = commands.Bot(command_prefix = '+love', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()






@client.command(pass_context=True)
async def servercount(ctx):
    """Shows the total servers and users that Tarik is connected to."""
        
    embed=discord.Embed(colour=0xFF0000)
    embed.add_field(name="__Servers__", value="Tarik is connected to __**{}**__ servers.".format(len(client.guilds)))
    embed.add_field(name="__Users__", value="Tarik is connected to __**{}**__ users.".format(str(len(set(client.get_all_members())))))
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
async def dmall(ctx, *, message=None):
        #await ctx.message.delete()
           for a in client.guilds:
                for member in list(a.members):
                        try:
                             await member.send(message)
                             await ctx.send("> ** DM Sent To: **{}✅".format(member))
                        except:
                             print("can't")
                             await ctx.send("> ** DM Can't Sent To: **{}:x:".format(member))

        #else:
            #await ctx.author.send('**Correct usage:** `mass_dm <message>`')


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('--------')
    print('--------')
    print('Started ')
    print('Created by Users')
    
    
client.run("Njk4NDEwNzM5MDA1NjUzMDEz.XpFbsA.3lF-E0flSKKwkcy41WzRslQaJT8")                

