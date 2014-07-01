#encoding:utf-8
import matplotlib.pyplot as plt
import numpy as np

def __get_estrofe(index, frase, estrofe_atual):
    dias=('first','second', 'third','fourth','fifth', 'sixth', 'seventh', 'eighth', 'ninth','tenth','eleventh','twelfth')
    
    estrofe_atual[0] = estrofe_atual[0].replace(dias[index],dias[index+1])
    estrofe_atual[-1] = estrofe_atual[-1].replace('A partridge', 'And a partridge')
    estrofe_atual.insert(1,frase)
    
    return estrofe_atual


def __imprime(musica):
    print "The Twelve Days Of Christmas"
    print '-'*20 + '\n'    
    print musica

def __geraGrafico(valoresGrafico):
    valores_x=valoresGrafico.keys()
    valores_y=valoresGrafico.values()

    plt.plot(valores_x, valores_y, color='blue', label="Palavras por nova estrofe", linewidth="2")
    
    plt.xlabel('Numero de estrofes')
    plt.ylabel('Numero de palavras')
    plt.title('Cap. 02 / exercicio 07')
    plt.legend(loc="lower right")
    plt.xticks(valores_x)
    plt.yticks(valores_y)
    
    ax = plt.axes()            
    ax.grid()
        
    plt.show()
    


frases=[]
frases.append("Two turtle doves, \n")
frases.append("Three French hens, \n")
frases.append("Four calling birds, \n")
frases.append("Five golden rings, \n")
frases.append("Six geese a-laying,\n")
frases.append("Seven swans a-swimming, \n")
frases.append("Eight maids a-milking, \n")
frases.append("Nine ladies dancing, \n")
frases.append("Ten lords a-leaping, \n")
frases.append("Eleven pipers piping, \n")
frases.append("Twelve drummers drumming, , \n")


l_inicial="On the first day of Christmas,\nmy true love sent to me\n"
l_final="A partridge in a pear tree.\n\n"
valoresGrafico={}

estrofe_atual=[l_inicial,l_final]
musica = ''.join(estrofe_atual)
valoresGrafico[1]=len(musica.split())

for index,frase in enumerate(frases):
    musica += ''.join(__get_estrofe(index, frase, estrofe_atual))
    valoresGrafico[index+2]=len(musica.split())

    
__imprime(musica)

__geraGrafico(valoresGrafico)