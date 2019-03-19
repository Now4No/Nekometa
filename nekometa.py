import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----//-----')

@bot.command()
async def greet(ctx):
    await ctx.send("Hewwooo^^")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Nekometa", description="Dank bot created coz why not", color=0xeee657)
# give info
    embed.add_field(name="Author", value=">Sprite-Kun")
# Shows the number of servers Nekometa is member of
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
# give users a link to invite
    embed.add_field(name="Invite", value="[Invite link]https://discordapp.com/api/oauth2/authorize?client_id=556121131124523008&permissions=8&scope=bot()")
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Nekometa", description="List of available commands:", color=0xeee657)
    embed.add_field(name="&greet", value="noice greet msg", inline=False)
    embed.add_field(name="&info", value="so yk me better:%", inline=False)
    embed.add_field(name="&help", value="Gives this msg", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if 'UwU' in message.content:
        await message.channel.send('u have de big gae ^^')
    if 'oof' in message.content:
        await message.channel.send('Oof^^')
    if 'OwO' in message.content:
        if message.author.id == 411715164228812801:
            await message.channel.send('u.u miu^^')
        else:
            await message.channel.send('u.u normies')
    if 'Oof' in message.content:
        await message.channel.send('Oopsie')
    if 'gay' in message.content:
        await message.channel.send(message.author.id, 'you too:p')
    await bot.process_commands(message)

bot.run('NTU2MTIxMTMxMTI0NTIzMDA4.D22SBg.1aHUkLAbjNUkF8F46OvkWUgMLoM')
