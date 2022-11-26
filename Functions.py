

import discord, textwrap

import Functions


def Clean_Command(String, Command):

    #Rimuoviamo il commando dalla stringa
    index = String.index(Command) + len(Command)
    Text = String[index:]
    if(Text[0] == " "): Text = Text[1:]

    return Text


#Funzione per recuperare il nome della variabile come stringa
def retrieve_var_name(var, local_variables):

    #Per ogni variabile in local_variables, ne controlla il nome ([0]) solo se è uguale a var
    name = [k for k, v in local_variables.items() if v == var][0]

    return name


async def retrieve_code_from_file(file):



    File_bytes = await file.read()


    #Trasformiamo l'oggetto Byte in una stringa di Python3 (gli oggetti byte iniziano con la b)
    code = File_bytes.decode()



    return code

async def chat_print(channel, *arg):

    #Trasfromiamo tutti gli argomenti in un'unica stringa
    string = ""
    for i in range(len(arg)):
        string += str(arg[i])

    await channel.send("> **>>>** " + string)

    return


async def chat_input(channel, client, *arg):

    # Trasfromiamo tutti gli argomenti in un'unica stringa
    string = ""
    for i in range(len(arg)):
        string += str(arg[i])

    #Inviamo la stringa/stringhe inserite
    await channel.send("> **>>>** " + string)

    #Creiamo un check per assicurarci che il prossimo messaggio sia nello stesso canale
    def check(m):
        return m.channel == channel

    #Aspettiamo un nuovo messaggio
    new_msg = await client.wait_for("message", check=check)

    # cerchiamo il primo spazio
    new_input = new_msg.content
    index = new_input.index(" ")
    new_input = new_input[index + 1:]

    await channel.send("> **<<<** " + str(new_input))

    return new_input



def interactive_command_replace(code, channel, client):


    #Rimpiazziamo il print con chat_print
    new_code = code.replace("print(", "await chat_print(" + retrieve_var_name(channel, locals()) + ",")


    #Rimpiazziamo il print con input_print
    new_code = new_code.replace("input(", "await chat_input(" + retrieve_var_name(channel, locals()) + "," +
                            retrieve_var_name(client, locals()) + ",")

    #se vi dovessero essere delle definizioni di funzione siamo sicuri queste siano asincrone
    #new_code = new_code.replace("def", "async def").


    return new_code


async def interactive_execute(channel, client, code):


    '''
    Il programma da svolgere deve essere eseguito all'interno di una funzione asincrona in modo tale che
    si possano utilizzare comandi interattivi che richiedano di aspettare la risposta dell'utente

    Per questa ragione è necessario definire una funzione asincrona e incollarci il resto del programma
    '''

    interactive_code = "async def executing(channel, client, code):\n"


    # Sostituiamo il print con la funzione chat_print
    code = interactive_command_replace(code, channel, client)

    #Aggiungiamo il prefisso in modo tale che il programma sia svolto come una funzione asincrona e indentiamo tutto il resto del programma
    interactive_code = interactive_code + textwrap.indent(code, '  ')

    #dedentiamo il codice
    interactive_code = textwrap.dedent(interactive_code)

    #eseguiamo il codice che definirà una nuova funzione
    exec(interactive_code, globals())
    #chiamiamo la funzione
    await executing(channel, client, code)


    return

