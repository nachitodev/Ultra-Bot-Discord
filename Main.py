import time, ipapi, os, discord, re, json, phonenumbers
from mojang import MojangAPI
from urllib.request import urlopen
from discord.ext import commands
import phonenumbers 
from phonenumbers import geocoder, carrier  

bot = commands.Bot(command_prefix='.')
os.system("cls")
os.system("title Ultra Discord Bot")
# MC Lookup


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def mclookup(ctx, *, message:str=None):
    uuid = MojangAPI.get_uuid(f"{message}")

    if not uuid:
        embed = discord.Embed(title="This player doesn't exist!", color=discord.Color.red())
        embed.set_author(name=f'Error!',)
        embed.set_footer(text=f"MC Lookup | Requested by {ctx.author} ")
        print(f"MC Lookup | Requested by {ctx.author} ")
        await ctx.send(embed=embed)
    else:
        profile = MojangAPI.get_profile(uuid)
        embed = discord.Embed(title=f"Profile Details", color=discord.Color.green())
        embed.add_field(name="UUID", value=uuid)
        embed.add_field(name="Skin URL", value=profile.skin_url)
        embed.add_field(name="NameMC Link", value="https://namemc.com/profile/" + uuid)
        embed.set_footer(text=f"MC Lookup | Requested by {ctx.author} ")
        print(f"MC Lookup | Requested by {ctx.author}")
        await ctx.send(embed=embed)

# IP Lookup

@bot.command()
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
    print(f"IP Lookup | Requested by {ctx.author} ")
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

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def numberlookup(ctx, *, message):
    embed = discord.Embed(title=f"**Number** Lookup!", description='',color=discord.Color.green(), timestamp=ctx.message.created_at) 
    embed.add_field(name="Phone Number", value=message, inline=False)
    embed.add_field(name="Region", value=number_scanner_region(message), inline=False) 
    embed.add_field(name="Company", value=number_scanner_supplier(message), inline=False)
    embed.set_footer(text=f"Number Lookup | Requested by {ctx.author}")
    print(f"Number Lookup | Requested by {ctx.author} ")
    await ctx.send(embed=embed)


bot.run("TOKEN-HERE")
