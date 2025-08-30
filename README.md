# Welcome to BookerBot

This is a simple bot I created for my own Roblox Discod server, and my submission for the hackclub event *Converge*, it is currently in early development so that's why it lacks many features.

## Features
The bot in its current state mainly accomplishes 2 features:
> 1. creates a custom welcome message for any member that joins the server and declares wether they are the 2nd/3rd member, etc.
> 2. Allows them to use Discord UI buttons to select wether to either 1. Go to a given website 2. proceed to select a date ("booking") or 3. Cancel their interaction

## How to use the bot:

If you would like to use the booking features of **my bot** for your own server (no change to code), just use the following link to invite the bot to it: https://discord.com/oauth2/authorize?client_id=1392842869634764902&permissions=268438528&integration_type=0&scope=bot,

**It is worth mentioning that the code for the *welcome message/rolegiving* I have made channel-specific to suit my needs.** Therefore, if you would like to use those features of the bot for yourself, you will have to use this code to **create your own bot** via the *Discord Developer Portal*. Just make sure you change the <ins> channel ID </ins> and the <ins> role you would like to give </ins> in Booker+Welcomer.py. Additionally, make sure you put your own bot's token in a .env file
