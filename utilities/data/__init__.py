# Este é o módulo 'data' do pacote 'utilities'
# Foi criado para resolver o exercício 112 do Curso em Vídeo


def ready_correct(msg):
    """
    -> Irá ler a entrada apenas de valores no seguintes formatos: 0 / 0.00 / 0,00
    :param msg: Mensagem para a entrada do valor
    :return: Valor válido
    """
    enter = str(input(msg)).replace(',', '.')
    while enter.strip() == "" or enter.isalpha():
        print(f'\033[31mError: \"{enter}\" not is valid! Try again.\033[m')
        enter = str(input(msg)).replace(',', '.')
    return float(enter)
