import os
import discord
import requests
import json

client = discord.Client()
def get_pricechange():
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=creo-engine")
    json_data = json.loads(response.text)
    pricechange = json_data[0]["price_change_24h"]
    return (pricechange)
 status = pricechange()
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"${status}"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith("!pricechange"):
        pricechange = get_pricechange()
        await message.channel.send(f"**CREO Price Change 24h**: ${pricechange}")  
    if msg.startswith("!refresh"):
        refresh = get_pricechange()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"${refresh}"))
client.run(os.getenv("TOKEN"))
