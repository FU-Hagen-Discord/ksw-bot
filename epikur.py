import os

import disnake
from disnake.ext import commands

from dotenv import load_dotenv

from cogs import appointments, calmdown, help, links, polls, support, timer, welcome, roles, text_commands

# .env file is necessary in the same directory, that contains several strings.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))
ACTIVITY = os.getenv('DISCORD_ACTIVITY')
PIN_EMOJI = "📌"

# intents = disnake.Intents.default()
# intents.members = True
# bot = commands.Bot(command_prefix='!', help_command=None, activity=disnake.Game(ACTIVITY), intents=intents)
class Epikur(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', help_command=None, activity=disnake.Game(ACTIVITY),
                         intents=disnake.Intents.all())
        self.add_cogs()
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            if timer_cog := self.get_cog("Timer"):
                self.add_view(timer_cog.get_view())
        print("Client started!")

    def add_cogs(self):        
        self.add_cog(appointments.Appointments(bot))
        self.add_cog(calmdown.Calmdown(bot))
        self.add_cog(help.Help(bot))
        self.add_cog(links.Links(bot))
        self.add_cog(polls.Polls(bot))
        self.add_cog(support.Support(bot))
        self.add_cog(timer.Timer(bot))
        self.add_cog(welcome.Welcome(bot))
        self.add_cog(roles.Roles(bot))
        self.add_cog(text_commands.TextCommands(bot))


bot = Epikur()        


def get_reaction(reactions):
    """ Returns the reaction that is equal to the specified PIN_EMOJI,
    or if that reaction does not exist in list of reactions, None will be returned"""

    for reaction in reactions:
        if reaction.emoji == PIN_EMOJI:
            return reaction
    return None


async def pin_message(message):
    """ Pin the given message if it is not already pinned """

    if not message.pinned:
        await message.pin()


async def unpin_message(message):
    """ Unpin the given message if it is pinned, and it has no pin reaction remaining. """

    if message.pinned:
        reaction = get_reaction(message.reactions)
        if reaction is None:
            await message.unpin()


@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return

    if payload.emoji.name == PIN_EMOJI:
        channel = await bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        await pin_message(message)


@bot.event
async def on_raw_reaction_remove(payload):
    if payload.emoji.name == PIN_EMOJI:
        channel = await bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        await unpin_message(message)


bot.run(TOKEN)
