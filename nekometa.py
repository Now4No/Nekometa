import discord
from discord.ext import commands
import asyncio

INTERVAL = 0.000001

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
    embed.add_field(name="Invite",
                    value="[Invite link]https://discordapp.com/api/oauth2/authorize?client_id=556121131124523008&permissions=8&scope=bot()")
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
    if bot.user.id != message.author.id:
        if 'UwU' in message.content:
            if message.author.id == '411715164228812801':
                await bot.send_message(message.channel, 'hewo miuu:3')
            else:
                await bot.send_message(message.channel, 'OwO senpai:p')
        if 'oof' in message.content:
            await bot.send_message(message.channel, 'Oof^^')
        if 'OwO' in message.content:
            if message.author.id == '502521437496803359':
                await bot.send_message(message.channel, 'OwO master~')
            if message.author.id == '411715164228812801':
                await bot.send_message(message.channel, 'u.u miu^^')
        if 'Oof' in message.content:
            await bot.send_message(message.channel, 'Oof^^')
        if message.content.startswith('Gay'):
            await bot.send_message(message.channel, 'no u:p')
        if 'No u' in message.content:
            await bot.send_message(message.channel, 'no no u')
        if 'No no u' in message.content:
            await bot.send_message(message.channel, 'ugh nvm')
        if message.content.endswith('F'):
            await bot.send_message(message.channel, 'F')
        if 'nigger' in message.content:
            await bot.send_message(message.channel, 'N-word detected----_Alerting <@!502521437496803359>_')
        if 'Nigger' in message.content:
            await bot.send_message(message.channel, 'N-word detected----_Alerting <@!502521437496803359>_')
        if 'nigga' in message.content:
            await bot.send_message(message.channel, 'N-word detected----_Alerting <@!502521437496803359>_')
        if 'Nigga' in message.content:
            await bot.send_message(message.channel, 'N-word detected----_Alerting <@!502521437496803359>_')
        if 'ngl' in message.content:
            await bot.send_message(message.channel, 'N-word detected----_Alerting <@!502521437496803359>_')
        if 'Ngl' in message.content:
            await bot.send_message(message.channel, 'N-word detected----_Alerting <@!502521437496803359>_')
    await bot.process_commands(message)

bot.run('NTU2MTIxMTMxMTI0NTIzMDA4.D22SBg.1aHUkLAbjNUkF8F46OvkWUgMLoM')
