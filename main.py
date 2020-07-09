import discord, asyncio
from discord.ext import commands

token = 'Your Bots Token Here'

client = commands.Bot(command_prefix = '++')
client.remove_command('help')

async def status():
    while True:
        watch = discord.Activity(type = discord.ActivityType.watching, name = 'Made By Dropout <3')
        await client.change_presence(activity = watch)
        await asyncio.sleep(10800)
        
@client.event
async def on_ready():
    print('Online')
    status()
   

@client.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
            await ctx.send(f'Sent "{message}" To {user}')
        except:
            pass

    
client.run(token, bot = True)
