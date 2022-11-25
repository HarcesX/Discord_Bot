
import os   #This module provides a portable way of using operating system dependent functionality

import textwrap

import discord
from dotenv import load_dotenv

import Interactive



load_dotenv()  # take environment variables from .env.

#Apriamo il file e prendiamo il il token
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')
PRIVILEGIATO = os.getenv('PRIVILEGIATO')


#Nuovo oggetto
#The client is the object that represetns our connection to Discord.
#A Client handles events, tracks state, and generally interacts with Discord APIs
client = discord.Client()


#decorator
@client.event
async def on_ready():

    #cercando il server
    guild = discord.utils.get(client.guilds, name=GUILD)

    '''
    #lamba è una funzione anonima

    #find cerca il nome della gilda nell'iterabile client.guilds (le gilde sono i server)
    #una volta trovato il valore find lo ritorna
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    '''

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    #.join concatena i valori di un iterabile (lista i.e.) con il separatore che lo precede

    members = "\n - " .join([member.name for member in guild.members])

    #usiamo una f-string (sono più balorde di quelle normali)
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    #Guardiamo chi ha mandato il messaggio
    writer = message.author



    #Se il bot non è menzionato il message.content sarà vuoto
    if(message.content != ""):

        Text = message.content
        #cerchiamo il primo spazio
        index = Text.index(" ")
        Text = Text[index+1:]

        if(Interactive.Awaiting_Input):
            await Interactive.Ex_Command(Text, message.channel)


        elif(Text.split()[0] == "run:"):

            #print("ciao")
            index = Text.index("run: ") + len("run: ")
            Text = Text[index:]

            await Interactive.run_code(Text, message.channel)






    return



client.run(TOKEN)
