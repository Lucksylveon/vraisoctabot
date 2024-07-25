import discord
from discord.ext import commands, tasks
import random
import asyncio
from discord import Streaming
from discord.utils import get
from discord import app_commands
import time
import datetime
from datetime import datetime
from discord import file
import json
import os
import typing 

class Bla(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_ready(self):
        print("BLA   on ready")
        
    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(title="commande help de octabot", description="ici tout les commande du bot", color=discord.Color.random())

        help_embed.add_field(name='octabot', value="je suis un bot pour le serveur de octive creer par Luck(二ンフㇶア)", inline=False)
        help_embed.add_field(name="--help", value="affiche se messsage", inline=False)
        help_embed.add_field(name="--ping", value="repond pong avec la latense en ms", inline=False)
        help_embed.add_field(name="--timestamp", value="donne la valeur du timestamp ", inline=False)
        help_embed.add_field(name="--temps", value="donne la date et heure du moment", inline=False)
        help_embed.add_field(name="--tm", value="repond le monbre de menbre present sur le serveur", inline=False)
        help_embed.add_field(name="--reseaux", value="envoie les lien des reseaux de octive", inline=False)
        help_embed.add_field(name="/multiplication", value="pour multiplier deux monbre", inline=False)
        help_embed.add_field(name="/division", value="pour diviser deux monbre", inline=False)
        help_embed.add_field(name="/adddition", value="pour additionner deux monbre", inline=False)
        help_embed.add_field(name="/soustraction", value="pour soustraire deux monbre", inline=False)
        await ctx.send(embed = help_embed)


async def setup(bot):
    await bot.add_cog(Bla(bot))
