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



class Time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("un commande", self)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Time on ready")
    
    @commands.command()
    async def temps(self, ctx):
        actuel = datetime.now()
        await ctx.reply(actuel)
    
    @commands.command()
    async def timestamp(self, ctx):
    
        await ctx.send(f"le timestamp actuelle est de {time.time()} senconde ecouler depuis le 1 janvier 1970")
    

async def setup(bot):
    await bot.add_cog(Time(bot))
