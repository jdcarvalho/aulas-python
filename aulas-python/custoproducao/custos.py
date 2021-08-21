
def limpar_banco_existente():
    """
    Limpa o banco de ados existentes para fins de ensino
    :return:
    """
    import os
    if os.path.exists('custos.csv'):
        os.remove('custos.csv')


def armazenar_custo(descricao_custo, valor_custo):
    """
    Essa função irá armazenar os custos de produção em um arquivo CSV
    :param descricao_custo: Descritivo do custo a ser guardado
    :param valor_custo: Valor do custo em reais
    :return:
    """
    from datetime import datetime
    f = open('custos.csv', 'a')
    hoje = datetime.now().strftime('%d/%m/%Y')
    dados = [hoje, descricao_custo, valor_custo]
    f.write(','.join(['"' + str(x) + '"' for x in dados]) + '\n')
    f.close()


def obter_custo_total():
    """
    Retorna o custo total obtido da planilha de custos
    :return:
    """
    f = open('custos.csv', 'r')

    resultados = list()

    for linha in f.readlines():
        """"
        Estrutura de repetição
        """
        dados = linha.split(',')
        ultimo = dados[-1]
        ultimo = ultimo.replace('"', '')
        resultados.append(float(ultimo))
    return sum(resultados)


def produzir_milho(quantidade_terra, indice_chuva):
    """

    Baseado na quantidade de terra em hectares e sabendo que um hectare
    produz em média 3600kg de milho calcular a produtividade

    O índice de chuva é baseado em 100% para chuvas regulares. e quanto menor o
    índice de chuvas deve ser reflitdo como perda de produção:

    Exemplo. para um índice de 95% de chuvas deve-se dar uma quebra de 5%
    na safra

    :return:
    """
    total_produzido = quantidade_terra * 3600

    if indice_chuva < 0 or indice_chuva > 100:
        raise ValueError('Índice de chuva deve ser entre 0 e 100, bocó')

    if indice_chuva < 100:
        # Por exemplo 5% de quebra
        percentual_quebra = 100 - indice_chuva
        total_quebra = (total_produzido * percentual_quebra) / 100
        total_produzido = total_produzido - total_quebra

    return total_produzido
