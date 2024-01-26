import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$who is the smartest guy in the world'):
    await message.channel.send('Yang!')
  elif message.attachments:
    # Check if the message has image attachments
    for attachment in message.attachments:
      if attachment.content_type.startswith('image'):
        # Download the file
        saved_file = await attachment.save('downloaded_image.png')
        
        # Send the file back as a message
        with open('downloaded_image.png', 'rb') as f:
          await message.channel.send(file=discord.File(f))
          
        await message.channel.send(f'Thanks for the image, {message.author.name}!')
      else:
        await message.channel.send('Please upload a valid image.')
    
@bot.command(name='smart')
async def smartest_guy(ctx):
  await ctx.send('Yang!')


client.run(os.environ["DISCORD_TOKEN"])
