import discord
from discord.ext import commands
from discord.utils import get
import os
from CalendarTest import today, tomorrow, dayafter1, dayafter2

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True 

Welcomer = commands.Bot(command_prefix='!', description='Welcomer Bot', intents=intents) 

@Welcomer.event
async def on_ready():
    print("Welcomer Bot is online!")

@Welcomer.event
async def on_member_join(member):
    channel = Welcomer.get_channel(12345679)  # Replace with your channel ID
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
    role = get(member.guild.roles, name="BookerRole")  # Replace with your role name
    if role is not None:
        await member.add_roles(role)
    else:
        print("Role 'BookerRole' not found!") # Also replace with your role name
    embed = discord.Embed(title="Welcome to the server!", description=f"Welcome to the Server {member.mention}! You are the {member_count_text} member 💎", color=discord.Color.blue())
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed.set_thumbnail(url=avatar_url)
    await channel.send(embed=embed) 


class Bookings(discord.ui.View):
    def __init__(self):
        super().__init__()
        link_button = discord.ui.Button(label="Option2", style=discord.ButtonStyle.link, url="https://github.com/Dumbhog") # Replace with your desired URL
        self.add_item(link_button)

    @discord.ui.button(label="Option1", style=discord.ButtonStyle.blurple)
    async def Option1(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Booktype()
        await interaction.response.send_message("Please select an option:", view=view, ephemeral=True) # Select an option

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def Cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()

class Booktype(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Type 1", style=discord.ButtonStyle.primary)
    async def Type1(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global booktype
        booktype = "Type 1"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

    @discord.ui.button(label="Type 2", style=discord.ButtonStyle.primary)
    async def Type2(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global booktype
        booktype = "Type 2"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

    @discord.ui.button(label="Type 3", style=discord.ButtonStyle.primary)
    async def Type3(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global booktype
        booktype = "Type 3"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

    @discord.ui.button(label="Type 4", style=discord.ButtonStyle.primary)
    async def Type4(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global booktype
        booktype = "Type 4"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

class Date(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label=f"{today}", style=discord.ButtonStyle.primary)
    async def today_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has made a {booktype} booking for {today}!")

    @discord.ui.button(label=f"{tomorrow}", style=discord.ButtonStyle.primary)
    async def tomorrow_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has made a {booktype} booking for {tomorrow}!")

    @discord.ui.button(label=f"{dayafter1}", style=discord.ButtonStyle.primary)
    async def dayafter1_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has made a {booktype} booking for {dayafter1}!")

    @discord.ui.button(label=f"{dayafter2}", style=discord.ButtonStyle.primary)
    async def dayafter2_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has made a {booktype} booking for {dayafter2}!")
        
@Welcomer.command()
async def button_test(ctx):
    view = Bookings()
    await ctx.send("Please select a type of booking!", view=view, delete_after=45) 

token = os.getenv("DISCORD_BOT_TOKEN")
if not token:
    raise ValueError("Bot token not found in environment variable DISCORD_BOT_TOKEN. Please set it before running the bot.")

if __name__ == "__main__":
    Welcomer.run(token)