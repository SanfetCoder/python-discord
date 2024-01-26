import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from PIL import Image, ImageOps
from io import BytesIO
from helper.image import compress_image
from rembg import remove

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
    
  if message.attachments:
      # Check if the message has image attachments
      for attachment in message.attachments:
        if attachment.content_type.startswith('image'):
          if message.content.startswith('$remove'):
              # Download the file
              await attachment.save('downloaded_image.png')
              
              # Send the file back as a message
              with open('downloaded_image.png', 'rb') as f:
                # Processing the image 
                input = Image.open(f) 
                  
                # Removing the background from the given Image 
                output = remove(input) 
                  
                #Saving the image in the given path 
                output.save("/Users/sanphetlovestina/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Development/python-discord/remove-imaged.png") 
                
                with open('remove-imaged.png', 'rb') as r:
                  await message.channel.send(file=discord.File(r))
          elif message.content.startswith("$compress"):
              # Download the file
              await attachment.save('downloaded_image.png')
              
              # Send the file back as a message
              with open('downloaded_image.png', 'rb') as f:
                try:
                  input_path = "/Users/sanphetlovestina/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Development/python-discord/downloaded_image.png"
                  output_path = "/Users/sanphetlovestina/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Development/python-discord/compressed-image.png"
                  compress_image(input_path, output_path)
                  
                  with open ('compressed_image.jpeg', 'rb') as c:
                    await message.channel.send(file=discord.File(c))
                except Exception as e:
                  error = str(e)
                  if (error == "cannot write mode RGBA as JPEG"):
                    error = "We can't convert image with transparency to JPEG file"
                  await message.channel.send(error)
              
          
      
    
@bot.command(name='smart')
async def smartest_guy(ctx):
  await ctx.send('Yang!')


client.run(os.environ["DISCORD_TOKEN"])