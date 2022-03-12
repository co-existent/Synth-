100 lines of synths main code
updates about once a week




import discord
import json
import os
import random
from discord.ext import tasks
# imports things needed for bot (modules needed)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# bot token to activate bot

client = discord.Client()

Game = discord.Game

Streaming = discord.Streaming

idle = discord.Status.idle

dnd = discord.Status.dnd

random = random.choice
# turning a code into a shorter term

statuses = ''

@tasks.loop(seconds=120)
async def update_presence():
 statuses = f'Your Commands | {len(client.guilds)}, s!help', f'Your Mother | {len(client.guilds)}, s!help', f'Idiots Try And Code Complex Things | {len(client.guilds)}, s!help', f'Russia And Ukraine | {len(client.guilds)}, s!help', f'You | {len(client.guilds)}, s!help', f'discord.py tutorials | {len(client.guilds)}, s!help', f'{len(client.guilds)} Servers Use Me | s!help', f'Giving My Lonely Owner Some Company | {len(client.guilds)}, s!help'
 await client.change_presence(status=dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=random(statuses)))
# chooses a random status to cycle through every 2 minutes
@update_presence.before_loop
async def before_update_presence():
 await client.wait_until_ready()

update_presence.start()
# starts the loop
@client.event
async def on_ready():

 print('Connected to bot: {}'.format(client.user.name))
 print('Bot ID: {}'.format(client.user.id))
 print(f"Added In {len(client.guilds)} Servers")

 print('Bot ID: {}'.format(client.user.id))
 print('logged in as {0.user}'.format(client))
# prints stuff to terminal

@client.event
async def on_message(message):
  if message.author == client.user:
   return
  if message.content.startswith('s!help'):
   await message.channel.send(f'> {message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n {message.author.mention} \n **``(s!memory_im, pst, msg, statuses, status_loop) Shows Memories On Help With discrd.py``** \n **``(s!FAQ) Synths FAQ``** \n **``(s!flirt) Flirts Wit U,``** \n **``(s!join) Sends Support Server Link,``** \n **``(s!invite) Invite Link To Invite Bot,``** \n **``(s!code) Sends Code Status To Tell You What Is Happening To The Bot,``** \n **``(s!learn) Brings You To The Docs To Learn Some Things About Python/discord.py,``** \n **``(s!servers) Says How Many Servers The Bot Is In.``**')
  if message.author == client.user:
    return
  if message.content.startswith("hewwo"):
   await message.channel.send (random(["Hello!", "¡Hola! (Spanish)", "こんにちは！(Japanese)",  "你好！(Chinese)", "Witam! (Polish)", "Kamusta! (Filipino)", "Dia dhuit! (Irish)", "Ahoj! (Czech)", "Hallo! (German)", "Bonjour! (French)"]))
  if message.author == client.user:
    return
  if message.content.startswith('s!flirt'):
   await message.channel.send (random(["Sup Baby 😏", "Hey Shorty, Lets Take This Inside 😏", "If You Gotta Go Hunt, I Better Be The First You Hunt 😏", "I wish I was your mirror, so that I could look at you every morning 😏", "I really like our friendship, especially when we make out😏", "If I had a candy bar for every time I thought of you, I would be fat 😏"]))
  if message.author == client.user:
   return
  if message.content.startswith('s!invite'):
   await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n {message.author.mention} ``My Invite Link:`` **https://discord.com/api/oauth2/authorize?client_id=940163209011277874&permissions=8&scope=bot**")
  if message.author == client.user:
   return
  if message.content.startswith('s!join'):
    await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n {message.author.mention} ``Join My Main/Support Server:`` **https://discord.gg/XD5bP9t7Mk**")
  if message.author == client.user:
   return
  if message.content.startswith('s!code'):
    await message.channel.send(f"> {message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n {message.author.mention} ``Getting Coding Status...`` ``Code Replys With:`` *``Status Fixed! Now Working On Currency Commands And Website...``*")
  if message.author == client.user:
   return
  if message.content.startswith('s!learn'):
    await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n {message.author.mention} Learn Python Coding At:  http://discordpy.readthedocs.io/en/latest/")
  if message.author == client.user:
   return 
  if message.content.startswith('s!servers'):
    await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n In {len(client.guilds)} Servers")
  if message.author == client.user:
   return 
  if message.content.startswith('five night'): 
    msg = await message.channel.send('https://cdn.discordapp.com/attachments/939287435253268564/951688536321556510/Y2Mate.is_-_1902_Regina_Music_Box_Double_Comb_-_Vintage_Music_Bizet_The_Toreadors_Song_March-aLZun0gxXII-480p-1642431443735.mp4')
    cross = client.get_emoji(946483487014268940)
    await msg.add_reaction(cross)
  if message.author == client.user:
   return 
  if message.content.startswith('s!FAQ'):
    await message.channel.send(f'{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n 1. "Where Are The Currency Commands?" Answer: "They Are Coming Soon :)" 2. "Why Does The Bot Go Down So Much?" Answer: "Im Just Testing Out Features With The Bot And If You Have Any Questions Just DM Me"')
  if message.author == client.user:
   return 
  if message.content.startswith('s!memory_im'):
    await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n Importing: When You Import Something Like When You Start Discord.py You ```Import discord``` But Before That You Would Do ``pip3 install discord`` To Install Discord Module, Here Are The Imports Used For Synths Activation And Stuff: https://cdn.discordapp.com/attachments/940378610093662218/949947940766646282/unknown.png")
  if message.author == client.user:
   return 
  if message.content.startswith('s!memory_pst'):
    await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n Pasting Stuff Into The Terminal: How Do You Print? Easy All You Do Is ``print('your_message_here')`` Its Very Easy, Here Is Some Examples Of What You Can Do And How It Will Come Out: **Ex Of The Print** https://cdn.discordapp.com/attachments/940378610093662218/949949542814588929/unknown.png **And How It Will Come Out** https://cdn.discordapp.com/attachments/940378610093662218/949949689954967582/unknown.png")
  if message.author == client.user:
   return 
  if message.content.startswith('s!memory_msg'):
    await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n Making A Bot Send Messages In The Channel: There Is Two Ways, First Is To Have The Bot Say Something When It Joins, And Making A Bot Reply With Something When You Say, For Example. Joe, If U Want To Make It Reply To It For It To Say Another Word With No Ping, You Do This: ")
  if message.author == client.user:
   return 
  if message.content.startswith('s!github'): 
    msg = await message.channel.send(f"{message.author.mention} 📧**NEWS: s!news For New Info (this message will go away in a week)**📧 \n https://github.com/pianoidoll/Synth-/find/main")
    cross = client.get_emoji(763440516066574338)
    await msg.add_reaction(cross)
  if message.author == client.user:
   return 
  if message.content.startswith('s!news'): 
    await message.channel.send("Github Is Here! `s!github`")
  if message.author == client:
   return
  if message.content.startswith('dubstep'):
    await message.channel.send("https://tenor.com/view/i-love-dubstep-dubstep-gif-23900396")
  if message.author == client:
   return
  if message.content.startswith('s!website'):
    embed=discord.Embed(title="Click Here For Inviting Synth Instructions", url="https://discord.com/api/oauth2/authorize?client_id=940163209011277874&permissions=8&scope=bot", color=0x00ffbf)
    embed.set_author(name="Click For Synths Website!!!", url="https://discord.gg/XD5bP9t7Mk", icon_url="https://i.pinimg.com/originals/69/01/c4/6901c471e753e912776c0d4c558aed6a.gif")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXdxJsEDY_S2341r2bwImXYleLdsvCLT8UyTWghcDa70zm30Vr_NAaHhVmcnyX2N1386Y&usqp=CAU")
    embed.add_field(name="Thanks For Synths Support!", value="Have A Great Day!!", inline=True)
    embed.set_footer(text="Bot, Servers, And Coding All Done By: Terrence#6960")
    await message.channel.send(embed=embed)
# message sending
@client.event
async def on_member_join(member):
 await member.send('New Message')


@client.event
async def on_guild_join(guild):

 for channel in guild.text_channels:
  if channel.permissions_for(guild.me).send_messages:
    await channel.send('Hey there! Im A Bot That Has Features With Music And Coding, s!help For more, A Bot With Upcoming Features, DM My Owner For Questions! **Prefix: s!**')
  break
# sends message when joined new server/guild

client.run(DISCORD_TOKEN)
# runs the bot token


