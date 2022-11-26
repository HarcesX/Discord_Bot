
import os   #This module provides a portable way of using operating system dependent functionality

import discord

from dotenv import load_dotenv

import Functions, Games.Tris, Math.Math as Math

load_dotenv()  # take environment variables from .env.

#Apriamo il file e prendiamo il il token
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')
BOT_TAG = os.getenv('BOT_TAG')


#Nuovo oggetto
#The client is the object that represetns our connection to Discord.
#A Client handles events, tracks state, and generally interacts with Discord APIs
bot = discord.Client()


#decorator
@bot.event
async def on_ready():

    #cercando il server
    guild = discord.utils.get(bot.guilds, name=GUILD)

    '''
    #lamba è una funzione anonima

    #find cerca il nome della gilda nell'iterabile client.guilds (le gilde sono i server)
    #una volta trovato il valore find lo ritorna
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    '''

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    #.join concatena i valori di un iterabile (lista i.e.) con il separatore che lo precede

    members = "\n - " .join([member.name for member in guild.members])

    #usiamo una f-string (sono più balorde di quelle normali)
    print(f'Guild Members:\n - {members}')

@bot.event
async def on_message(message):
    #Guardiamo chi ha mandato il messaggio
    writer = message.author



    #Se il bot non è menzionato il message.content sarà vuoto
    if((message.content != "") and (writer != bot.user)):

        #Salvo il messaggio
        Text = message.content

        # Puliamo il messaggio dal tag
        Text = Functions.Clean_Command(Text, BOT_TAG)



        if (Text.split()[0] == "graph:"):


            file_name = await Math.graph("y = x * 4", -50, 150.0, 400)

            file_name = discord.File(file_name)

            await message.channel.send(file=file_name , content="Ecco il grafico")



        if (Text.split()[0] == "graph_sen:"):


            file_name = await Math.graph_sen()

            file_name = discord.File(file_name)

            await message.channel.send(file=file_name , content="Ecco il grafico")



        if (Text.split()[0] == "interactive_execute:"):
            # Puliamo il messaggio dal commando
            Text = Functions.Clean_Command(Text, "interactive_execute:")

            print(Text)

            await Functions.interactive_execute(message.channel, bot, Text)



        if (Text.split()[0] == "interactive_run:"):

            #se vi sono attachments
            if(message.attachments):

                code = await Functions.retrieve_code_from_file(message.attachments[0])

                print(code)

                await Functions.interactive_execute(message.channel, bot, code)

        if (Text.split()[0] == "play_tris:"):

            with open(r'U:\Programma Zioneee\Python\DiscordBot Test1\Games\Tris.py', "r") as file:
                code = file.read()
                file.close()

            await Functions.interactive_execute(message.channel, bot, code)



    return



bot.run(TOKEN)
