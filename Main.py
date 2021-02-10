# coding: utf-8
#!/usr/bin/env python

# Imports

import time, ipapi, os, discord, re, json, phonenumbers
from mojang import MojangAPI
from urllib.request import urlopen
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import CommandNotFound
import phonenumbers 
from phonenumbers import geocoder, carrier  


# Clear

def cls():
    os.system("cls")


cls()
os.system("title Ultra Discord Bot. - Logging...")

# Settings

with open("settings.json") as s:
    settings = json.load(s)

# ---------------------------------

token = settings.get("token")
prefix = settings.get("prefix")
version = settings.get("version")
presence = settings.get("presence")


Ultra = commands.Bot(command_prefix=prefix)


# ---------------------------------


# Commands

cls()
os.system(f"title Ultra Discord Bot -  Ready, Version {version}")
# Main

@Ultra.event
async def on_ready():
   await Ultra.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{presence}"))
   print(f"""
                                                    [ Prefix: {prefix}]
                                                    [ Version: {version}]
                                                    [ Username: {Ultra.user.name} ]
                                                    [ Presence: "{presence}"]
""")



# Error.

@Ultra.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title=f"**Command Not Found!**", description=f"Type {prefix}help For Command List.",color=discord.Color.red(), timestamp=ctx.message.created_at) 
            await ctx.send(embed=embed)


# MC Lookup


@Ultra.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def mclookup(ctx, *, message:str=None):
    uuid = MojangAPI.get_uuid(f"{message}")

    if not uuid:
        embed = discord.Embed(title="This player doesn't exist!", color=discord.Color.red())
        embed.set_author(name=f'Error!',)
        embed.set_footer(text=f"MC Lookup | Requested by {ctx.author} ")
        await ctx.send(embed=embed)
    else:
        profile = MojangAPI.get_profile(uuid)
        embed = discord.Embed(title=f"Profile Details", color=discord.Color.green())
        embed.add_field(name="UUID", value=uuid)
        embed.add_field(name="Skin URL", value=profile.skin_url)
        embed.add_field(name="NameMC Link", value="https://namemc.com/profile/" + uuid)
        embed.set_footer(text=f"MC Lookup | Requested by {ctx.author} ")
        await ctx.send(embed=embed)

# IP Lookup

@Ultra.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def iplookup(ctx, *, message:str=None):
    embed = discord.Embed(title=f"**{ip}** lookup!", description='',color=discord.Color.green(), timestamp=ctx.message.created_at) # Improved by ꜗꜗ#6507
    embed.add_field(name="ORG", value=f"{ip_info['org']}", inline=False)
    embed.add_field(name="ASN", value=f"{ip_info['asn']}", inline=False)
    embed.add_field(name="Region", value=f"{ip_info['region']}", inline=False)
    embed.add_field(name="Country", value=f"{ip_info['country_name']}", inline=False)
    embed.add_field(name="City", value=f"{ip_info['city']}", inline=False)
    embed.add_field(name="Timezone", value=f"{ip_info['timezone']}", inline=False)
    embed.add_field(name="Language", value=f"{ip_info['languages']}", inline=False)
    embed.add_field(name="Currency", value=f"{ip_info['currency']}", inline=False)
    embed.set_footer(text=f"IP Lookup | Requested by {ctx.author}")
    await ctx.send(embed=embed)


# Number Lookup

def number_scanner_region(phone_number):
    number = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(number,"es")
    data = description
    return data

def number_scanner_supplier(phone_number):
    number = phonenumbers.parse(phone_number)
    supplier = carrier.name_for_number(number,"es")
    data = supplier
    return data

@Ultra.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def numberlookup(ctx, *, message):
    embed = discord.Embed(title=f"**Number** Lookup!", description='',color=discord.Color.green(), timestamp=ctx.message.created_at) 
    embed.add_field(name="Phone Number", value=message, inline=False)
    embed.add_field(name="Region", value=number_scanner_region(message), inline=False) 
    embed.add_field(name="Company", value=number_scanner_supplier(message), inline=False)
    embed.set_footer(text=f"Number Lookup | Requested by {ctx.author}")
    await ctx.send(embed=embed)

# Ping.

@Ultra.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title=f"**Pong...**", description=f"{round(Ultra.latency * 1000)}ms",color=discord.Color.green(), timestamp=ctx.message.created_at) 
    await ctx.send(embed=embed)


if __name__ == "__main__":
    try:
        Ultra.run(token)
    except discord.errors.LoginFailure:
        os.system("title Ultra Discord Bot - Login Error...")
        print("Login Error, Press Any Key.")
        os.system('pause >NUL')
