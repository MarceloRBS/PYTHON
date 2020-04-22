# Este é o módulo 'money' do pacote 'utilities'
# Foi criado para resolver o exercício 112 do Curso em Vídeo


def coins(pr=0, uni='R$'):
    """
    -> Formata para unidades monetárias
    :param pr: Valor não formatado
    :param uni: Unidade monetária de preferência
    :return: Retorna o valor formatado
    """
    return f'{uni}{pr:.2f}'.replace('.', ',')


def half(pr=0, format=False):
    """
    -> Retorna a metáde do valor
    :param pr: Valor original
    :param format: Formata o valor para uma unidade monetária
    :return: Retorna o resutado
    """
    new_price = pr / 2
    return new_price if format is False else coins(new_price)


def double(pr=0, format=False):
    """
    -> Retorna o dobro do valor
    :param pr: Valor original
    :param format: Formata o valor para uma unidade monetária
    :return: Retorna o resultado
    """
    new_price = pr * 2
    return new_price if format is False else coins(new_price)


def increasing(pr=0, pe=0, format=False):
    """
    -> Aumentará um valor a depender do percentual
    :param pr: Valor original
    :param pe: Percentual
    :param format: Formata o valor para uma unidade monetária
    :return: Retorna o resuldado com o acréscimo formatado, ou não formatado
    """
    new_price = ((100 + pe) * pr) / 100
    return new_price if format is False else coins(new_price)


def decreasing(pr=0, pe=0, format=False):
    """
    -> Diminuirá um valor a depender do percentual
    :param pr: Valor original
    :param pe: Percentual
    :param format: Formata o valor para uma unidade monetária
    :return: Retorna o resuldado com o decréscimo formatado, ou não formatado
    """
    new_price = ((100 -pe) * pr) / 100
    return new_price if format is False else coins(new_price)


def resume(pr=0, up=0, down=0):
    """
    -> Resume os dados inserídos em uma tabéla
    :param pr: Valor original
    :param up: Percentual de acréscimo (será arredondado)
    :param down: Percentual de decréscimo (será arredondado)
    """
    print('-' * 40)
    print(f'VALUE RESUME:             {coins(pr)}')
    print('-' * 40)
    print(f'Double:                   {double(pr, True)}')
    print(f'Half:                     {half(pr, True)}')
    print(f'{up:.1f}% of increasing:      {increasing(pr, up, True)}'.replace('.', ','))
    print(f'{down:.1f}% of decreasing:      {decreasing(pr, down, True)}'.replace('.', ','))
    print('-' * 40)
