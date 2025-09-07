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
    channel = Welcomer.get_channel(1399365756294004829)  # Replace with your channel ID
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
    embed = discord.Embed(title="Welcome to the server!", description=f"Welcome to Sapphire Manor {member.mention}! You are the {member_count_text} member 💎", color=discord.Color.blue())
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
    embed.set_thumbnail(url=avatar_url)
    await channel.send(embed=embed) 

# Choose Booking Type

class Bookings(discord.ui.View):
    def __init__(self):
        super().__init__()
        link_button = discord.ui.Button(label="Wedding", style=discord.ButtonStyle.link, url="https://forms.gle/FW1ajVXBwqibgLpp7")
        self.add_item(link_button)

    @discord.ui.button(label="Room", style=discord.ButtonStyle.blurple)
    async def room_booking(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Roomtype()
        await interaction.response.send_message("Please select a roomtype:", view=view, ephemeral=True) # Select a roomtype

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def Cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()

# Choose Room Option

class Roomtype(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Standard", style=discord.ButtonStyle.primary)
    async def Standard(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global roomtype
        roomtype = "a Standard room"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

    @discord.ui.button(label="Family", style=discord.ButtonStyle.primary)
    async def Family(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global roomtype
        roomtype = "a Family suite"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

    @discord.ui.button(label="Luxury", style=discord.ButtonStyle.primary)
    async def Luxury(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global roomtype
        roomtype = "a Luxury suite"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

    @discord.ui.button(label="Diamond", style=discord.ButtonStyle.primary)
    async def Diamond(self, interaction: discord.Interaction, button: discord.ui.Button):
        view = Date()
        global roomtype
        roomtype = "the Diamond Suite"
        await interaction.response.send_message("Please select a date:", view=view, ephemeral=True) # Select a date

# Choose Booking Date

class Date(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label=f"{today}", style=discord.ButtonStyle.primary)
    async def today_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has booked {roomtype} for {today}!")

    @discord.ui.button(label=f"{tomorrow}", style=discord.ButtonStyle.primary)
    async def tomorrow_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has booked {roomtype} for {tomorrow}!")

    @discord.ui.button(label=f"{dayafter1}", style=discord.ButtonStyle.primary)
    async def dayafter1_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has booked {roomtype} for {dayafter1}!")

    @discord.ui.button(label=f"{dayafter2}", style=discord.ButtonStyle.primary)
    async def dayafter2_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        member = interaction.user
        await interaction.response.send_message(f"{member} has booked {roomtype} for {dayafter2}!")
        
@Welcomer.command()
async def book(ctx):
    view = Bookings()
    await ctx.send("Please select a type of booking!", view=view, delete_after=45) 

# Ticket System

class Ticket_buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        ticket_link = discord.ui.Button(label="Wedding Form", style=discord.ButtonStyle.link, url="https://forms.gle/FW1ajVXBwqibgLpp7") # Replace with your desired URL
        self.add_item(ticket_link)

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red)
    async def Delete(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.delete()

@Welcomer.command()
async def ticket(ctx):
    
    staff_role = discord.utils.get(ctx.guild.roles, name="Ticket-Viewer")  # Replace with your ticket support role name

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ctx.author: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
    }
    if staff_role:
        overwrites[staff_role] = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)

    channel_name = f"{ctx.author.name}'s-ticket"
    create_channel = await ctx.guild.create_text_channel(
        name=channel_name,
        overwrites=overwrites,
        reason="Ticket created"
    )
    
    await create_channel.send(f"{ctx.author.name} has created a ticket! Access it in the channel menu.")

    view = Ticket_buttons()
    await create_channel.send("Use the buttons below to manage your ticket.", view=view)

# Run the bot

token = os.getenv("DISCORD_BOT_TOKEN")
if not token:
    raise ValueError("Bot token not found in .env file: 'DISCORD_BOT_TOKEN'. Please set it before running the bot.")

if __name__ == "__main__":
    Welcomer.run(token)