import discord
from discord.ext import commands
from discord.utils import get
import os

intents = discord.Intents.default()
intents.members = True  # Enable the members intent

Welcomer = commands.Bot(command_prefix='!', description='Welcomer Bot', intents=intents) 

@Welcomer.event
async def on_ready():
    print("Welcomer Bot is online!")

@Welcomer.event
async def on_member_join(member):
    channel = Welcomer.get_channel(1393266971105300651)  # Replace with your channel ID
    guild = member.guild
    member_count = guild.member_count
    member_count_string = str(member_count)
    if member_count_string[-2:] in ("11", "12", "13"):
        ord_index = "th"
    elif member_count_string.endswith("1"):
        ord_index = "st"
    elif member_count_string.endswith("2"):
        ord_index = "nd"
    elif member_count_string.endswith("3"):
        ord_index = "rd"
    else:
        ord_index = "th"
    member_count_text = f"{member_count}{ord_index}"
    role = get(member.guild.roles, name="Customers")  # Replace with your role name
    if role is not None:
        await member.add_roles(role)
    else:
        print("Role 'Customers' not found!")
    embed = discord.Embed(title="Welcome to the server!", description=f"Welcome to the Server {member.mention}! You are the {member_count_text} member 💎", color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    await channel.send(embed=embed) 

token = os.getenv("DISCORD_BOT_TOKEN")
if not token:
    raise ValueError("Bot token not found in environment variable DISCORD_BOT_TOKEN")
Welcomer.run(token)