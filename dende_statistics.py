class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):
        """
        Inicializa o objeto Statistics.

        Parâmetros
        ----------
        dataset : dict[str, list]
            O conjunto de dados, onde as chaves representam os nomes das
            colunas e os valores são as listas de dados correspondentes.
        """
        self.dataset = dataset

    def mean(self, column):
        """
        Calcula a média aritmética de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A média dos valores na coluna.
        """

        values = self.dataset[column]

        if isinstance(values[0], str):
            print("Erro: coluna não numérica")
            return None

        if not values:
            return 0.0
        
        return sum(values) / len(values)

    def median(self, column):
        """
        Calcula a mediana de uma coluna.

        A mediana é o valor central de um conjunto de dados ordenado.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O valor da mediana da coluna.
        """

        values = sorted(self.dataset[column])
        n = len(values)
        mid = n // 2
        if all(isinstance(v, (int, float)) for v in values):
            if n % 2:
                return values[mid]
            else:
                return (values[mid - 1] + values[mid]) / 2
        else:
            return values[mid]

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.

        A moda é o valor que aparece com mais frequência no conjunto de dados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        list
            Uma lista contendo o(s) valor(es) da moda.
        """
        values = self.dataset[column]
        frequency = {}
        for value in values:
            frequency[value] = frequency.get(value, 0) + 1
        max_freq = max(frequency.values())
        return [key for key, freq in frequency.items() if freq == max_freq]

    def variance(self, column):#GIOVANNA - TESTADO = OK

        if column not in self.dataset:
            return None

        dados = self.dataset[column]#extraindo os dados das colunas

        if len(dados) == 0:#caso a coluna esteja vazia
            return None
        
        media = sum(dados) / len(dados)#tirando a média da coluna

        soma_quadrados = sum((x - media) ** 2 for x in dados)#ao quadrado de cada desvio

        variancia_populacional = soma_quadrados / len(dados)#média novamente

        return variancia_populacional
    

    def stdev(self, column):#GIOVANNA - TESTADO = OK

        variancia_populacional = self.variance(column)#extraindo dados

        if variancia_populacional is None:#caso a coluna esteja vazia
            return None

        desvio = variancia_populacional ** 0.5#raiz quadrada

        return desvio

    def covariance(self, column_a, column_b):#GIOVANNA - Testado = OK

        valores_A = self.dataset[column_a]#extraindo os dados das colunas
        valores_B = self.dataset[column_b]#extraindo os dados das colunas

        n = len(valores_A)#len para saber o tamanho
        media_A = sum(valores_A) / len(valores_A)#média
        media_B = sum(valores_B) / len(valores_B)#média

        desvios_A = []#armazenar os devios da coluna A
        for x in valores_A:#listando os desvios
            desvios_A.append( x - media_A)

        desvios_B = []#armazenar os devios da coluna B
        for x in valores_B:#listando os desvios
            desvios_B.append( x - media_B)

        soma_produtos = 0#começand do zero a soma dos produtos

        for da, db in zip(desvios_A, desvios_B):#zip para unir em pares
            soma_produtos += (da * db)#armazenando a soma dos produtos

        resultado = soma_produtos / n #média de relacionamento

        return float(resultado)

    def itemset(self, column):#GIOVANNA - Testado = OK

        valores_unicos = set(self.dataset[column])# set -> separa os valores únicos

        return valores_unicos

    def absolute_frequency(self, column):
        """
        Calcula a frequência absoluta de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas contagens (frequência absoluta).
        """
        pass

    def relative_frequency(self, column):
        """
        Calcula a frequência relativa de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas proporções (frequência relativa).
        """
        pass

    def cumulative_frequency(self, column, frequency_method='absolute'):
        """
        Calcula a frequência acumulada (absoluta ou relativa) de uma coluna.

        A frequência é calculada sobre os itens ordenados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        frequency_method : str, opcional
            O método a ser usado: 'absolute' para contagem acumulada ou
            'relative' para proporção acumulada (padrão é 'absolute').

        Retorno
        -------
        dict
            Um dicionário ordenado com os itens como chaves e suas
            frequências acumuladas como valores.
        """
        pass

    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        pass

    def quartiles(self, column):
        """
        Calcula os quartis (Q1, Q2 e Q3) de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário com os quartis Q1, Q2 (mediana) e Q3.
        """
        pass

    def histogram(self, column, bins):
        """
        Gera um histograma baseado em buckets (intervalos).

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        bins : int
            Número de buckets (intervalos).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os intervalos (tuplas)
            e os valores são as contagens.
        """
        pass
