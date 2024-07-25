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



class Modo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("modo on ready")
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
    
    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def tchaname(self, ctx, channel: discord.TextChannel, *, new_name):
        await channel.edit(name=new_name)
    
    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def voicesup(self, ctx, channel: discord.VoiceChannel):
        await channel.delete()



    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def textsup(self, ctx, channel: discord.TextChannel):
        await channel.delete()





    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def vchaname(self, ctx, channel: discord.VoiceChannel, *, new_name):
        await channel.edit(name=new_name)
    
    @commands.command()
    @commands.is_owner()
    async def pick(self, ctx):
        choisir = ["1", "2", "3"]
        await ctx.send(random.choice(choisir))



async def setup(bot):
    await bot.add_cog(Modo(bot))
    
