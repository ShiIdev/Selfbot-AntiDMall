import discord
from discord.ext import commands
import re
import requests

print("""
  /$$$$$$              /$$     /$$         /$$$$$$$  /$$      /$$           /$$ /$$
 /$$__  $$            | $$    |__/        | $$__  $$| $$$    /$$$          | $$| $$
| $$  \ $$ /$$$$$$$  /$$$$$$   /$$        | $$  \ $$| $$$$  /$$$$  /$$$$$$ | $$| $$
| $$$$$$$$| $$__  $$|_  $$_/  | $$ /$$$$$$| $$  | $$| $$ $$/$$ $$ |____  $$| $$| $$
| $$__  $$| $$  \ $$  | $$    | $$|______/| $$  | $$| $$  $$$| $$  /$$$$$$$| $$| $$
| $$  | $$| $$  | $$  | $$ /$$| $$        | $$  | $$| $$\  $ | $$ /$$__  $$| $$| $$
| $$  | $$| $$  | $$  |  $$$$/| $$        | $$$$$$$/| $$ \/  | $$|  $$$$$$$| $$| $$
|__/  |__/|__/  |__/   \___/  |__/        |_______/ |__/     |__/ \_______/|__/|__/
                                                                               
                                                                               
                                                                                    
""")
token = input("Token: ")
prefix=";"
bot = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)

invite_pattern = re.compile(r"(discord\.gg/|discord\.com/invite/)")

@bot.event
async def on_ready():
    print("[+] Token connecté avec succès")
    print(f"Les publicités DMall seront désormais supprimées")

@bot.event
async def on_message(message):
    if message.guild is None and message.author.bot:
        if invite_pattern.search(message.content):
            delete_dm_channel(message.channel.id)

def delete_dm_channel(channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        print(f"[+] Le channel suivant a été supprimé avec succès: {channel_id}")
    else:
        print(f"[-] Le channel suivant n'a pas pu être supprimé {channel_id}: {response.status_code}")

bot.run(token, bot=False)