import discord
import random
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import time
import asyncio




# inporte une autre page py 
# from (nom du fichiet ) import ( nom de la fonction )

bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())



# verification du lancement du bot
@bot.event
async def on_ready():
    print("Pres")

    await bot.tree.sync() # command slash

@bot.tree.command(name="test", description="teste")
async def test(i: discord.Interaction):
    await i.response.send_message("coucou")


@bot.tree.command(name="say", description="say en slash")
async def say(ctx, *, texte: str):
    if "@here" in texte or "@everyone" in texte:
        # Envoyer un message d'erreur à l'utilisateur
        await ctx.send("Désolé, vous ne pouvez pas mentionner @here ou @everyone.", hidden=True)
        return
    await ctx.send(texte, hidden=True)



@bot.command()
async def ca(ctx):
    await ctx.send("passe")

@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    serveurname = server.name
    numberChannelsTXT = len(server.text_channels)  
    numberVocal = len(server.voice_channels)
    serverDescription = server.description
    numberMembre = server.member_count
    created_at = server.created_at.strftime("%d/%m/%Y a %H:%M:%S")
    message = f"Le serveur {serveurname} contient {numberChannelsTXT} channels textuels et {numberVocal} salons vocaux avec {numberMembre} membres. Il a été créé le {created_at}."
    await ctx.send(message)
    

@bot.command()
async def say(ctx, *texte):
    if "@here" in " ".join(texte) or "@everyone" in " ".join(texte):
        await ctx.send("Désolé, vous ne pouvez pas mentionner **here** ou **everyone**.")
        await ctx.message.delete()
        return
    await ctx.send(" ".join(texte))
    await ctx.message.delete() # suprime lapelle de command



@bot.command()
async def voc(ctx):
    if ctx.author.voice:
        invite = await ctx.author.voice.channel.create_invite(max_age=86400, max_uses=0, unique=True)
        await ctx.send(f"Voici le lien d'invitation pour le salon vocal actuel : {invite.url}")
        await ctx.message.delete()
    else:
        await ctx.send("Vous devez être connecté à un salon vocal pour utiliser cette commande !")
        await ctx.message.delete()

#@cooldown(1, 60, BucketType.guild) # 1 utilisation toutes les 25 minutes pour tout le serveur


@bot.command(name="pugs")
@commands.cooldown(1, 1200, commands.BucketType.guild)
async def pugs(ctx):
    guild = bot.get_guild(1096891335203627130) # Remplacez GUILD_ID par l'ID de votre serveur
    role = guild.get_role(1097816236622098533) # Remplacez ROLE_ID par l'ID du rôle à pinguer
    await role.edit(mentionable=True)
    await ctx.send(f"{role.mention}, la commande a été exécutée !")
    await asyncio.sleep(10) # Attendre 10 secondes avant de rendre le rôle non pingable
    await role.edit(mentionable=False)

@pugs.error
async def pug_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = round(error.retry_after)
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        await ctx.send(f"Cette commande est en cours de rechargement. Veuillez attendre {minutes} minutes et {seconds} secondes.")


@bot.tree.context_menu(name="France")
async def translate(i: discord.Interaction, message: discord.Message):
    await i.response.defer()
    from deep_translator import GoogleTranslator
    to_translate = message.content
    translated = GoogleTranslator(source='auto', target='fr').translate(to_translate)
    await i.followup.send(translated)


@bot.tree.context_menu(name="English")
async def translate(i: discord.Interaction, message: discord.Message):
    await i.response.defer()
    from deep_translator import GoogleTranslator
    to_translate = message.content
    translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
    await i.followup.send(translated)


@bot.tree.context_menu(name="Italiano")
async def translate(i: discord.Interaction, message: discord.Message):
    await i.response.defer()
    from deep_translator import GoogleTranslator
    to_translate = message.content
    translated = GoogleTranslator(source='auto', target='it').translate(to_translate)
    await i.followup.send(translated)

@bot.tree.context_menu(name="Allemand")
async def translate(i: discord.Interaction, message: discord.Message):
    await i.response.defer()
    from deep_translator import GoogleTranslator
    to_translate = message.content
    translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
    await i.followup.send(translated)

@bot.tree.context_menu(name="عرب")
async def translate(i: discord.Interaction, message: discord.Message):
    await i.response.defer()
    from deep_translator import GoogleTranslator
    to_translate = message.content
    translated = GoogleTranslator(source='auto', target='ar').translate(to_translate)
    await i.followup.send(translated)




# token du bot
# bot.run(token)
with open("token.txt", "r")as f:
    token = f.readlines()
token = token[0].replace("\n", "")
bot.run(token)


# python3 main.py