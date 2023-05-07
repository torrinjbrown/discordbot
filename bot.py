import discord
import os 
import requests
import json

#
client = discord.Client(intents=discord.Intents.default()) # Connects to the dicord client

# Creating function for getting quotes
def get_quote():
    response = response.get('https://api.breakingbadquotes.xyz/v1/quotes')
    json_data = json.loads(response.text)
    quote = json_data[0]
    print(quote)


@client.event #Setting up the client event for the bot
async def on_ready(): 
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

token = "MTEwMzc1MDg2NDcwOTEwMzc4Nw.GhIbnZ.zIo_0jvDPq3070wvtzfDQRlFS3hPgFx9Dq-XcA"
client.run(token=token)
