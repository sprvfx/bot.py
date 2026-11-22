import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

bot = event
async def on_message_edit ( before , after ):
    kanal = after.channel
    await kanal.send("Wiadomość została edytowana!")
    await kanal.send("Stara wiadomość: " + before.content)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


bot.run("token")
