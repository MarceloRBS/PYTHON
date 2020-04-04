print()
print(f"\033[1m{'LOJÃO MELHOR PREÇO':>42}\033[m\n")

print('|' * 67)
print(f"{'ÁREA DE COMPRA':>40}")
print('|' * 67)

total = maior = 0
caro = ' '
while True:
    produto = input('\nInforme o produto: ').strip()
    valor = float(input('Informe o preço: R$'))
    if valor > maior:
        maior = valor
        caro = produto
    total += valor

    perg = input('\nDeseja adcionar mais produtos ao carrinho? [S/N] ').strip().upper()
    if perg != 'S' and perg != 'N':
        print('\033[31mOps! Algo deu errado.\033[m')
    while True:
        if perg != 'S' and perg != 'N':
            perg = input('Deseja adcionar mais produtos ao carrinho? [S/N] ').strip().upper()
            print('\033[31mOps! Algo deu errado.\033[m')
        else:
            break
    if perg == 'N':
        print()
        break

print('|' * 67)
print(f"{'CAIXA':>35}")
print('|' * 67)

print(f'\n# VALOR TOTAL DA COMPRA: R${total:.2f}')
print(f'# PRODUTO MAIS CARO: {caro}')
print('''\n          Opções de pagamento:

[ 1 ] À vista: 20% de desconto \033[32m~MELHOR OPÇÃO~\033[m
[ 2 ] 2x no cartão: preço atual
[ 3 ] 3x ou mais no cartão: 15% de juros''')

escolha = int(input('\n-> Qual opção você prefere? '))
while escolha != 1 and escolha != 2 and escolha != 3:
    print('\033[31mOPÇÃO INEXISTENTE.\033[m')
if escolha == 1:
    desconto = total * 80 / 100
    print(f'O valor total a pagar agora é de R${desconto}.')
if escolha == 2:
    parcelas = total / 2
    print(f'O valor a pagar será duas parcelas de R${parcelas}.')
if escolha == 3:
    nparc = int(input('-> Quantas parcelas serão? '))
    while nparc < 3:
        print('\033[33mSomente o valor 3 ou acima disso.\033[m')
        nparc = int(input('-> Quantas parcelas serão? '))
    jrparc = (total * 115 / 100) / nparc
    print(f'O valor a pagar será {nparc} parcelas de R${jrparc:.2f}.')

print('\n<< VOLTE SEMPRE >>')
