import os

from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = int(os.getenv("DISCORD_WELCOME_CHANNEL"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.bot.fetch_channel(self.channel_id)
        msg = f"Hallo {member.mention} und willkommen auf dem KSW-Studi-Server der FernUni, schön dass du hierhergefunden hast! \n"
              f"Wenn du unibezogene Fragen hast: zöger nicht, sie in #studium-talk zu stellen! \n" \
              f'Die #teeküche hier ist der "Off-topic-Channel", also für den lockeren Austausch zwischen Kommilitoninnen :dancers:\n'
              f"Viel Spaß beim Stöbern und Netzwerken!"
        await channel.send(msg)
