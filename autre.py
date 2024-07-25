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



class Autre(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("les bonus on ready")
    
    @commands.command()
    async def tm(self, member):
        await member.send(f"totale des menbre sur le serveur {member.guild.member_count} menbre")





    @commands.command()
    async def reseaux(self, ctx):
        youtubel = "https://www.youtube.com/@octivem"
        twitchl = "https://www.twitch.tv/octivemytb"
        embed = discord.Embed(title = "les different lien de octive", description = f"sur youtube {youtubel}\n et aussi sur twitch {twitchl}")
        embed.set_thumbnail(url = "https://yt3.googleusercontent.com/XBJgZ63uUpvQf_imUpc6MEKg5QhLyDpA5slxf6AQZH266v5v5hgV2ZSExFV-8yndbFFPEl0lbaI=s176-c-k-c0x00ffffff-no-rj")

        await ctx.send(embed = embed)


async def setup(bot):
    await bot.add_cog(Autre(bot))

