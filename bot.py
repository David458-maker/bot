import discord
from discord.ext import commands
 
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(command_prefix='#', intents=intents)
 
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def segregacja(ctx):
    await ctx.send(f'Rozdzielając odpady już na poziomie gospodarstwa domowego ograniczamy tony śmieci, które zanieczyszczają środowisko, a co za tym idzie – mamy wpływ na zmniejszenie zagrożenia dla życia i zdrowia ludzi i zwierząt.')

@bot.command()
async def papier(ctx):
    await ctx.send(f'Papierowe śmieci wyrzuć do niebieskiego kosza')

@bot.command()
async def metale(ctx):
    await ctx.send(f'Metalowe śmieci i tworzywa sztuczne wyrzuć do żółtego kosza')

@bot.command()
async def szkło(ctx):
    await ctx.send(f'Szklane śmieci wyrzuć do zielonego kosza')

@bot.command()
async def bio(ctx):
    await ctx.send(f'biodegradowalne śmieci wyrzuć do brązowego kosza')

@bot.command()
async def mieszane(ctx):
    await ctx.send(f'bodpady mieszane wyrzuć do czarnego kosza')

@bot.command()
async def ecomem(ctx):
    with open("images/mem1.jpg", 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
    # Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)


bot.run(")
