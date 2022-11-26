import textwrap




#Variabile per salvare il vecchio codice in caso si stia aspettando un nuovo input
preceding_code = " "

Awaiting_Input = False



'''sync def Ex_Command(new_input, channel):


    #Controlliamo se stiamo già aspettando un input

    if(not Interactive.Awaiting_Input):

        par_index = new_input.index("(")
        end_par_index = new_input.index(")")



        #Mandare un messaggio in chat se si scrive print
        if(new_input[0:par_index] == "print"):

            string = new_input[par_index + 1:end_par_index]
            await channel.send("> **>>>** " + string)


        # Mandare un messaggio in chat e aspettare per una ricezione
        if ("input" in new_input):

            #Cerchiamo l'indice dell'uguale
            equal_index = new_input.index("=")

            preceding_code = new_input[0:equal_index+1]

            string = new_input[par_index + 2:end_par_index - 1]
            await channel.send("> **>>>**  '" + string + "'")

            #Alziamo la flag, per avvisare che stiamo aspettando un input
            Interactive.Awaiting_Input = True


    #Se stiamo aspettando un input
    elif(Interactive.Awaiting_Input):

        global var

        var = new_input

        Interactive.Awaiting_Input = False
        await channel.send("> **<<<**  '" + new_input + "'")

    return'''


async def run_code(code, channel):

    # set per le variabili che saranno nel codice eseguito
    loc = {}

    code = textwrap.dedent(code)

    exec(code, globals(), loc)

    # Salva la variabile ritornata dall'exec

    output = loc['output']

    if (output == 33):
        await channel.send(36)
    else:
        await channel.send(output)

    return