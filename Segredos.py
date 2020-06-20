from Lib import cripto
from os import system

system('cls') # Irá limpar o terminal para que a exibição do programa se torne mais limpa

print('\n\033[31mCR\033[34mIP\033[33mTEX\033[m \033[34mDI\033[31mGI\033[33mTAL\033[m')
# Criptex seria uma palavra entrecruzada de criptologia e códice (codex).
# Esse termo aparece na obra O Código Da Vinci, do escritor Dan Brown. Na obra se trata de um cofre cilíndrico.
# Logo, o CRIPTEX DIGITAL é uma réplica desse cofre e irá armazenar todos os resultados em um arquivo txt em seu computador.

while True:
    print('''\nO que deseja fazer?
[ 1 ] Criptar
[ 2 ] Descriptar
[ 3 ] Sair''')

    while True:
        try:
            opcoes = int(input('>>> '))
        except (ValueError, TypeError):
            print(f'\033[31mErro de valor ou tipo... Tente novamente\033[m')
        else:
            if opcoes > 3 or opcoes < 1:
                print('\033[31mOpção inexistente... Tente novamente\033[m')
            else:
                break

    if opcoes == 1:
        print('\nDIGÍTE UM TEXTO PARA SER CRIPTOGRAFADO')

        origi = (input('>>> '))
        resul = cripto.criptografar(origi)
        print(f'< {resul} >')

        conf = cripto.confirmar()

        if conf == 'S':
            cripto.armazenar(origi, resul)
    elif opcoes == 2:
        print('\nDIGÍTE UM TEXTO PARA SER DESCRIPTOGRAFADO')

        origi = (input('>>> '))
        resul = cripto.descriptografar(origi)
        print(f'< {resul} >')
        
        conf = cripto.confirmar()

        if conf == 'S':
            cripto.armazenar(origi, resul)
    else:
        break

print('\n\033[33mSaindo...\033[m')
