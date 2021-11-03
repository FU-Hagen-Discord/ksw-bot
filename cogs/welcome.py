import os
import random 
import asyncio
import utils

from discord.ext import commands

#redundant?
client = discord.Client() 

# Welcome-Msgs
a1 = f"Willkommen {member.mention} auf dem Discordserver von und für Studis der Fakultät für Kultur- und Sozialwissenschaften der FernUni! :partying_face:" \
a2 = f"Hi {member.mention}, herzlich willkommen! :hugging: " \
a3 = f"Hey {member.mention}, hast du Kuchen mitgebracht? :cake:" \
a4 = f"Hey {member.mention} ist da! :partying_face:" \
s1 = f"Hi {member.mention}, es sieht hier ein wenig leer aus - nicht wahr? Im <#{os.getenv('DISCORD_ROLE_CHANNEL')}> kannst du dir Studiengangs- und/ oder Interessenrollen vergeben und die entsprechenden Channels freischalten :wink:" \
s2 = f"Hi {member.mention}, bei dem Channel <#{os.getenv('DISCORD_ROLE_CHANNEL')}> kannst du dir Studiengangs- und/ oder Interessenrollen vergeben lassen: danach werden die dazu passende Modulchannels für dich sichtbar :blush:" \
s3 = f" Moin {member.mention}, in <#{os.getenv('DISCORD_DISCORDTIPPS_CHANNEL')}>  wurden nützliche Infos zu der Plattform Discord gesammelt. :notepad_spiral: Schau gerne vorbei!"\
s4 = f"Willkommen {member.mention}, hast du die <#{os.getenv('DISCORD_OFFTOPIC_CHANNEL')}> schon entdeckt? :teapot: Dort kann man über alles reden, was nicht studiumspezifisch ist - #offtopic 😊. " \
s5 = f":wave: {member.mention}, erzähl gerne etwas über dich in <#{os.getenv('DISCORD_INTRODUCTION_CHANNEL')}>." \
s6 = f"Hallo {member.mention}! Mach es dir gemütlich und zögere nicht, mir per privaten Nachricht Fragen zu stellen, wenn du Hilfe vom Orga-Team brauchst :love_letter:" \
s7 = f" Hey {member.mention}! Im Channel <#{os.getenv('DISCORD_UNITALK_CHANNEL')}> kannst du dich mit Kommilitoninnen über Themen rund um das Studium unterhalten :student: " \

#List
welcome_messages = a1, a2, a3, a4, s1,s2, s3, s4, s5, s6, s7

#copypasta
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = int(os.getenv("DISCORD_GREETING_CHANNEL"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.bot.fetch_channel(self.channel_id)  
        # random anstatt msg=      
        msg = random.choices(welcome_messages, k=1)[0]
        await message.channel.send(msg)
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
