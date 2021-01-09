import time
from mojang import MojangAPI
import time
import os
import discord
import re
import json
from urllib.request import urlopen
from discord.ext import commands

bot = commands.Bot(command_prefix='.', self_bot=True)
os.system("cls")
os.system("title BOT")
# MC Lookup


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def mclookup(ctx, *, message:str=None):
    uuid = MojangAPI.get_uuid(f"{message}")

    if not uuid:
        embed = discord.Embed(title="This player doesn't exist!", color=discord.Color.red())
        embed.set_author(name=f'Error!',)
        embed.set_footer(text=f"MC Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
        print(f"MC Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
        await ctx.send(embed=embed)
    else:
        profile = MojangAPI.get_profile(uuid)
        embed = discord.Embed(title=f"Profile Details", color=discord.Color.green())
        embed.add_field(name="UUID", value=uuid)
        embed.add_field(name="Skin URL", value=profile.skin_url)
        embed.add_field(name="NameMC Link", value="https://es.namemc.com/profile/" + uuid)
        embed.set_footer(text=f"MC Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
        print(f"MC Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
        await ctx.send(embed=embed)

# IP Lookup

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def iplookup(ctx, *, message:str=None):
	url = f'http://ipinfo.io/{message}/json'
	response = urlopen(url)
	data = json.load(response)
	IP=data['ip']
	Org=data['org']
	City = data['city']
	Country=data['country']
	Region=data['region']

	if not IP:
	    embed = discord.Embed(title="This IP doesn't exist!", color=discord.Color.red())
	    embed.set_author(name='Error!',)
	    embed.set_footer(text=f"IP Lookup | Requested by {ctx.author}")
	    print(f"IP Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
	    await ctx.send(embed=embed)
	else:
	    embed = discord.Embed(title=f"IP Details", color=discord.Color.green())
	    embed.add_field(name="IP", value=IP)
	    embed.add_field(name="Country", value=Country)
	    embed.add_field(name="City", value=City)
	    embed.add_field(name="Region", value=Region)
	    embed.add_field(name="Org", value=Org)
	    embed.set_footer(text=f"IP Lookup | Requested by {ctx.author}")
	    print(f"IP Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
	    await ctx.send(embed=embed)

bot.run("your token here", bot=False)