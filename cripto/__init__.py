def criptografar(txt):
    '''
    Function para criptografar:
        param 'txt' - Texto para ser criptografado
    '''
    mensagem = str(txt)

    chave = 3
    cifrada = ""
    n = 128

    for letra in mensagem:
        indice = ord(letra)
        nova_letra = chr((indice + chave)%n)
        cifrada = cifrada + nova_letra

    return cifrada


def descriptografar(txt):
    '''
    Function para descriptografar:
        param 'txt' - Texto para ser descriptografado
    '''
    mensagem = str(txt)
    
    chave = -3
    descifrada = ""
    n = 128

    for letra in mensagem:
        indice = ord(letra)
        nova_letra = chr((indice + chave)%n)
        descifrada = descifrada + nova_letra    

    return descifrada


def armazenar(txt1, txt2):
    '''
    Function para armazenar dados em arquivos texto:
        param 'txt1' - Primeiro texto que deve ser escrito. Fica ao lado do segundo
        param 'txt2' - Segundo texto que deve ser escrito. Fica ao lado do primeiro
    '''
    if txt1 != '' and txt2 != '':
        with open('resultado.txt', 'at') as arquivo:
            arquivo.write(f'{txt1} == ' + f'{txt2}\n')
    else:
        pass


def confirmar():
    '''
    Function usada para perguntar se o user deseja salvar uma information.
    Obs.: O algoritmo usa a primeira letra (S ou N)
    '''
    while True:
        print('\nDeseja salvar o resultado?')

        try:
            confir = input('>>> ').upper()[0]
        except (ValueError, TypeError, IndexError):
            print(f'\033[31mErro! Tente novamente\033[m')
        else:
            if confir != 'S' and confir != 'N':
                print('SOMENTE |S| OU |N|')
            elif confir == 'S':
                print('\n\033[32mMensagem salva!\033[m')
                break
            else:
                break

    return confir
