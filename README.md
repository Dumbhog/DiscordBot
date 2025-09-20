# Welcome to BookerBot

This is a simple bot I created for my own Roblox Discord server, and my submission for the hackclub event *Converge*. The server is for a hotel so that's why it allows users to book rooms.

## Features
The bot in its current state mainly accomplishes 2 features:
> 1. creates a custom welcome message for any member that joins the server and declares wether they are the 2nd/3rd member, etc.
> 2. Allows them to use Discord UI buttons to select wether to either 1. Go to a given website 2. proceed to select a date ("booking") or 3. Cancel their interaction
> 3. Users can create temporary channels (tickets) to message moderators concering any issues they may have, from there the user can click a button and the channel will be deleted.

## How to use the bot:

If you would like to use the booking features of **my bot** for your own server , just use the following link to invite the bot to it: https://discord.com/oauth2/authorize?client_id=1413854070564978749&permissions=3088&integration_type=0&scope=bot. Bear in mind that you will have to create a role called *ticket-viewer* and give it to the bot in order for for ticket feature to work succesfully. Additionally you will have to edit the code and change the **channel ID** on <ins> line 19 </ins> for the welcome message to work.