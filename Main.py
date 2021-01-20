import time, ipapi, os, discord, re, json
from mojang import MojangAPI
from urllib.request import urlopen
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
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
        embed.add_field(name="NameMC Link", value="https://namemc.com/profile/" + uuid)
        embed.set_footer(text=f"MC Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
        print(f"MC Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
        await ctx.send(embed=embed)

# IP Lookup

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def iplookup(ctx, *, message:str=None):
    embed = discord.Embed(title=f"**{ip}** lookup!", description='',color=0xbf00ff, timestamp=ctx.message.created_at) # Improved by ꜗꜗ#6507
    embed.add_field(name="ORG", value=f"{ip_info['org']}", inline=False)
    embed.add_field(name="ASN", value=f"{ip_info['asn']}", inline=False)
    embed.add_field(name="Region", value=f"{ip_info['region']}", inline=False)
    embed.add_field(name="Country", value=f"{ip_info['country_name']}", inline=False)
    embed.add_field(name="City", value=f"{ip_info['city']}", inline=False)
    embed.add_field(name="Timezone", value=f"{ip_info['timezone']}", inline=False)
    embed.add_field(name="Language", value=f"{ip_info['languages']}", inline=False)
    embed.add_field(name="Currency", value=f"{ip_info['currency']}", inline=False)
    embed.set_footer(text=f"IP Lookup | Requested by {ctx.author}")
    print(f"IP Lookup | Requested by {ctx.author} | BOT By Junai#0001 🔧")
    await ctx.send(embed=embed)

bot.run("TOKEN-HERE")
else
bot.run("TOKEN-HERE", bot=False)
