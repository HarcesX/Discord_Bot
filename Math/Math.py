
import matplotlib.pyplot as plot
import numpy

async def graph_sen():

    #Assegnando 100 valori all'asse x, da -pi a 4pi
    x = numpy.linspace(-numpy.pi, 4*numpy.pi, 100)

    y = numpy.sin(x)

    plot.plot(x, y)

    # naming the x axis
    plot.xlabel('x - axis')
    # naming the y axis
    plot.ylabel('y - axis')

    # giving a title to my graph
    plot.title('Grafico Seno')

    file_name = "U:\Programma Zioneee\Python\DiscordBot Test1\Math\plot.png"

    plot.savefig(file_name)

    return file_name


async def graph(Expression, min_x_val, max_x_val, value_numbers):

    '''
    :param Expression:
    :param min_x_val: minimo valore di x rappresentato nel grafico
    :param max_x_val: massimo valore di x rappresentato nel grafico
    :param value_numbers: numero di valori di x
    :return:
    '''


    '''
    Assegniamo i valori x per cui sarà visualizzato il grafico
    Perchè possa essere eseguito come unico codice lo mettiamo
    all'interno di una stringa e la sommiamo all'espressione
    '''
    min_x = str(min_x_val)
    max_x = str(max_x_val)
    value_numbers_string = str(value_numbers)

    addon_string = 'x = numpy.linspace('+ min_x + ',' + max_x + value_numbers_string +')\n'

    Expression = addon_string + Expression


    #Cerchiamo e calcoliamo il valore di y nell'espressione
    loc = {}
    exec(Expression, globals(), loc)
    y = loc['y']
    x = loc['x']



    plot.plot(x, y)

    # naming the x axis
    plot.xlabel('x - axis')
    # naming the y axis
    plot.ylabel('y - axis')

    # giving a title to my graph
    plot.title('Grafico Seno')

    file_name = "U:\Programma Zioneee\Python\DiscordBot Test1\Math\plot.png"

    plot.savefig(file_name)

    return file_name
