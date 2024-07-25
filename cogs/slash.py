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

class Slashcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} charger corectement")
    
    @app_commands.command(name="addition", description="fait une addition")
    async def addition(self, interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
        result = thing_to_say + thing_to_say2
        await interaction.response.send_message(f"le resultat de {thing_to_say} plus {thing_to_say2} est de {result}")
    
    @app_commands.command(name="soustraction", description="fait une soustraction")
    async def soustraction(self, interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
        result = thing_to_say - thing_to_say2
        await interaction.response.send_message(f"le resultat de {thing_to_say} moins {thing_to_say2} est de {result}")
    
    @app_commands.command(name="multiplication", description="fait une multiplication")
    async def multiplication(self, interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
        result = thing_to_say * thing_to_say2
        await interaction.response.send_message(f"le resultat de {thing_to_say} fois {thing_to_say2} est de {result}")
    
    @app_commands.command(name="division", description="fat une division")
    async def division(self, interaction: discord.Interaction, thing_to_say: int, thing_to_say2: int):
        result = thing_to_say / thing_to_say2
        await interaction.response.send_message(f"le resultat de {thing_to_say} diviser par {thing_to_say2} est de {result}")
    
    app_commands.describe(name="dit", description="le bot envoie se que tu as a dire")
    async def dit(self, interaction: discord.Interaction, thing_to_say: str):
        await interaction.response.send_message(f"{interaction.user.name} a dit: {thing_to_say}")


async def setup(bot):
    await bot.add_cog(Slashcommand(bot))

