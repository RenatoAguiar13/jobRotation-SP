import json

with open('dados.json') as file:
    dados = json.load(file)

# A questão dizia que os dias sem faturamento não deveriam ser contados para a média, mas como não foi deixado claro quanto ao menor faturamento, decidi por leva-los em conta.

menorFaturamento = float('inf')
for dia in dados:
    if dia['valor'] < menorFaturamento:
        menorFaturamento = dia['valor']

maiorFaturamento = 0
for dia in dados:
    if dia['valor'] > maiorFaturamento:
        maiorFaturamento = dia['valor']

# Ignorando os dias sem faturamento e calculando a média:

soma = 0
dias_com_faturamento = 0
for dia in dados:
    if dia['valor'] > 0:
        soma += dia['valor']
        dias_com_faturamento += 1

media = soma / dias_com_faturamento


dias_acima_da_media = 0
for dia in dados:
    if dia['valor'] > media:
        dias_acima_da_media += 1

print('Menor faturamento: R$ {:.4f}'.format(menorFaturamento))
print('Maior faturamento: R$ {:.4f}'.format(maiorFaturamento))
print('Número de dias com faturamento acima da média: {}'.format(dias_acima_da_media))
