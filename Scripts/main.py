import os
import json

import discord
from discord.ext import commands
from discord.utils import get

# from cogs.cmds.team import Team

client = commands.Bot(command_prefix='v?', case_insensitive=True)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} cog is loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} cog is unloaded')

# client.add_cog(Team(client))

for filename in os.listdir('./cogs'):
    if filename == '__init__.py':
        continue
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

def load_secrets():
    # os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cmds')
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')
    filename = os.path.join(directory, 'secrets.json')
    
    secrets = json.load(open(filename, 'r'))

    client.run(secrets['token'])

def load_config():
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')
    filename = os.path.join(directory, 'config.json')
    
    config = json.load(open(filename, 'r'))

    client.command_prefix = config['prefix']

load_config()
load_secrets()