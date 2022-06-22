import os
import random

import disnake
from disnake.ext import commands

import utils


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = int(os.getenv("DISCORD_GREETING_CHANNEL"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.bot.fetch_channel(self.channel_id)
        welcome_messages = [
            f"Willkommen {member.mention} auf dem Discordserver von und für Studis der Fakultät für Kultur- und "
            f"Sozialwissenschaften der FernUni! :partying_face:",
            f"Hi {member.mention}, herzlich willkommen! :hugging: ",
            f"Hey {member.mention}, hast du Kuchen mitgebracht? :cake:",
            f"Hey {member.mention} ist da! :partying_face:",
            f"Hi {member.mention}, es sieht hier ein wenig leer aus - nicht wahr? Im "
            f"<#{os.getenv('DISCORD_ROLE_CHANNEL')}> kannst du dir Studiengangs- und/ oder Interessenrollen vergeben "
            f"und die entsprechenden Channels freischalten :wink:",
            f"Hi {member.mention}, bei dem Channel <#{os.getenv('DISCORD_ROLE_CHANNEL')}> kannst du dir Studiengangs- "
            f"und/ oder Interessenrollen vergeben lassen: danach werden die dazu passende Modulchannels für dich "
            f"sichtbar :blush:",
            f" Moin {member.mention}, in <#{os.getenv('DISCORD_DISCORDTIPPS_CHANNEL')}>  wurden nützliche Infos zu der "
            f"Plattform Discord gesammelt. :notepad_spiral: Schau gerne vorbei!",
            f"Willkommen {member.mention}, hast du die <#{os.getenv('DISCORD_OFFTOPIC_CHANNEL')}> schon entdeckt? "
            f":teapot: Dort kann man über alles reden, was nicht studienspezifisch ist - #offtopic 😊. ",
            f":wave: {member.mention}, erzähl gerne etwas über dich in <#{os.getenv('DISCORD_INTRODUCTION_CHANNEL')}>.",
            f"Hallo {member.mention}! Mach es dir gemütlich und zögere nicht, mir per privaten Nachricht Fragen zu "
            f"stellen, wenn du Hilfe vom Orga-Team brauchst :love_letter:",
            f" Hey {member.mention}! Im Channel <#{os.getenv('DISCORD_UNITALK_CHANNEL')}> kannst du dich mit "
            f"Kommilitoninnen über Themen rund um das Studium unterhalten :student: "
        ]

        msg = random.choice(welcome_messages)
        await channel.send(msg)
        await utils.send_dm(member,
                            f"Willkommen auf dem Discordserver von und für Studis der Fakultät für Kultur- und "
                            f"Sozialwissenschaften der FernUni!\n\n"
                            f":placard: Beim Text-Channel <#{os.getenv('DISCORD_ROLE_CHANNEL')}> kannst du dir "
                            f"Studiengangs- und/ oder Interessenrollen vergeben lassen. "
                            f"\n__Gut zu wissen:__ Du kannst dann die Modul-Textchannels sehen, wenn du die dazu "
                            f"passende Rolle hast.  \n\n"
                            f"Bei Bedarf wurden in <#{os.getenv('DISCORD_DISCORDTIPPS_CHANNEL')}> hilfreiche Infos zum"
                            f" Umgang mit Discord gesammelt, schau gerne rein! \n"
                            f":books: Im Channel <#{os.getenv('DISCORD_UNITALK_CHANNEL')}> kannst du dich mit "
                            f"Kommilitoninnen über Themen rund um das Studium unterhalten, "
                            f"in der <#{os.getenv('DISCORD_OFFTOPIC_CHANNEL')}> (der sogenannte Offtopic-Channel) "
                            f"können alle anderen Themen besprochen werden :speech_balloon: \n\n"
                            f"Und wenn du magst, kannst du gerne etwas über dich in der "
                            f"<#{os.getenv('DISCORD_INTRODUCTION_CHANNEL')}> erzählen.\n\n"
                            f"Falls du bei etwas Hilfe brauchen solltest, schreib mir doch eine private Nachricht. Das "
                            f"Orga-Team wird sich dann bei dir zurück melden. "
                            f"Mach es dir gemütlich und vorallem: zöger nicht Fragen zu stellen, falls du welche hast!")
