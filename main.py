import discord
import json
from discord.ext import commands
import os

token = input("Enter Token of Your Bot")


Token = token
#customHelpCommands
class CustomHelpCommand(commands.HelpCommands):
  def __init__(self):
    super().__init__


@client.command()
async def send_bot_help(self, mapping, message):
  await ctx.send("Hello"+{message.auther} + "Mello is an upcoming interactive service platform that seeks to redefinethe very concept of entertainment")
  return await super().send_bot_help(mapping)


@client.command()
async def send_cog_help(self, cog, message):
  await ctx.send("Hello"+{message.auther} + "Mello is an upcoming interactive service platform that seeks to redefinethe very concept of entertainment")
  return await super().send_bot_help(cog)


@client.command()
async def send_group_help(self, group, message):
  await ctx.send("Hello"+{message.auther} + "Mello is an upcoming interactive service platform that seeks to redefinethe very concept of entertainment")
  return await super().send_bot_help(group)  






client = commands.bot(commans_prefix = ',',Help_Command=CustomHelpCommand)



#Getting Bot Ready
@client.event
async def On_ready():
  print('We Have Logged in as {0.user}'.client.user)


#checking Which User Has Joined
@client.event
async def on_member_join(member):
  print(f'{member} has joined a server.')
  with open('users.json', 'r')
    users = json.load(f)

  await update_data(users, member)

  with open ('users.json', 'w') as f
        json.dump(users, f)


#Checking which user Has Left
@client.event
async def on_member_remove(member):
  print(f'{member}has left the server .')
  

#On Postings
@client event
async def on_message(message)
 with open('users.json', 'r')
    users = json.load(f)
 
    await update_data(users, message.autherr)
    await add_experience(users, message.auther, 5)
    await level_up(users, message.auter, message.channel)



    with open ('users.json', 'w') as f
            json.dump(users, f)


#updating data
async def update_data(user, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1


#adding Experiences
async def add_experience(users, user, exp):
    users[user.id]['experience'] +=exp


#leveling up the users
async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(ecperience ** (1/4))


    if lvl_start < lvl_end:
        await client.sendmessage(channel, '{} has leveled up to level {}'.format{user.mention, lvl_end})
        users[user.id]['level'] = lvl_end



#kicking User Out of the Server
@client.command()
async def kick(ctx, member : discord.Member, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Kicked {user.mention}')


#banning User on server
@client.command()
async def ban(ctx, member : discord.Member, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'banned {user.mention}')


#Unbanning User on Server
@client.command()
async def unban(ctx, *, member):
  banned_users = awaits ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_user:
    user = ban_entry.user

    if(user.name, user,discriminator) == (member_name, member.discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}')
      return


client.run(Token)

