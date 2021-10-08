import os

from discord.ext import commands

import utils


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = int(os.getenv("DISCORD_GREETING_CHANNEL"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.bot.fetch_channel(self.channel_id)
        msg = f"Hallo {member.mention} und willkommen auf dem KSW-Studi-Server, schön dass du hierhergefunden hast <a:kitty_clap:864411228130902017>\n"
        await channel.send(msg)
        await utils.send_dm(member,
                            f"Willkommen auf dem Discordserver von und für Studis der Fakultät für Kultur- und Sozialwissenschaften der FernUni!\n\n" \
                            f":placard: Beim Text-Channel <#{os.getenv('DISCORD_ROLE_CHANNEL')}> kannst du dir Studiengangs- und/ oder Interessenrollen vergeben lassen. " \
                            f"__Gut zu wissen:__ Du kannst dann die Modul-Textchannels sehen, wenn du die dazu passende Rolle hast.  \n\n" \
                            f"Bei Bedarf wurden in <#{os.getenv('DISCORD_DISCORDTIPPS_CHANNEL')}> ein paar hilfreiche Infos zum Umgang mit Discord gesammelt, schau gerne rein! \n" \
                            f":books: Im Channel <#{os.getenv('DISCORD_UNITALK_CHANNEL')}> kannst du dich mit Kommilitoninnen über Themen rund um das Studium unterhalten, " \
                            f"in der <#{os.getenv('DISCORD_OFFTOPIC_CHANNEL')}> (der sogenannte Offtopic-Channel) können alle anderen Themen besprochen werden :speech_balloon: \n\n" \
                            f"Und wenn du magst, kannst du gerne etwas über dich in der <#{os.getenv('DISCORD_INTRODUCTION_CHANNEL')}> erzählen.\n\n" \
                            f"Falls du bei etwas Hilfe brauchen solltest, schreib mir doch eine private Nachricht. Das Moderatoren Team wird sich dann bei dir zurück melden. " \
                            f"Mach es dir gemütlich und vorallem: zöger nicht Fragen zu stellen, falls du welche hast!")
