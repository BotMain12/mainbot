import discord
import json
import youtube_dl
from discord.ext import commands
import asyncio
import os
import itertools
import random
import requests
import bs4
authorized_users = [
    "271987926026420224"
    "303917352964194305"
]

client = commands.Bot(command_prefix = 'b!')
client.remove_command('help')
client.remove_command('b!joke')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='b!help | 211 Servers.'), status=discord.Status('dnd'), afk=False)
    await asyncio.sleep(5)
    print('Logged in...')
    print('Username: ' + str(client.user.name))
    print('Client ID: ' + str(client.user.id))
    print('Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + client.user.id + '&scope=bot&permissions=0')

@client.event
async def on_member_join(member):
    welcome_embed_description = "Welcome to *Bastion!*, {}!  We hope you enjoy your time here!".format(member.mention)
    embed = discord.Embed(title="New Member", description=welcome_embed_description, color=0x149900)
    embed.set_footer(text="New Member Count: " + str(len(member.server.members)))
    channel = discord.utils.get(member.server.channels, name="welcome-goodbye")
    await client.send_message(channel, embed=embed)
    role = discord.utils.get(member.server.roles, name="Member")
    await client.add_roles(member, role)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        client.say("An error occured while performing the command! Error: 301")

@client.event
async def on_member_remove(member):
    welcome_embed_description = "{} just left. :cry:".format(member.mention)
    embed = discord.Embed(title="Member Left", description=welcome_embed_description, color=0x990000)
    embed.set_footer(text="New Member Count: " + str(len(member.server.members)))
    channel = discord.utils.get(member.server.channels, name="welcome-goodbye")
    await client.send_message(channel, embed=embed)

@client.event
async def on_message(message):
    if ('cock') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('penis') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('vagina') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('motherfucker') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fucker') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('tits') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('fucking') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('anal') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('porn') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if ('pussy') in message.content:
       await client.send_message(message.channel,'**Hey!** You are not allowed to say that!')
       await client.delete_message(message)
    if message.content == 'b!ping':
        await client.send_message(message.channel,'Pong!')
    if message.content == 'b!version':
        await client.send_message(message.channel,'Current Version: **Bastion 6.4**')
    if message.content == 'b!credits':
        await client.send_message(message.channel,'**Credits to WolfHussain for creating me with such IQ and thinking ability. Thank him please :)**')
    if message.content == 'b!servercount':
        await client.send_message(message.channel,'*Currently working for approximatly 212 Servers*')
    if message.content.startswith('b!status') and message.author.id == config.OWNERID:
        await client.change_presence(game=discord.Game(name=message.content[7:]))
    if message.content.startswith('b!joke'):
            chuckJoke = requests.get('http://api.icndb.com/jokes/random?')
            if chuckJoke.status_code == 200:
                chuckJoke = chuckJoke.json()['value']['joke']
                await client.send_message(message.channel, chuckJoke)
    await client.process_commands(message)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('*Messages Deleted, Sir.*')

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.Member, *, arg = None):
    if arg is None:
        await client.say("Please provide a reason for {}'s warning.".format(user.name))
        return False
    reason = arg
    author = ctx.message.author
    server = ctx.message.server
    embed = discord.Embed(title="Warn", description=" ", color=0x00ff00)
    embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
    embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
    embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
    await client.say(embed=embed)
    await client.send_message(user, "You have been warned for: {}".format(reason))
    await client.send_message(user, "from: {} server".format(server))

@client.command(pass_context=True)
async def info():
    embed = discord.Embed(
        title = 'Name:',
        description = 'Bastion#3765',
        colour = discord.Colour.blue()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_author(name='Information Section:',
    icon_url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.add_field(name='Creator:', value='TheGreenMammon#0001.', inline=False)
    embed.add_field(name='Creation Date:', value='12th Dec 2018.', inline=False)
    embed.add_field(name='Coded from:', value='3.6.5 Python Shell.', inline=False)
    embed.set_footer(text='© 2019 - Bastion Company Inc.')

    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    await client.say('Help is on its way! Check your DM.')
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()

    )

    embed.set_author(name='Help | Commands')
    embed.add_field(name='b!info', value='Gives you information about me.', inline=False)
    embed.add_field(name='b!playerinfo', value='Gives you information about the player.', inline=False)
    embed.add_field(name='b!serverinfo', value='Gives you information about the server.', inline=False)
    embed.add_field(name='b!ping', value='Gives you information about my Latency.', inline=False)
    embed.add_field(name='b!ban', value='Bans a player.', inline=False)
    embed.add_field(name='b!unban', value='Unbans a player.', inline=False)
    embed.add_field(name='b!kick', value='Kicks a player.', inline=False)
    embed.add_field(name='b!mute', value='Mutes a player.', inline=False)
    embed.add_field(name='b!unmute', value='Unmutes a player.', inline=False)
    embed.add_field(name='b!warn', value='Warns a player.', inline=False)
    embed.add_field(name='b!purge', value='Clears a message.', inline=False)
    embed.add_field(name='b!join', value='Joins the channel.', inline=False)
    embed.add_field(name='b!leave', value='Leaves the channel.', inline=False)
    embed.add_field(name='b!play', value='Plays the music you want the bot to play in the url.', inline=False)
    embed.add_field(name='b!pause', value='Pauses the music.', inline=False)
    embed.add_field(name='b!stop', value='Stops the music.', inline=False)
    embed.add_field(name='b!resume', value='Resumes the music.', inline=False)
    embed.add_field(name='b!punch', value='Punchs the member.', inline=False)
    embed.add_field(name='b!members', value='Gives you the member count of the server.', inline=False)
    embed.add_field(name='b!credits', value='Gives you credits to who made me.', inline=False)
    embed.add_field(name='b!servercount', value='Gives you the amount of servers i am working for.', inline=False)
    embed.add_field(name='b!version', value='Gives you the version of me.', inline=False)
    embed.add_field(name='b!joke', value='Gives you a funny joke. ', inline=False)
    embed.add_field(name='b!say', value='Says something with the specified message.', inline=False)
    embed.add_field(name='b!announcementhere', value='Announces something with a @here', inline=False)
    embed.add_field(name='b!announcementeveryone', value='Announces something with a @everyone', inline=False)
    embed.add_field(name='b!setnick', value='Sets a nick for the specified player.', inline=False)
    embed.add_field(name='b!restart', value='Restarts the bot.', inline=False)
    embed.add_field(name='b!leave', value='Makes the bot leave the discord server.', inline=False)
    embed.add_field(name='b!broadcast', value='Broadcasts the message to all servers that the bot is in', inline=False)


    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leavechannel(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True)
async def playerinfo(ctx, user: discord.Member):
    embed = discord.Embed(title='{} Info:'.format(ctx.message.author.name), description='Here is  what i could find, Sir.', color=0x00ff00)
    embed.add_field(name='Name:', value='ctx.message.author.name', inline=False)
    embed.add_field(name='ID:', value='ctx.message.author.id', inline=False)
    embed.add_field(name='Status:', value='ctx.message.author.status', inline=False)
    embed.add_field(name='Highest Role:', value='ctx.message.author.top_role', inline=False)
    embed.add_field(name='Joined At:', value='ctx.message.author.joined_at', inline=False)
    embed.set_thumbnail(url='ctx.message.author.avatar_url')

    await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(
        title = 'Server Information:',
        description = 'Information is on its way!',
        colour = discord.Colour.blue()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.set_author(name='Server Information:',
    icon_url='https://cdn.discordapp.com/attachments/434288295548026886/529380566244655114/images.jpg')
    embed.add_field(name='Server Name:', value='Custom Discord Bot Testing Server.', inline=False)
    embed.add_field(name='Creation Date:', value='4th Dec 2018.', inline=False)
    embed.add_field(name='Made By:', value='Discord | Discord, Please Sponser Me.', inline=False)
    embed.add_field(name='ID:', value='ctx.message.server.id', inline=False)
    embed.add_field(name='Roles:', value='len(ctx.message.server.roles)', inline=False)
    embed.add_field(name='Members:', value='len(ctx.message.server.members)', inline=False)

    await client.say(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    if ctx.message.author.id in authorized_users:
        role = discord.utils.get(member.server.roles, name="Muted")
        await client.add_roles(user, role)
        embed = discord.Embed(title="Mute", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.id in authorized_users:
        role = discord.utils.get(member.server.roles, name="Muted")
        await client.remove_roles(user, role)
        embed = discord.Embed(title="Unmute", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ban(ctx, member: discord.Member, days: int = 1):
    if ctx.message.author.id in authorized_users:
        await client.ban(member, days)
        embed = discord.Embed(title="Ban", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    if ctx.message.author.id in authorized_users:
        server = ctx.message.server
        bans = await client.get_bans(server)
        try:
            uid = int(member)
            uid = str(uid)
            matches = list(filter(lambda u: u.id == uid, bans))
            if not matches:
                return await client.say('no users ids matched with %s' % uid)
            _member = matches[0]
        except ValueError:
            matches = list(filter(lambda u: str(u) == member, bans))
            if not matches:
                return await client.say('no users matched with %s' % member)
            _member = matches[0]
        await client.unban(ctx.message.server, _member)
        embed = discord.Embed(title="Unban", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.id in authorized_users:
        await client.kick(member)
        embed = discord.Embed(title="Kick", description="Successful", color=0x149900)
        embed.add_field(name="User", value=member.id, inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="You do not have permission to use that command, {}.".format(ctx.message.author.name), color=0x990000)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.delete_message(t)
    embed = discord.Embed(title="Ping", description="Pong", color=0x149900)
    embed.add_field(name="Latency", value=str(int(ms)) + " ms", inline=False)
    await client.say(embed=embed)
    print(f'Ping {int(ping)}ms')

@client.command(pass_context=True)
async def punch(ctx, user: discord.Member):
    embed = discord.Embed(title="Now Punching", description=user.mention, color=0x149900)
    await client.say(embed=embed)
    embed_2 = discord.Embed(title="You've been punched!", description="By " + ctx.message.author.name, color=0x149900)
    await client.send_message(user, embed=embed_2)

@client.command(pass_context=True)
async def members(ctx):
    embed = discord.Embed(title="Member Count", description=str(len(ctx.message.server.members)), color=0x149900)
    await client.say(embed=embed)

@client.command(brief="Lists roles")
async def roles(ctx, *arg1):

    emb = discord.Embed(title="Roles currently in this server", color=0x546e7a)
    all_roles = ctx.guild.roles

    if arg1[0].strip().lower() == "class":
        emb = discord.Embed(title="Class roles currently in this server", color=0x546e7a)
        global class_roles
        all_roles = class_roles

    length = len(all_roles)
    msg1 = ""
    msg2 = ""

    for i in range(0, math.ceil(length/2)):
        msg1 += all_roles[i].name + "\n"

    embed.add_field(name="\u200b", value=msg1, inline=True)

    for i in range(math.ceil(length/2), length):
        msg2 += all_roles[i].name + "\n"

    embed.add_field(name="\u200b", value=msg2, inline=True)

    await client.say(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def verifyall(ctx):
    for vmember in ctx.guild.members:
        if h not in vmember.roles:
            await vmember.add_roles(h)
        if h in vmember.roles:
            print('member is verified')
    await client.send_message('All members verified.')

@client.command(pass_context=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)

    if not msg: await client.say("Please specify a message to send")
    else: await client.say(msg)
    return

@client.command()
@commands.has_permissions(administrator=True)
async def announcementhere(*args, pass_context=True):
    output = ''
    for word in args:
        output += word
        output += ' '
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )


    embed.add_field(name='Announcement', value =output, inline=False)
    await client.say('@here')
    await client.say(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def announcementeveryone(*args, pass_context=True):
    output = ''
    for      word in args:
        output += word
        output += ' '
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )


    embed.add_field(name='Announcement', value =output, inline=False)
    await client.say('@everyone')
    await client.say(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(manage_nickname=True)
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.say(f"Changed {user}'s nickname to {nickname}")
    await client.change_nickname(user, nickname)

@client.command(pass_content=True)
async def restart():
    await client.say(":arrows_counterclockwise: Restarting Bot...")
    await client.say(":arrows_counterclockwise: Updating OS...")
    await client.say(":arrows_counterclockwise: Updating Commands...")
    await client.say(":arrows_counterclockwise: Confirming System...")
    await client.say(":white_check_mark: Bot Successfully Restarted.")

@client.command(pass_context=True)
async def poke(ctx, member: discord.Member):
    await client.say(":arrows_counterclockwise: Accessing Command...")
    await client.say(":arrows_counterclockwise: Accessing Biofield Command Matrix...")
    await client.say(":arrows_counterclockwise: Sending Message to User...")
    await client.say(":white_check_mark: Successfully Sended Message to User!")
    await client.send_message(member, 'Please give me the code to leave command in #code-sharing.')

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    await client.say(f'Are you sure you want me to leave {ctx.message.server} to confirm type `yes`')
    await client.wait_for_message(author=ctx.message.author, content='yes')
    await client.leave_server(server)

@client.command(pass_context=True)
async def broadcast(ctx, *, msg):
    for server in client.servers:
        for channel in server.channels:
            try:
                await client.send_message(channel, msg)
            except Exception:
                continue
            else:
                break

@client.command(pass_context=True)
async def stats(ctx):
    embed=discord.Embed(title="Bot Stats:", color=0x00ffff)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/532951913583607810/543466086377586708/9469a36c70221a41de36862824c85ba2.png")
    embed.add_field(name="Servers:", value="211", inline=False)
    embed.add_field(name="Users:", value="2314", inline=False)
    embed.add_field(name="Support Server:" , value="Coming Soon...", inline=False)
    embed.add_field(name="Memory:", value="Free: 4.21 GB / Total: 50.00 GB", inline=False)
    embed.set_footer(text="2019 - 2020 | Bastion")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def suggest(ctx, *, msg: str):
    user_formatted = ctx.message.author.name + "#" + ctx.message.author.discriminator
    channel = discord.utils.get(ctx.message.server.channels, name="new-suggestions")
    embed = discord.Embed(title="New Suggestion", description=msg, color=0x149900)
    embed.set_author(name=user_formatted, icon_url=ctx.message.author.avatar_url)
    embed_message = await client.send_message(channel, embed=embed)
    await client.add_reaction(embed_message, ':thumbsup:')
    await client.add_reaction(embed_message, ':thumbsdown:')
    embed_2 = discord.Embed(title="Success", description="Your suggestion has been sent.", color=0x149900)
    await client.send_message(ctx.message.channel, embed=embed_2)
    await client.delete_message(ctx.message)
    
client.run('NTI5MzYzMTI1NTMxNTc0Mjcy.DzTZ5g.ajY3FMBLLFl_Q4iDR5QsIJ_qJ6s')
