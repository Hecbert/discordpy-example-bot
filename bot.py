import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord.ui import Button, View
import logging
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

euro_2024_teams = [
    "Germany", "France", "Spain", "Italy", "England", "Netherlands", 
    "Portugal", "Belgium", "Croatia", "Denmark", "Switzerland", "Poland", 
    "Sweden", "Austria", "Czech Republic", "Russia", "Turkey", "Wales", 
    "Scotland", "Ireland"
]

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with the py-cord library
bot = commands.Bot(command_prefix="/", intents=intents)

# Event to show the bot is running
@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user}! Bot is ready and operational.')

# Define a slash command
@bot.slash_command(name="hello", description="Responds with a greeting")
async def hello(ctx):
    await ctx.respond("Hello! Ready to banter? ⚽🎉")
    logging.info("Hello command was executed.")

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        logging.error(f'An error occurred while executing the command: {error}')
    else:
        logging.error(f'Unexpected error: {error}')

@bot.slash_command(name="pick_team", description="User picks a number and bot selects a random Euro 2024 team")
async def pick_team(ctx, number: int):
    # Validate the user input
    if number < 1 or number > 20:
        await ctx.respond("Please choose a number from 1 to 20.")
        return

    teams = ["Germany", "France", "Spain", "Italy", "England", "Netherlands", "Portugal", "Belgium", "Croatia", "Denmark", "Switzerland", "Poland", "Sweden", "Austria", "Czech Republic", "Russia", "Turkey", "Wales", "Scotland", "Ireland"]
    team = random.choice(teams)
    await ctx.respond(f"You picked number {number}. Random Euro 2024 Team: {team}")       

# Run the bot using your secure token
bot.run(TOKEN.strip())
