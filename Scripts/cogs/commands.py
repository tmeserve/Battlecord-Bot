import os

import discord
from discord import Client
from discord.ext import commands

from .data.team import Team

from util import Util

util = Util()

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.teams = []

        # self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'classes')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands Cog is ready')
    
    @commands.command()
    async def team(self, ctx):
        print(ctx.message.content)

def setup(client):
    client.add_cog(Commands(client))