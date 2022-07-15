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
    print(f'{client.user} has connected to Discord! ')
    for guild in client.guilds:
        print("connected to ", guild.name)
    refresh_price.start()

@tasks.loop(seconds=float(REFRESH_TIMER))
async def refresh_price():
    for guild in client.guilds:
        await guild.me.edit(activity=discord.Activity(type=discord.ActivityType.watching, name=f"CREO {status}% | LucyHarun"))
@tasks.loop(seconds=float(REFRESH_TIMER))
client.run(os.getenv("TOKEN"))
