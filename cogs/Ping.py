import discord
from discord.ext import commands
import random

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping on ready")
    
    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.bot.latency * 1000)
        await ctx.send(f"pong avec une latence de {bot_latency} ms")







async def setup(bot):
    await bot.add_cog(Ping(bot))
