import csv
from dende_statistics import Statistics

# FUNÇÃO PARA LER O CSV E CRIAR O DICIONÁRIO

def ler_csv_para_dicionario(nome_arquivo):

    print(f"Lendo arquivo: {nome_arquivo}")
    
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=',')
        
        colunas = leitor.fieldnames
        if not colunas:
            print("Arquivo vazio ou sem cabeçalho!")
            return None, None, None
            
        print(f"Colunas encontradas: {colunas}")
        
        dados_dict = {coluna: [] for coluna in colunas}
        linhas_originais = []
        
        for linha in leitor:
            linhas_originais.append(linha)
            
            for coluna in colunas:
                valor = linha.get(coluna, '')
                
                try:
                    if valor and valor.strip() and valor != 'N/A':
                        valor_limpo = valor.strip().strip('"').strip("'")
                        valor_convertido = float(valor_limpo)
                        dados_dict[coluna].append(valor_convertido)
                    else:
                        dados_dict[coluna].append(None)
                except (ValueError, TypeError):
                    valor_limpo = valor.strip().strip('"').strip("'") if valor else ''
                    dados_dict[coluna].append(valor_limpo)
        
        print(f"Total de linhas lidas: {len(linhas_originais)}")
        return dados_dict, linhas_originais, colunas

# FUNÇÃO PARA LIMPAR DADOS NÃO NUMÉRICOS

def limpar_coluna_numerica(dados_dict, coluna):
    valores_limpos = []
    valores_removidos = 0
    
    for valor in dados_dict[coluna]:
        if isinstance(valor, (int, float)) and valor is not None:
            valores_limpos.append(valor)
        else:
            valores_removidos += 1
    
    return valores_limpos, valores_removidos


def criar_dataset_numerico(dados_dict, colunas_interesse):
    """Cria um novo dicionário apenas com colunas numéricas válidas"""
    dataset_numerico = {}
    
    print("\n Processando colunas numéricas:")
    for coluna in colunas_interesse:
        if coluna in dados_dict:
            valores_limpos, removidos = limpar_coluna_numerica(dados_dict, coluna)
            
            if len(valores_limpos) > 10:
                dataset_numerico[coluna] = valores_limpos
                print(f"{coluna}: {len(valores_limpos)} válidos ({removidos} ignorados)")
            else:
                print(f"{coluna}: poucos valores ({len(valores_limpos)}), ignorando")
        else:
            print(f"{coluna}: não encontrada")
    
    return dataset_numerico

# FUNÇÃO DE ANÁLISE COM SUA CLASSE STATISTICS

def analisar_com_statistics(dataset_numerico):
    """
    Aplica todos os métodos da sua classe Statistics no dataset
    Agora incluindo absolute_frequency, relative_frequency e cumulative_frequency
    """
    print("\n" + "="*80)
    print("ANÁLISE EXPLORATÓRIA COM CLASSE STATISTICS")
    print("="*80)
    
    stats = Statistics(dataset_numerico)
    resultados = {}
    
    for coluna in dataset_numerico.keys():
        print(f"\n COLUNA: {coluna}")
        print("-" * 60)
        
        resultados[coluna] = {}
        
        # 1. MÉDIA (mean)
        try:
            media = stats.mean(coluna)
            if media is not None:
                resultados[coluna]['média'] = round(media, 4)
                print(f"  Média (mean)............: {media:.4f}")
        except Exception as e:
            print(f"Erro na média: {e}")
        
        # 2. MEDIANA (median)
        try:
            mediana = stats.median(coluna)
            if mediana is not None:
                resultados[coluna]['mediana'] = round(mediana, 4)
                print(f"  Mediana (median)........: {mediana:.4f}")
        except Exception as e:
            print(f"Erro na mediana: {e}")
        
        # 3. MODA (mode)
        try:
            moda = stats.mode(coluna)
            if moda:
                if len(moda) > 3:
                    moda_str = f"{moda[:3]}... (total: {len(moda)})"
                else:
                    moda_str = str(moda)
                resultados[coluna]['moda'] = moda
                print(f"  Moda (mode).............: {moda_str}")
        except Exception as e:
            print(f"Erro na moda: {e}")
        
        # 4. VARIÂNCIA (variance)
        try:
            variancia = stats.variance(coluna)
            if variancia is not None:
                resultados[coluna]['variância'] = round(variancia, 4)
                print(f"  Variância (variance)....: {variancia:.4f}")
        except Exception as e:
            print(f"Erro na variância: {e}")
        
        # 5. DESVIO PADRÃO (stdev)
        try:
            desvio = stats.stdev(coluna)
            if desvio is not None:
                resultados[coluna]['desvio padrão'] = round(desvio, 4)
                print(f"  Desvio Padrão (stdev)...: {desvio:.4f}")
        except Exception as e:
            print(f"Erro no desvio padrão: {e}")
        
        # 6. VALORES ÚNICOS (itemset)
        try:
            unicos = stats.itemset(coluna)
            if unicos:
                qtd_unicos = len(unicos)
                resultados[coluna]['valores únicos'] = qtd_unicos
                print(f"  Valores únicos (itemset).: {qtd_unicos}")
        except Exception as e:
            print(f"Erro no itemset: {e}")
        
        # 7. FREQUÊNCIA ABSOLUTA
        try:
            freq_abs = stats.absolute_frequency(coluna)
            if freq_abs:
                # Pega as 5 ocorrências mais comuns
                top5 = sorted(freq_abs.items(), key=lambda x: x[1], reverse=True)[:5]
                resultados[coluna]['frequência absoluta (top5)'] = dict(top5)
                print(f"  Frequência Absoluta (top5):")
                for valor, contagem in top5:
                    print(f"    {valor}: {contagem} ocorrências")
        except Exception as e:
            print(f"Erro na frequência absoluta: {e}")
        
        # 8. FREQUÊNCIA RELATIVA 
        try:
            freq_rel = stats.relative_frequency(coluna)
            if freq_rel:
                top5_rel = sorted(freq_rel.items(), key=lambda x: x[1], reverse=True)[:5]
                resultados[coluna]['frequência relativa (top5)'] = {
                    str(k): round(v*100, 2) for k, v in top5_rel
                }
                print(f"  Frequência Relativa (top5 %):")
                for valor, proporcao in top5_rel:
                    print(f"    {valor}: {proporcao*100:.2f}%")
        except Exception as e:
            print(f"Erro na frequência relativa: {e}")
        
        # 9. FREQUÊNCIA ACUMULADA 
        try:
            # Absoluta acumulada
            freq_acum_abs = stats.cumulative_frequency(coluna, 'absolute')
            if freq_acum_abs:
                items = list(freq_acum_abs.items())
                resultados[coluna]['freq acumulada final'] = items[-1][1] if items else 0
                print(f"  Frequência Acumulada (final): {items[-1][1] if items else 0}")
                
                freq_acum_rel = stats.cumulative_frequency(coluna, 'relative')
                if freq_acum_rel:
                    items_rel = list(freq_acum_rel.items())
                    resultados[coluna]['freq acumulada rel final'] = round(items_rel[-1][1] * 100, 2) if items_rel else 0
                    print(f"  Frequência Acumulada Relativa: {items_rel[-1][1]*100:.2f}%")
        except Exception as e:
            print(f"Erro na frequência acumulada: {e}")
        
        # 10. MÍNIMO E MÁXIMO
        valores = dataset_numerico[coluna]
        minimo = min(valores)
        maximo = max(valores)
        resultados[coluna]['mínimo'] = round(minimo, 4)
        resultados[coluna]['máximo'] = round(maximo, 4)
        print(f"  Mínimo.................: {minimo:.4f}")
        print(f"  Máximo..................: {maximo:.4f}")
        
        # 11. CONTAGEM
        resultados[coluna]['total amostras'] = len(valores)
        print(f"  Total amostras..........: {len(valores)}")
        
        # 12. AMPLITUDE
        amplitude = maximo - minimo
        resultados[coluna]['amplitude'] = round(amplitude, 4)
        print(f"  Amplitude...............: {amplitude:.4f}")
    
    return resultados, stats

# FUNÇÃO PARA ANALISAR COVARIÂNCIAS

def analisar_covariancias(stats, colunas):
    """Calcula a covariância entre pares de colunas"""
    print("\n" + "="*80)
    print("ANÁLISE DE COVARIÂNCIA ENTRE COLUNAS")
    print("="*80)
    
    if len(colunas) < 2:
        print("Menos de 2 colunas disponíveis")
        return []
    
    covariancias = []
    
    for i in range(len(colunas)):
        for j in range(i+1, len(colunas)):
            col_a = colunas[i]
            col_b = colunas[j]
            
            try:
                cov = stats.covariance(col_a, col_b)
                
                if cov is not None:
                    print(f"\n  {col_a}  x  {col_b}")
                    print(f"  Covariância: {cov:.4f}")
                    
                    if cov > 0:
                        print(f"    → Relação POSITIVA")
                    elif cov < 0:
                        print(f"    → Relação NEGATIVA")
                    else:
                        print(f"    → Sem relação linear")
                    
                    covariancias.append({
                        'coluna_a': col_a,
                        'coluna_b': col_b,
                        'covariancia': round(cov, 4)
                    })
            except Exception as e:
                print(f"\n Erro: {e}")
    
    return covariancias

# FUNÇÃO PARA GERAR RELATÓRIO EM TXT

def gerar_relatorio_txt(resultados, covariancias, nome_arquivo="resultados_analise_spotify.txt"):
    """Gera um arquivo de relatório detalhado"""
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write("="*90 + "\n")
        f.write("RELATÓRIO DE ANÁLISE EXPLORATÓRIA - SPOTIFY DATASET\n")
        f.write("="*90 + "\n\n")
        
        f.write("ANÁLISE REALIZADA COM CLASSE STATISTICS (dende_statistics.py)\n")
        f.write("-"*90 + "\n")
        f.write("Métodos utilizados:\n")
        f.write("  • mean()     → Média aritmética\n")
        f.write("  • median()   → Mediana\n")
        f.write("  • mode()     → Moda\n")
        f.write("  • variance() → Variância populacional\n")
        f.write("  • stdev()    → Desvio padrão populacional\n")
        f.write("  • itemset()  → Valores únicos\n")
        f.write("  • covariance() → Covariância entre colunas\n")
        f.write("  • absolute_frequency() → Frequência absoluta (NOVO!)\n")
        f.write("  • relative_frequency() → Frequência relativa (NOVO!)\n")
        f.write("  • cumulative_frequency() → Frequência acumulada (NOVO!)\n")
        f.write("-"*90 + "\n\n")
        
        f.write("\n" + "="*90 + "\n")
        f.write("ESTATÍSTICAS DESCRITIVAS POR COLUNA\n")
        f.write("="*90 + "\n")
        
        for coluna, metricas in resultados.items():
            f.write(f"\n{'─'*60}\n")
            f.write(f"COLUNA: {coluna}\n")
            f.write(f"{'─'*60}\n")
            
            ordem = [
                'média', 'mediana', 'moda', 'desvio padrão', 'variância',
                'mínimo', 'máximo', 'amplitude', 'valores únicos', 
                'frequência absoluta (top5)', 'frequência relativa (top5)',
                'freq acumulada final', 'freq acumulada rel final',
                'total amostras'
            ]
            
            for metrica in ordem:
                if metrica in metricas:
                    valor = metricas[metrica]
                    
                    if metrica == 'moda' and isinstance(valor, list):
                        if len(valor) > 5:
                            f.write(f"  {metrica.upper():<25}: {valor[:5]} ... (total: {len(valor)} modas)\n")
                        else:
                            f.write(f"  {metrica.upper():<25}: {valor}\n")
                    elif metrica in ['frequência absoluta (top5)', 'frequência relativa (top5)']:
                        f.write(f"  {metrica.upper():<25}:\n")
                        for k, v in valor.items():
                            if '%' in str(v) or isinstance(v, float):
                                f.write(f"    {k}: {v}%\n")
                            else:
                                f.write(f"    {k}: {v}\n")
                    else:
                        f.write(f"  {metrica.upper():<25}: {valor}\n")
        
        if covariancias:
            f.write("\n" + "="*90 + "\n")
            f.write("ANÁLISE DE COVARIÂNCIA\n")
            f.write("="*90 + "\n")
            
            for cov in covariancias:
                f.write(f"\n{'-'*60}\n")
                f.write(f"{cov['coluna_a']}  x  {cov['coluna_b']}\n")
                f.write(f"Covariância: {cov['covariancia']}\n")
                
                if cov['covariancia'] > 0:
                    f.write(f"→ Relação POSITIVA\n")
                elif cov['covariancia'] < 0:
                    f.write(f"→ Relação NEGATIVA\n")
                else:
                    f.write(f"→ Sem relação linear\n")
        
        f.write("\n" + "="*90 + "\n")
        f.write("FIM DO RELATÓRIO\n")
        f.write(f"Gerado em: {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("="*90 + "\n")
    
    print(f"\n Relatório gerado: {nome_arquivo}")

# FUNÇÃO PRINCIPAL

def main():
    print("ANÁLISE EXPLORATÓRIA - SPOTIFY SONGS DATASET")
    print("="*80)
    
    arquivo_csv = "spotify_data clean.csv"
    
    try:
        dados_dict, linhas, colunas = ler_csv_para_dicionario(arquivo_csv)
        if dados_dict is None:
            return
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_csv}' não encontrado!")
        return
    except Exception as e:
        print(f"Erro: {e}")
        return
    
    colunas_interesse = [
        'track_popularity',
        'artist_popularity',
        'artist_followers',
        'album_total_tracks',
        'track_duration_ms',
        'track_number'
    ]
    
    dataset_numerico = criar_dataset_numerico(dados_dict, colunas_interesse)
    
    if not dataset_numerico:
        print("Nenhuma coluna numérica válida encontrada!")
        return
    
    resultados, stats = analisar_com_statistics(dataset_numerico)
    
    colunas_analisadas = list(dataset_numerico.keys())
    covariancias = []
    
    if len(colunas_analisadas) >= 2:
        covariancias = analisar_covariancias(stats, colunas_analisadas)
    
    gerar_relatorio_txt(resultados, covariancias)
    
    print("\n" + "="*80)
    print("ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("="*80)
    print(f"\n Colunas analisadas: {', '.join(colunas_analisadas)}")
    print(f"Relatório: 'resultados_analise_spotify.txt'")

# EXECUTAR O PROGRAMA

if __name__ == "__main__":
    main()