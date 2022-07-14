import os
import discord
import requests
import json

client = discord.Client()
def get_price():
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=creo-engine")
    json_data = json.loads(response.text)
    price = json_data[0]["price_change_percentage_24h"]
    return (price)
status = get_price()       
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    if get_price >= 0:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"CREO +{status}% | LucyHarun"))
    else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"CREO {status}% | LucyHarun"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content 
    if msg.startswith("!refresh"):
        refresh = get_price()
        if get_price >= 0:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"CREO +{refresh}% | LucyHarun"))
        else:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"CREO {refresh}% | LucyHarun"))
client.run(os.getenv("TOKEN"))
