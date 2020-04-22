# Confira o pacode 'utilities' para testar outras funcionalidades
from utilities import money
from utilities import data

p = data.ready_correct('Type a value: R$') # Preço
increase = data.ready_correct('Type a value for increasing: ') # Percentual de aumento
decrease = data.ready_correct('Type a value for decreasing: ') # Percentual de queda
money.resume(p, increase, decrease)
