import discord
from discord.ext import commands, tasks
import random
from discord import Streaming
from discord.utils import get
from discord import app_commands
import time 
import datetime 
from datetime import datetime
import json
from discord import file
#from easy_pil import Editor, load_image_async, font
import typing
from typing import Optional
import math
import asyncio
import os
from discord import RawReactionActionEvent
#from discord.utils import find
import time
from datetime import datetime, timezone, timedelta




bot = commands.Bot(command_prefix="--", intents=discord.Intents.all())

bot.remove_command("help")
 

status = ["avec Octive | --help", "discord | --help", "avec moi-meme | --help", "avec toi | --help", "avec Luck(ニンフィア) | --help", "ma vie de bot | --help", "avec Legoeloi | --help", "rien | --help"]






@tasks.loop(minutes = 0, seconds = 30)
async def changeStatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status = discord.Status.online, activity = game)


@bot.event
async def on_ready():
    print("bot connecter avec succes a discord")
    changeStatus.start()
    editChannel.start()



@tasks.loop(minutes= 5, seconds= 30)
async def editChannel():
    channeln = bot.get_channel(1111700846057639997)
    enligne = await bot.fetch_guild(935219559189864540, with_counts=True)
    await channeln.edit(name = f"en ligne {enligne.approximate_presence_count} / {enligne.approximate_member_count} membres")



async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith("py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")



@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1009383466644807780)
    
    embed = discord.Embed(title = (member), description = "bienvenue a toi sur le serveur de octive m", color = 0x3377FF)
    embed.set_image(url=member.display_avatar)

    embed.add_field(name = "total des menbres", value = (member.guild.member_count))
    await channel.send(f"merci {member.mention}")


    await channel.send(embed= embed)
    guild = member.guild
    #channeln = bot.get_channel(1111700846057639997)
    #await channeln.edit(name = f"total des membre: {member.guild.member_count}")
    

channel = (1009383466644807780)



@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1009383466644807780)
    embed = discord.Embed(title =f"dommage {member.name}", description = "un menbre vient de nous quitter", color =0xBE2808)

    await channel.send(embed= embed)
    guild = member.guild
    #channeln = bot.get_channel(1111700846057639997)
    #await channeln.edit(name = f"total des membre: {member.guild.member_count}")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit= amount)

@bot.command()
async def tt(ctx):
    # Dictionnaires des noms des mois et des jours en japonais
    tokyo_timezone = timezone(timedelta(hours=9))
    mois_japonais = {
    1: "1月", 2: "2月", 3: "3月", 4: "4月", 5: "5月", 6: "6月",
    7: "7月", 8: "8月", 9: "9月", 10: "10月", 11: "11月", 12: "12月"
}

    jour_japonais = {
    0: "月曜日", 1: "火曜日", 2: "水曜日", 3: "木曜日",
    4: "金曜日", 5: "土曜日", 6: "日曜日"
}

    #Obtenir la date et l'heure actuelles à Tokyo
    heure_tokyo = datetime.now(tokyo_timezone)

    # Obtenir le numéro du mois et du jour
    numero_mois = heure_tokyo.month
    numero_jour_semaine = heure_tokyo.weekday()

    # Obtenir les noms en japonais
    nom_mois_japonais = mois_japonais[numero_mois]
    nom_jour_semaine_japonais = jour_japonais[numero_jour_semaine]
    hm = datetime.now(tokyo_timezone)
    hmfor = hm.strftime("%H:%M")
    an = datetime.now(tokyo_timezone)
    ye = an.strftime("%Y")

    # Formater l'heure de Tokyo avec les noms en japonais
    heure_formatee = "{}{}日 {}".format(nom_mois_japonais, heure_tokyo.day, nom_jour_semaine_japonais)
    await ctx.send(f"a tokyo on est le: {ye}年{heure_formatee} a {hmfor} ")



@bot.command(name="embed")
@commands.has_permissions(manage_messages=True)
async def embed(ctx, channel: commands.TextChannelConverter):
    await ctx.send(f"{ctx.author} envoyez votre message dans les 60 secondes")
    try:

        msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
        embed = discord.Embed(
                    type='article',
                    description=msg.content
                    )
        await channel.send(embed=embed)
 

    except asyncio.TimeoutError:
        await ctx.send("Temps écoulé relancez la commande.")

@bot.command()
async def presence(ctx):
    persent = await bot.fetch_guild(1008865119943524363, with_counts=True)
    await ctx.send(f"le nombre en ligne {persent.approximate_presence_count} utilisateur")
""" ----------------------------------------------------------------------
"""
""""
@bot.event
async def on_message(message):
    
    
        
    
    
    if message.author.bot == False:

      if message.author.guild.id == 935219559189864540:
            
        with open('level.json', 'r') as f:
            users = json.load(f)
            gain = [10, 15, 20, 25, 30]
            ajj = random.choice(gain)
        
            gaina = [30, 45, 60, 75, 90]
            ajja = random.choice(gaina)

            await update_data(users, message.author)
            
            if message.author.guild_permissions.manage_channels == True:
                if message.content.startswith('--'):
                    await add_experience(users, message.author, 0)
                else:
                    await add_experience(users, message.author, ajja)
            else:
                if message.content.startswith('--'):
                    await add_experience(users, message.author, 0)
                else:
                    await add_experience(users, message.author, ajj)
            await level_up(users, message.author, message)

            with open('level.json', 'w') as f:
                json.dump(users, f)

    await bot.process_commands(message)


#users[f'{user.id}']

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        
        
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['totalexp'] = 0
        users[f'{user.id}']['level'] = 0


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp
    users[f'{user.id}']['totalexp'] += exp



async def level_up(users, user, message):
    with open('level.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    channelv = bot.get_channel(1009404407378616390)
    lvl_final = lvl_start + 1
    back_xp = (100 + lvl_start ** 3)
    xp_need = (100 + lvl_final ** 3)
    if experience > xp_need:
        await channelv.send(f'{user.mention} tu as telement parler que tu est niveau: {lvl_final}')
        users[f'{user.id}']['level'] = lvl_final
        users[f'{user.id}']['experience'] -= back_xp

"""

@bot.event
async def on_message(message):
    
    
    
    
    
    if message.author.bot == False:
    
        if message.author.guild.id == 935219559189864540:
        
            
            with open('level.json', 'r') as f:
                users = json.load(f)
                gain = [10, 15, 20, 25, 30]
                ajj = random.choice(gain)
            
            

                await update_data(users, message.author)
                

                
                
            
                if message.content.startswith('--'):
                    await add_experience(users, message.author, 0)
                else:
                    await add_experience(users, message.author, ajj)
                await level_up(users, message.author, message)

                
                with open('level.json', 'w') as f:
                    json.dump(users, f)
        
        

    await bot.process_commands(message)


async def auto_responce(message, user: discord.User, dm: discord.DMChannel):
    if message in dm:
        await user.send("test")
 
async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['last_level'] = 0
        users[f'{user.id}']['totalexp'] = 0
        users[f'{user.id}']['level'] = 0


async def add_experience(users, user, exp):
    
    #users[f'{user.id}']['experience'] += exp
    users[f'{user.id}']['totalexp'] += exp


async def level_up(users, user, message):
    with open('level.json', 'r') as g:
        levels = json.load(g)
    last_level = users[f'{user.id}']['last_level']
    lvl = users[f'{user.id}']['level']
    experience = users[f'{user.id}']['totalexp']
    channelv = bot.get_channel(1009404407378616390)
    lvl = 0.1*(math.sqrt(experience))
    if int(lvl) > last_level:
        await channelv.send(f'{user.mention} tu as telement parler que tu est niveau: {int(lvl)}')
        users[f'{user.id}']['last_level'] = int(lvl)

@bot.hybrid_command(name="level", description="donne le classement")
async def level(ctx, x=10):
  with open('level.json', 'r') as f:
    
    users = json.load(f)
    
  leaderboard = {}
  total=[]
  
  
  
  for user in list(users):
    name = int(user)
    total_amt = users[str(user)]['totalexp']
    total_amt2 = users[str(user)]['level']
    leaderboard[total_amt] = name
    
    
    total.append(total_amt)

    

   

  

    

  total = sorted(total,reverse=True)
  

  
  

  emb = discord.Embed(
    title = f'Top {x} des plus haut niveau sur le serveur de octive m',
    description = 'les plus haut niveau',
    color=discord.Color.random()
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    
    member = bot.get_user(id_)

    
    

    emb.add_field(name = f'{index}: {member}', value = f'{amt} xp est level {int(0.1*(math.sqrt(amt)))}', inline=False)
    
    
    
    if index == x:
      break
    else:
      index += 1
      
  await ctx.send(embed = emb)


@bot.hybrid_command(name="levelancien", description="donne votre place dans le leaderboard")
async def levelancient(ctx, x=10):
  with open('level.json', 'r') as f:
    
    users = json.load(f)
    
  leaderboard = {}
  total=[]
  lvl = users[f'{user.id}']['level']


  for user in list(users):
    name = int(user)
    total_amt = users[str(user)]['experience']
    leaderboard[total_amt] = name
    total.append(total_amt)

    

    

  total = sorted(total,reverse=True)
  

  em = discord.Embed(
    title = f'Top {x} des plus haut niveau sur le serveur de octive m',
    description = 'les plus haut niveau',
    color=discord.Color.random()
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    member = bot.get_user(id_)
    
    
    em.add_field(name = f'{index}: {member}', value = f'niveaux {lvl} est xp {amt}', inline=False)
    
    
    if index == x:
      break
    else:
      index += 1
      
  await ctx.send(embed = em)



@bot.hybrid_command(name="rank", description="afffiche votre rang")
async def rank(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('level.json', 'r') as f:
            users = json.load(f)

        

     
        membre= discord.Member.name
        image = ctx.author.avatar
        lvl = users[str(id)]['last_level']
        #exp = users[str(id)]['experience']
        total = users[str(id)]['totalexp']
        exp_prochain = ((int(lvl) + 1 ) / 0.1) ** 2
        exp_prochain = int(exp_prochain)
        exp_tu_as_eu = (int(lvl) / 0.1 ) ** 2
        exp_apres = exp_prochain - exp_tu_as_eu
        exp_tu_as = total - exp_tu_as_eu
        #expl = expf - expd
        #usep = exp - expd
        enb = discord.Embed(title=f"xp total {total}", description="en bas ton niveaux et progression", color=discord.Color.random())
        enb.set_author(name=ctx.author.display_name)
        enb.set_thumbnail(url=f"{image}")
        enb.add_field(name="le niveau", value=f"{lvl}")
        enb.add_field(name="progression", value=f"{int(exp_tu_as)} / {int(exp_apres)} xp")
        enb.add_field(name="level suivant", value=f"{int(exp_apres - exp_tu_as)} xp", inline=False)
        #enb.add_field(name="experience", value=f"{exp} xp total")
        
        if total !=0:
            
            await ctx.send(embed = enb)
        else:
            await ctx.send("vous n'avez pas d'exp commencer par parler dans les channel pour en accumuller")
        
    else:
        id = member.id
        with open('level.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['last_level']
        exp = users[str(id)]['totalexp']
        await ctx.send(f'{member} a le niveau {lvl}!')
        await ctx.send(f'sont xp est de {exp}')


@bot.command()
async def givexp(ctx, user, value: int):
    with open('level.json', 'r') as f:
        users = json.load(f)
    users[f'{user}']['experience'] += value
    
    await ctx.send(f"{value} a etait ajouter a {user}")



async def main():
    async with bot:
        await load()
        await bot.start("token")

asyncio.run(main())
