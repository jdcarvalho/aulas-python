
from custoproducao.custos import armazenar_custo, limpar_banco_existente, \
    obter_custo_total, produzir_milho

# Criada para fins de ensino a fim de manter o mesmo arquivo sempre com os
# custos criados abaixo
limpar_banco_existente()

armazenar_custo('Custo com Combustível', 400)
armazenar_custo('Custo com Lubrificantes', 200)
armazenar_custo('Adubo', 4000)
armazenar_custo('Fungicida', 8000)
armazenar_custo('Fungicida 2 porque choveu muito', 8000)

total_custo = obter_custo_total()
print('O total do custo é de: {0}'.format(total_custo))

total_quilos = produzir_milho(10, 95)
print('O total de milho produzido foi de {0} quilos'.format(total_quilos))

quantidade_sacas = int(total_quilos / 60)
print('O total de milho produzido em sacas é de {0} sacas'.format(
    quantidade_sacas
))

valor_reais = quantidade_sacas * 100
print('O faturamento bruto foi de {0} reais'.format(valor_reais))

custo_por_quilo = total_custo / total_quilos
print('O custo de produção por quilo é de {0} reais'.format(custo_por_quilo))

custo_por_saca = custo_por_quilo * 60
print('O custo de produção por saca é de {0} reais'.format(custo_por_saca))
