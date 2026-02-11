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
        pass

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
        pass

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
        pass

    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        pass

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """
        pass

    def covariance(self, column_a, column_b):
        """
        Calcula a covariância entre duas colunas.

        Parâmetros
        ----------
        column_a : str
            O nome da primeira coluna (X).
        column_b : str
            O nome da segunda coluna (Y).

        Retorno
        -------
        float
            O valor da covariância entre as duas colunas.
        """
        pass

    def itemset(self, column):
        """
        Retorna o conjunto de itens únicos em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        set
            Um conjunto com os valores únicos da coluna.
        """
        pass

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
        # Recebe os valores do dataset
        values = self.dataset[column]

        # Contadores para a fórmula
        total_b = 0  # Quantas vezes o valor condicionante aparece (divisor)
        sucessos_ba = 0  # Quantas vezes a sequência (B -> A) ocorre (numerador)

        # Percorre até o penúltimo elemento
        for i in range(len(values) - 1):
            # Verifica se o elemento atual é o condicionante (B)
            if values[i] == value2:
                total_b += 1

                # Verifica se o consequente (A) aparece imediatamente após o condicionante (B)
                if values[i + 1] == value1:
                    sucessos_ba += 1
        # Proteção contra divisão por zero (caso value2 não exista ou seja o último)
        if total_b == 0:
            return 0.0

        return sucessos_ba / total_b
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

        # Recebendo os valores do dataset
        values = sorted(self.dataset[column])
        n = len(values)

        # Caso a quantidade de valores for igual a zero
        if n == 0:
            return {"Q1": 0, "Q2": 0, "Q3": 0}

        # Cálculo do Q2 (Mediana)
        mid = n // 2
        if n % 2 == 0:
            q2 = (values[mid - 1] + values[mid]) / 2
            # O fatiamento começa do início até o mid
            lower_half = values[:mid]
            # O fatiamento começa do mid até o final
            upper_half = values[mid:]
        else:
            q2 = values[mid]
            # Para n ímpar, a mediana (Q2) é excluída de ambas as metades
            lower_half = values[:mid]
            upper_half = values[mid + 1:]

        # Cálculo do Q1 (Mediana da Metade Inferior)
        n_lower = len(lower_half)
        mid_l = n_lower // 2
        if n_lower % 2 == 0:
            q1 = (lower_half[mid_l - 1] + lower_half[mid_l]) / 2
        else:
            q1 = (lower_half[mid_l])

        # Cálculo do Q3 (Mediana da Metade Superior
        n_upper = len(upper_half)
        mid_u = n_upper // 2
        if n_upper % 2 == 0:
            q3 = (upper_half[mid_u - 1] + upper_half[mid_u]) / 2
        else:
            q3 = (upper_half[mid_u])

        return {"Q1": q1, "Q2": q2, "Q3": q3}
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

        valores = self.dataset[column]
        menor_valor,  valor_maior = min(valores), max(valores)
        numero_bins = 4
        tamanho_bin = (valor_maior - menor_valor) / numero_bins

        # Criação os limites dos intervalos (os buckets)
        limites = []
        for i in range(numero_bins + 1):
            ponto = menor_valor + (i * tamanho_bin)
            limites.append(ponto)

        # Geração do dicionário com tuplas como chaves (Início, Fim)
        # Ex: {(20.0, 35.0): 0, (35.0, 50.0): 0, ...}
        histograma = {}
        for i in range(numero_bins):
            intervalo = (limites[i], limites[i + 1])
            histograma[intervalo] = 0

        # Realização da contagem
        for valor in valores:
            indice = int((valor - menor_valor) / tamanho_bin)

            # Ajuste para o valor máximo
            if indice == numero_bins:
                indice -= 1

            # Recupera a chave (tupla) correspondente ao índice para incrementar (Ex: (20.0, 35.0))
            chave_intervalo = (limites[indice], limites[indice + 1])
            histograma[chave_intervalo] += 1

        return histograma

        pass